import pandas as pd
import numpy as np


# 1. Load and explore the data

input_file = "data/trends_clean.csv"

df = pd.read_csv(input_file)

print(f"Loaded data: {df.shape}")

print("\nFirst 5 rows:")
print(df.head())

print(f"\nAverage score: {df['score'].mean():.2f}")
print(f"Average comments: {df['num_comments'].mean():.2f}")


# 2. Basic analysis with NumPy

scores = df["score"].to_numpy()

mean_score = np.mean(scores)
median_score = np.median(scores)
std_score = np.std(scores)
max_score = np.max(scores)
min_score = np.min(scores)

print("\n--- NumPy Stats ---")
print(f"Mean score     : {mean_score:.2f}")
print(f"Median score   : {median_score:.2f}")
print(f"Std deviation  : {std_score:.2f}")
print(f"Max score      : {max_score}")
print(f"Min score      : {min_score}")


# Category with the most stories
category_counts = df["category"].value_counts()
most_common_category = category_counts.idxmax()
most_common_count = category_counts.max()

print(
    f"\nMost stories in: {most_common_category} "
    f"({most_common_count} stories)"
)


# Story with the most comments
most_commented_index = df["num_comments"].idxmax()
most_commented_story = df.loc[most_commented_index]

print(
    f"\nMost commented story: "
    f"{most_commented_story['title']} "
    f"— {most_commented_story['num_comments']} comments"
)


# 3. Add new columns

# Engagement shows how much discussion a story gets
# compared with its score.
df["engagement"] = df["num_comments"] / (df["score"] + 1)


# A story is popular when its score is above the average score.
df["is_popular"] = df["score"] > mean_score


# 4. Save the analysed data

output_file = "data/trends_analysed.csv"

df.to_csv(output_file, index=False)

print(f"\nSaved to {output_file}")
