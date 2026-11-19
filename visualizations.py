
# DIAMOND DATASET - DATA VISUALIZATION

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned dataset
df = pd.read_csv("data/processed/diamonds_cleaned.csv")

# Create folder to save graphs
os.makedirs("graphs", exist_ok=True)

# Set graph style
sns.set_style("whitegrid")


# GRAPH 1: PRICE DISTRIBUTION

plt.figure(figsize=(10, 6))

sns.histplot(data=df, x="price", bins=50, kde=True)

plt.title("Distribution of Diamond Prices")
plt.xlabel("Diamond Price")
plt.ylabel("Number of Diamonds")

plt.savefig("graphs/01_price_distribution.png")
plt.show()


# GRAPH 2: CARAT DISTRIBUTION

plt.figure(figsize=(10, 6))

sns.histplot(data=df, x="carat", bins=40, kde=True)

plt.title("Distribution of Diamond Carat")
plt.xlabel("Carat")
plt.ylabel("Number of Diamonds")

plt.savefig("graphs/02_carat_distribution.png")
plt.show()


# GRAPH 3: DIAMOND CUT COUNT

plt.figure(figsize=(10, 6))

sns.countplot(data=df, x="cut", order=df["cut"].value_counts().index)

plt.title("Number of Diamonds by Cut")
plt.xlabel("Diamond Cut")
plt.ylabel("Number of Diamonds")

plt.savefig("graphs/03_cut_count.png")
plt.show()


# GRAPH 4: DIAMOND COLOR COUNT

plt.figure(figsize=(10, 6))

sns.countplot(data=df, x="color", order=df["color"].value_counts().index)

plt.title("Number of Diamonds by Color")
plt.xlabel("Diamond Color")
plt.ylabel("Number of Diamonds")

plt.savefig("graphs/04_color_count.png")
plt.show()


# GRAPH 5: DIAMOND CLARITY COUNT

plt.figure(figsize=(10, 6))

sns.countplot(data=df, x="clarity", order=df["clarity"].value_counts().index)

plt.title("Number of Diamonds by Clarity")
plt.xlabel("Diamond Clarity")
plt.ylabel("Number of Diamonds")

plt.savefig("graphs/05_clarity_count.png")
plt.show()


# GRAPH 6: PRICE BY CUT

plt.figure(figsize=(10, 6))

sns.barplot(data=df, x="cut", y="price", errorbar=None)

plt.title("Average Diamond Price by Cut")
plt.xlabel("Diamond Cut")
plt.ylabel("Average Price")

plt.savefig("graphs/06_price_by_cut.png")
plt.show()


# GRAPH 7: PRICE BY COLOR

plt.figure(figsize=(10, 6))

sns.barplot(data=df, x="color", y="price", errorbar=None)

plt.title("Average Diamond Price by Color")
plt.xlabel("Diamond Color")
plt.ylabel("Average Price")

plt.savefig("graphs/07_price_by_color.png")
plt.show()


# GRAPH 8: PRICE BY CLARITY

plt.figure(figsize=(10, 6))

sns.barplot(data=df, x="clarity", y="price", errorbar=None)

plt.title("Average Diamond Price by Clarity")
plt.xlabel("Diamond Clarity")
plt.ylabel("Average Price")

plt.savefig("graphs/08_price_by_clarity.png")
plt.show()

# GRAPH 9: CARAT VS PRICE

plt.figure(figsize=(10, 6))

sns.scatterplot(data=df, x="carat", y="price", alpha=0.4)

plt.title("Relationship Between Carat and Price")
plt.xlabel("Carat")
plt.ylabel("Price")

plt.savefig("graphs/09_carat_vs_price.png")
plt.show()


# GRAPH 10: VOLUME VS PRICE

plt.figure(figsize=(10, 6))

sns.scatterplot(data=df, x="volume", y="price", alpha=0.4)

plt.title("Relationship Between Volume and Price")
plt.xlabel("Diamond Volume")
plt.ylabel("Price")

plt.savefig("graphs/10_volume_vs_price.png")
plt.show()


# GRAPH 11: CORRELATION HEATMAP

plt.figure(figsize=(10, 8))

correlation = df.select_dtypes(include="number").corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap of Diamond Features")

plt.savefig("graphs/11_correlation_heatmap.png")
plt.show()


# GRAPH 12: PRICE BY CUT BOXPLOT

plt.figure(figsize=(10, 6))

sns.boxplot(data=df, x="cut", y="price")

plt.title("Price Distribution Across Diamond Cuts")
plt.xlabel("Diamond Cut")
plt.ylabel("Price")

plt.savefig("graphs/12_price_by_cut_boxplot.png")
plt.show()

# GRAPH 13: CARAT VS VOLUME

plt.figure(figsize=(10, 6))

sns.scatterplot(data=df, x="carat", y="volume", alpha=0.4)

plt.title("Relationship Between Carat and Volume")
plt.xlabel("Carat")
plt.ylabel("Volume")

plt.savefig("graphs/13_carat_vs_volume.png")
plt.show()

# GRAPH 14: PRICE VS DEPTH

plt.figure(figsize=(10, 6))

sns.scatterplot(data=df, x="depth", y="price", alpha=0.4)

plt.title("Relationship Between Depth and Price")
plt.xlabel("Depth")
plt.ylabel("Price")

plt.savefig("graphs/14_price_vs_depth.png")
plt.show()


# GRAPH 15: PAIRPLOT

sample_df = df[["carat", "depth", "table", "price", "volume"]].sample(
    n=1000,
    random_state=42
)

pair_plot = sns.pairplot(sample_df)

pair_plot.savefig("graphs/15_pairplot.png")
plt.show()


print("\nAll graphs generated successfully")


