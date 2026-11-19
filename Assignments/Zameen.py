from pathlib import Path
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "zameencom-property-data-By-Kaggle-Short.csv"
OUTPUT_FILE = BASE_DIR / "zameen_cleaned.csv"

if not INPUT_FILE.exists():
    raise FileNotFoundError(
        f"CSV nahi mili. Is path par rakhein: {INPUT_FILE}"
    )

# 1. Load (file ';' se separate hoti hai)
df = pd.read_csv(INPUT_FILE, sep=";")
print("Loaded:", df.shape)

# 2. Duplicates hatao
df = df.drop_duplicates()
df = df.drop_duplicates(subset="property_id")

# 3. Constant columns hatao
constant_cols = [c for c in df.columns if df[c].nunique(dropna=False) <= 1]
df = df.drop(columns=constant_cols)
print("Dropped constant columns:", constant_cols)

# 4. Text cleaning
text_cols = [c for c in df.columns if pd.api.types.is_string_dtype(df[c])]
for col in text_cols:
    df[col] = df[col].str.strip()
df["location"] = df["location"].str.title()
df["property_type"] = df["property_type"].str.title()

# 5. Missing agency / agent
df["agency"] = df["agency"].fillna("Unknown")
df["agent"] = df["agent"].fillna("Unknown")

# 6. Date
df["date_added"] = pd.to_datetime(df["date_added"], format="%m-%d-%Y", errors="coerce")

# 7. 0 bedrooms/baths = missing
df["bedrooms"] = df["bedrooms"].replace(0, np.nan)
df["baths"] = df["baths"].replace(0, np.nan)

# 8. Area -> Marla (1 Kanal = 20 Marla)
def area_to_marla(text):
    parts = str(text).split()
    if len(parts) != 2:
        return np.nan
    value = float(parts[0])
    unit = parts[1].lower()
    if unit.startswith("kanal"):
        return value * 20
    if unit.startswith("marla"):
        return value
    return np.nan

df["area_marla"] = df["area"].apply(area_to_marla)
df["area_sqft"] = (df["area_marla"] * 272.25).round(0)
df = df.drop(columns=["area"])

# 9. Price outliers flag (delete nahi, sirf flag)
q1, q3 = df["price"].quantile([0.25, 0.75])
upper = q3 + 3 * (q3 - q1)
df["price_outlier"] = df["price"] > upper
df["price_per_marla"] = (df["price"] / df["area_marla"]).round(0)

# 10. Coordinates check (Lahore area)
bad_coords = ~(
    df["latitude"].between(31.2, 31.8) & df["longitude"].between(74.0, 74.7)
)
print("Rows with suspicious coordinates:", bad_coords.sum())
df.loc[bad_coords, ["latitude", "longitude"]] = np.nan

# 11. Result
print("\nMissing values after cleaning:")
print(df.isnull().sum())
print("\nCleaned shape:", df.shape)
print("Price outliers flagged:", df["price_outlier"].sum())

df.to_csv(OUTPUT_FILE, index=False)
print("\nSaved to:", OUTPUT_FILE)