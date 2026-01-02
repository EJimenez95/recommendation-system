# Author: Eric Jimenez
# Project: Recommendation System
# Date: 12/19/25
# Purpose: Developed a recommendation system that predicts user preferences
# for My Hero Academia characters using collaborative, content-based, and hybrid filtering,
# with visualizations to analyze trends and ratings.

from utils import load_users, load_items, load_ratings
from recommenders import collaborative, content_based, hybrid
from visualizations import (
    ratings_heatmap,
    popular_characters_bar,
    hero_villain_pie,
    quirk_popularity_bar
)


def print_recommendations(user, users, items):
    #Print all recommendation types for a given user
    print(f"\nRecommendations for {user.username}:\n")

    #Collaborative filtering results
    collab_recs = collaborative.recommend(user, users, top_n=5)
    print("Collaborative Filtering:")
    for item_id, score in collab_recs:
        print(f"- {items[item_id].name} (score: {score:.2f})")

    #Content-based filtering results
    content_recs = content_based.recommend(user, items, top_n=5)
    print("\nContent-Based Filtering:")
    for item_id, score in content_recs:
        print(f"- {items[item_id].name} (score: {score:.2f})")

    #Hybrid filtering results
    hybrid_recs = hybrid.recommend(user, users, items, alpha=0.6, top_n=5)
    print("\nHybrid Filtering:")
    for item_id, score in hybrid_recs:
        print(f"- {items[item_id].name} (score: {score:.2f})")


def main():
    #Load users, items, and ratings
    users = load_users()
    items = load_items()
    load_ratings(users)

    #Display loaded data for verification
    print("=== Loaded Users and Ratings ===")
    for user in users.values():
        print(f"{user.username}: {user.ratings}")

    #Generate visualizations
    ratings_heatmap(users, items)
    popular_characters_bar(items, users)
    hero_villain_pie(items)
    quirk_popularity_bar(items, users)

    #Run recommendations for a sample user
    sample_user = users[1]
    print_recommendations(sample_user, users, items)


if __name__ == "__main__":
    main()
