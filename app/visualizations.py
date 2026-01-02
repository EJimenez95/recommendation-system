import matplotlib
matplotlib.use("Agg")#Use non-GUI backend for saving images
import matplotlib.pyplot as plt
import seaborn as sns
import os

#Directory where plots will be saved
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


#Create a heatmap showing user ratings across characters
def ratings_heatmap(users, items):
    import pandas as pd

    data = []

    #Build rows for each user
    for user in users.values():
        row = {"user_id": user.username}
        for item_id, rating in user.ratings.items():
            row[items[item_id].name] = rating
        data.append(row)

    #Create DataFrame and set user names as index
    df = pd.DataFrame(data).set_index("user_id")

    plt.figure(figsize=(12, 6))
    sns.heatmap(df, annot=True, cmap="YlGnBu")
    plt.title("User Ratings Heatmap")
    plt.xlabel("Character")
    plt.ylabel("User")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/ratings_heatmap.png")
    plt.close()


#Create bar chart of characters ranked by average rating
def popular_characters_bar(items, users):
    import pandas as pd

    avg_ratings = {}

    #Compute average rating per character
    for item in items.values():
        ratings = [
            user.ratings[item.item_id]
            for user in users.values()
            if item.item_id in user.ratings
        ]
        avg_ratings[item.name] = sum(ratings) / len(ratings) if ratings else 0

    df = pd.Series(avg_ratings).sort_values(ascending=False)

    plt.figure(figsize=(12, 6))
    df.plot(kind="bar")
    plt.title("Most Popular Characters")
    plt.ylabel("Average Rating")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/popular_characters.png")
    plt.close()


#Create pie chart showing Hero vs Villain vs Neutral distribution
def hero_villain_pie(items):
    counts = {"Hero": 0, "Villain": 0, "Neutral": 0}

    #Count character alignments
    for item in items.values():
        if item.alignment in counts:
            counts[item.alignment] += 1

    plt.figure(figsize=(6, 6))
    plt.pie(
        list(counts.values()),  #convert dict_values to list
        labels=list(counts.keys()),  #convert dict_keys to list
        autopct="%1.1f%%",
        colors=["#4CAF50", "#F44336", "#FFC107"]
    )
    plt.title("Hero vs Villain vs Neutral Distribution")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/hero_vs_villain_pie.png")
    plt.close()


#Create bar chart showing average rating by quirk/tag
def quirk_popularity_bar(items, users):
    import pandas as pd

    quirk_ratings = {}

    #Collect ratings per quirk tag
    for item in items.values():
        for tag in item.tags:
            if tag not in quirk_ratings:
                quirk_ratings[tag] = []
            for user in users.values():
                if item.item_id in user.ratings:
                    quirk_ratings[tag].append(user.ratings[item.item_id])

    #Average ratings per quirk
    avg_quirk_ratings = {
        k: sum(v) / len(v) if v else 0
        for k, v in quirk_ratings.items()
    }

    df = pd.Series(avg_quirk_ratings).sort_values(ascending=False)

    plt.figure(figsize=(12, 6))
    df.plot(kind="bar")
    plt.title("Average Ratings by Quirk")
    plt.ylabel("Average Rating")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/quirk_popularity.png")
    plt.close()
