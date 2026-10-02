import requests
from datetime import datetime
collected_at = datetime.now().isoformat()

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"

response = requests.get(TOP_STORIES_URL)
story_ids = response.json()

print("Total story IDs:", len(story_ids))

print("First 10 story IDs:")
print(story_ids[:10])
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

first_story_id = story_ids[0]

story_response = requests.get(
    ITEM_URL.format(first_story_id),
    headers={"user-agent": "TrendPulse/1.0"}
)

story_details = story_response.json()

print("Story details:")
print(story_details)
print("Title:", story_details.get("title"))
print("Author:", story_details.get("by"))
print("Score:", story_details.get("score"))
print("Comments:", story_details.get("descendants"))
print("Story ID:", story_details.get("id"))
categories = {
    "technology": [
        "ai", "software", "tech", "code", "computer",
        "data", "cloud", "api", "gpu", "llm"
    ],

    "worldnews": [
        "war", "government", "country", "president",
        "election", "climate", "attack", "global"
    ],

    "sports": [
        "nfl", "nba", "fifa", "sport", "game", "team",
        "player", "league", "championship"
    ],

    "science": [
        "research", "study", "space", "physics",
        "biology", "discovery", "nasa", "genome"
    ],

    "entertainment": [
        "movie", "film", "music", "netflix", "game",
        "book", "show", "award", "streaming"
    ]
}
def classify_title(title):

    title = title.lower()

    for category, keywords in categories.items():

        for keyword in keywords:

            if keyword in title:
                return category

    return "other"


   

print("Category:", classify_title(story_details.get("title", "")))
collected_at = datetime.now().isoformat()

print("Collected at:", collected_at)



print()
print("Testing loop:")

records = []


for story_id in story_ids[:500]:
    print("Processing:", story_id, flush=True)


    story_response = requests.get(
    ITEM_URL.format(story_id),
    headers={"user-agent": "TrendPulse/1.0"},
    timeout=10
)

    story = story_response.json()


    record = {
        "post_id": story.get("id"),
        "title": story.get("title", ""),
        "category": classify_title(story.get("title", "")),
        "score": story.get("score", 0),
        "num_comments": story.get("descendants", 0),
        "author": story.get("by", ""),
        "collected_at": datetime.now().isoformat()
    }

    records.append(record)


print("Total records collected:", len(records))
import csv

with open("data/hacker_news_stories.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=records[0].keys())
    writer.writeheader()
    writer.writerows(records)

print("CSV file saved successfully!")

import json
from datetime import datetime

today = datetime.now().strftime("%Y%m%d")
json_file = f"data/trends_{today}.json"

with open(json_file, "w", encoding="utf-8") as file:
    json.dump(records, file, indent=2, ensure_ascii=False)

print(f"Collected {len(records)} stories. Saved to {json_file}")