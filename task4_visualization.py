import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Setup

input_file = "data/trends_analysed.csv"
output_dir = Path("outputs")

# Create the outputs folder if it does not exist
output_dir.mkdir(exist_ok=True)

# Load the analysed CSV
df = pd.read_csv(input_file)

print(f"Loaded data: {df.shape}")


# 2. Chart 1 - Top 10 Stories by Score

top_10 = df.nlargest(10, "score").sort_values("score")

# Shorten long titles to 50 characters
top_10["short_title"] = top_10["title"].apply(
    lambda title: title[:50] + "..." if len(title) > 50 else title
)

plt.figure(figsize=(10, 6))

plt.barh(top_10["short_title"], top_10["score"])

plt.title("Top 10 Stories by Score")
plt.xlabel("Score")
plt.ylabel("Story")

plt.tight_layout()

plt.savefig(output_dir / "chart1_top_stories.png")
plt.show()
plt.close()


# 3. Chart 2 - Stories per Category

category_counts = df["category"].value_counts()

plt.figure(figsize=(10, 6))

plt.bar(
    category_counts.index,
    category_counts.values,
    color=[f"C{i}" for i in range(len(category_counts))]
)

plt.title("Stories per Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(output_dir / "chart2_categories.png")
plt.show()

plt.close()


# 4. Chart 3 - Score vs Comments

plt.figure(figsize=(10, 6))

popular = df["is_popular"] == True
not_popular = df["is_popular"] == False

plt.scatter(
    df.loc[not_popular, "score"],
    df.loc[not_popular, "num_comments"],
    label="Not Popular"
)

plt.scatter(
    df.loc[popular, "score"],
    df.loc[popular, "num_comments"],
    label="Popular"
)

plt.title("Score vs Comments")
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.legend()

plt.tight_layout()

plt.savefig(output_dir / "chart3_scatter.png")
plt.show()

plt.close()


# 5. Bonus - Dashboard

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Chart 1
axes[0].barh(top_10["short_title"], top_10["score"])
axes[0].set_title("Top 10 Stories by Score")
axes[0].set_xlabel("Score")
axes[0].set_ylabel("Story")


# Chart 2
axes[1].bar(
    category_counts.index,
    category_counts.values,
    color=[f"C{i}" for i in range(len(category_counts))]
)
axes[1].set_title("Stories per Category")
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Number of Stories")
axes[1].tick_params(axis="x", rotation=45)


# Chart 3
axes[2].scatter(
    df.loc[not_popular, "score"],
    df.loc[not_popular, "num_comments"],
    label="Not Popular"
)

axes[2].scatter(
    df.loc[popular, "score"],
    df.loc[popular, "num_comments"],
    label="Popular"
)

axes[2].set_title("Score vs Comments")
axes[2].set_xlabel("Score")
axes[2].set_ylabel("Number of Comments")
axes[2].legend()


fig.suptitle("TrendPulse Dashboard")

plt.tight_layout()

plt.savefig(output_dir / "dashboard.png")
plt.show()

plt.close()

print("\nAll charts saved successfully!")