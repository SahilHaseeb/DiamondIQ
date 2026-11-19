
from pathlib import Path
import pandas as pd

# Data Quality Investigation

data_folder = Path("data")
csv_files = list(data_folder.glob("*.csv"))

if not csv_files:
    print("No CSV file found in the data folder.")

else:
    file_path = csv_files[0]
    df = pd.read_csv(file_path)


    print("DIAMOND DATA QUALITY INVESTIGATION")
   
    # 1. Dataset size
    print("\n1. Dataset shape:")
    print(df.shape)

    # 2. Duplicate records
    print("\n2. Duplicate rows:")
    print(df.duplicated().sum())

    # 3. Zero dimensions
    print("\n3. Records with zero dimensions:")
    for col in ["x", "y", "z"]:
        #x=length , y=width , z=Depth/height
        zero_count = (df[col] == 0).sum()
        print(f"{col}: {zero_count}")
     # Ulternative method
#print("X zero values:", (df["x"] == 0).sum())
# print("Y zero values:", (df["y"] == 0).sum())
# print("Z zero values:", (df["z"] == 0).sum())

    # 4. Inspect suspicious dimensions
    print("\n4. Records with zero dimensions:")
    zero_dimensions = df[
        (df["x"] == 0) |
        (df["y"] == 0) |
        (df["z"] == 0)
    ]

    print(zero_dimensions.head(10))
    print("Total suspicious dimension records:",
          len(zero_dimensions))

    # 5. Check the index-like column
    print("\n5. Unnamed column inspection:")
    print(df["Unnamed: 0"].head())
    print("Unique values:",
          df["Unnamed: 0"].nunique())
    print("Sequential index:",
          df["Unnamed: 0"].equals(
              pd.Series(range(1, len(df) + 1))
          ))

    # 6. Statistical summary of numeric features
    print("\n6. Numeric feature statistics:")
    print(df.describe())

    # 7. Check categorical values
    print("\n7. Categories in each categorical column:")
    for col in ["cut", "color", "clarity"]:
        print(f"\n{col}:")
        print(df[col].value_counts())

    #8. ALL ZERO-DIMENSION RECORDS
print("\n8. ALL ZERO-DIMENSION RECORDS:")

zero_records = df[
    (df["x"] == 0) |
    (df["y"] == 0) |
    (df["z"] == 0)
]

print(zero_records.to_string(index=False))

    #9. LARGEST Y DIMENSIONS
print("\n9. LARGEST Y DIMENSIONS:")

print(
    df.nlargest(10, "y")[["carat", "x", "y", "z", "price"]]
)

    #10. LARGEST Z DIMENSIONS
print("\n10. LARGEST Z DIMENSIONS:")

print(
    df.nlargest(10, "z")[["carat", "x", "y", "z", "price"]]
)


#.................Now we clean the DATA.................
# //////////////DATA CLEANING/////////////

print("\n" + "=" * 50)
print(" DATA CLEANING")
print("=" * 50)

# 1. Remove unnecessary index column (unnamed)
df = df.drop(columns=["Unnamed: 0"])

print("\n1. Unnecessary column removed.")
print("Remaining columns:", df.columns.tolist())


# 2. Find records having zero dimensions
zero_mask = (df[["x", "y", "z"]] == 0).any(axis=1)

print("\n2. Records with zero dimensions:", zero_mask.sum())


# 3. Remove records having zero dimensions
df_clean = df.loc[~zero_mask].copy()

print("\n3. Zero-dimension records removed.")


# 4. Verify cleaned dataset
print("\n4. Cleaned dataset shape:")
print(df_clean.shape)

print("\n5. Remaining zero dimensions:")
print((df_clean[["x", "y", "z"]] == 0).sum())

print("\n6. Missing values:")
print(df_clean.isnull().sum())

print("\n7. Duplicate rows:")
print(df_clean.duplicated().sum())


# 5. Save cleaned dataset
from pathlib import Path

output_folder = Path("data/processed")
output_folder.mkdir(parents=True, exist_ok=True)

df_clean.to_csv(output_folder / "diamonds_cleaned.csv", index=False)



# .................... DUPLICATE RECORD INVESTIGATION............

print("\n" + "=" * 50)
print(" DUPLICATE INVESTIGATION")
print("=" * 50)

# 1. Count extra duplicate records

duplicate_count = df_clean.duplicated().sum()

print("\n1. Extra duplicate records:", duplicate_count)


# 2. Count all rows involved in duplicate groups

all_duplicate_rows = df_clean.duplicated(keep=False).sum()

print("2. Total rows involved in duplicates:", all_duplicate_rows)


# 3. Display duplicate records
duplicate_records = df_clean[
    df_clean.duplicated(keep=False)
]

print("\n3. Duplicate records:")
print(duplicate_records.head(20).to_string(index=False))


# 4. Check dataset shape
print("\n4. Current dataset shape:")
print(df_clean.shape)


# STEP 3: REMOVE DUPLICATE RECORDS

print("\n" + "=" * 50)
print("STEP 3: REMOVE DUPLICATES")
print("=" * 50)

# 1. Count duplicates before removal
before = df_clean.duplicated().sum()

print("\n1. Duplicates before removal:", before)


# 2. Remove duplicate records
df_clean = df_clean.drop_duplicates().copy()


# 3. Count duplicates after removal
after = df_clean.duplicated().sum()

print("2. Duplicates after removal:", after)


# 4. Check new dataset shape
print("\n3. Dataset shape after duplicate removal:")
print(df_clean.shape)


# 5. Save final cleaned dataset
df_clean.to_csv(
    output_folder / "diamonds_cleaned.csv",
    index=False
)



# ............OUTLIER DETECTION USING IQR..............

print("\n" + "=" * 50)
print(" OUTLIER DETECTION")
print("=" * 50)

# Columns for outlier investigation
columns = ["carat", "depth", "table", "price", "x", "y", "z"]

for col in columns:

    Q1 = df_clean[col].quantile(0.25)
    Q3 = df_clean[col].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df_clean[
        (df_clean[col] < lower_limit) |
        (df_clean[col] > upper_limit)
    ]

    print("\nColumn:", col)
    print("Lower limit:", round(lower_limit, 2))
    print("Upper limit:", round(upper_limit, 2))
    print("Outliers:", len(outliers))
    
    
    # ............INVESTIGATE DIMENSION OUTLIERS...........

print("\n" + "=" * 50)
print("DIMENSION OUTLIER INVESTIGATION")
print("=" * 50)

dimension_columns = ["x", "y", "z"]

for col in dimension_columns:

    Q1 = df_clean[col].quantile(0.25)
    Q3 = df_clean[col].quantile(0.75)

    IQR = Q3 - Q1

    upper_limit = Q3 + 1.5 * IQR

    suspicious = df_clean[df_clean[col] > upper_limit]

    print("\nColumn:", col)
    print("Upper limit:", round(upper_limit, 2))

    print(
        suspicious.nlargest(10, col)[
            ["carat", "cut", "price", "x", "y", "z"]
        ].to_string(index=False)
    )


# Check all dimensions together
print("\nRecords with unusual dimensions:")

x_limit = df_clean["x"].quantile(0.75) + 1.5 * (
    df_clean["x"].quantile(0.75) - df_clean["x"].quantile(0.25)
)

y_limit = df_clean["y"].quantile(0.75) + 1.5 * (
    df_clean["y"].quantile(0.75) - df_clean["y"].quantile(0.25)
)

z_limit = df_clean["z"].quantile(0.75) + 1.5 * (
    df_clean["z"].quantile(0.75) - df_clean["z"].quantile(0.25)
)

dimension_outliers = df_clean[
    (df_clean["x"] > x_limit) |
    (df_clean["y"] > y_limit) |
    (df_clean["z"] > z_limit)
]

print("Total unique suspicious records:", len(dimension_outliers))


# ...........IDENTIFY EXTREME DIMENSION ERRORS...............

print("\n" + "=" * 50)
print("EXTREME DIMENSION ERROR INVESTIGATION")
print("=" * 50)

# Find records where one dimension is extremely large
extreme_errors = df_clean[
    (df_clean["x"] > 20) |
    (df_clean["y"] > 20) |
    (df_clean["z"] > 20)
]

print("Total extreme dimension errors:", len(extreme_errors))

print("\nSuspicious records:")
print(
    extreme_errors[
        ["carat", "price", "x", "y", "z"]
    ].to_string(index=False)
)



# ............REMOVE EXTREME DIMENSION ERRORS.................

print("\n" + "=" * 50)
print("REMOVING EXTREME DIMENSION ERRORS")
print("=" * 50)

# Count records before removal
before = len(df_clean)

# Keep records where all dimensions are 20 or less
df_clean = df_clean[
    (df_clean["x"] <= 20) &
    (df_clean["y"] <= 20) &
    (df_clean["z"] <= 20)
].copy()

# Count records after removal
after = len(df_clean)

print("Records before:", before)
print("Records removed:", before - after)
print("Records after:", after)

# Verify extreme values
print("\nRemaining extreme records:")

remaining = df_clean[
    (df_clean["x"] > 20) |
    (df_clean["y"] > 20) |
    (df_clean["z"] > 20)
]

print(len(remaining))

# Save cleaned dataset
df_clean.to_csv(
    output_folder / "diamonds_cleaned.csv",
    index=False
)




# ................FEATURE ENGINEERING.................

print("\n" + "=" * 50)
print("FEATURE ENGINEERING")
print("=" * 50)

# Calculate diamond volume
df_clean["volume"] = (
    df_clean["x"] *
    df_clean["y"] *
    df_clean["z"]
)

# Display new feature
print("\nDataset with new Volume feature:")

print(
    df_clean[
        ["carat", "x", "y", "z", "volume", "price"]
    ].head(10)
)

# Display volume statistics
print("\nVolume Statistics:")

print(df_clean["volume"].describe())

# Save updated dataset
df_clean.to_csv(
    output_folder / "diamonds_cleaned.csv",
    index=False
)

print("\nFeature engineering completed!")




# ..............DESCRIPTIVE STATISTICS....................

print("\n" + "=" * 50)
print("DESCRIPTIVE STATISTICS")
print("=" * 50)

# 1. Statistics of numerical columns
print("\nNumerical Data Statistics:")

print(df_clean.describe().round(2))

# 2. Statistics of categorical columns
print("\nCategorical Data Statistics:")

print(df_clean.describe(include="object"))

# 3. Average diamond price
print("\nAverage Diamond Price:")

print(df_clean["price"].mean())

# 4. Highest and lowest diamond price
print("\nHighest Diamond Price:")
print(df_clean["price"].max())

print("\nLowest Diamond Price:")
print(df_clean["price"].min())

# 5. Average carat
print("\nAverage Carat:")
print(df_clean["carat"].mean())

# 6. Number of diamonds in each cut category
print("\nDiamonds by Cut:")

print(df_clean["cut"].value_counts())

# 7. Number of diamonds in each clarity category
print("\nDiamonds by Clarity:")

print(df_clean["clarity"].value_counts())

# 8. Number of diamonds in each color category
print("\nDiamonds by Color:")

print(df_clean["color"].value_counts())

print("\nDescriptive Statistics Completed!")
