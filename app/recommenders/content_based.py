#Measure similarity between two tag lists using Jaccard similarity
def jaccard_similarity(tags1, tags2):
    #Convert tag lists to sets for comparison
    set1, set2 = set(tags1), set(tags2)
    if not set1 or not set2:
        return 0

    #Return ratio of shared tags to total unique tags
    return len(set1 & set2) / len(set1 | set2)


#Generate recommendations using content-based filtering
def recommend(user, items, top_n=5):
    scores = {}

    #Evaluate every item in the catalog
    for item_id, item in items.items():
        #Skip items the user has already rated
        if item_id in user.ratings:
            continue

        score = 0

        #Compare item against all items the user has rated
        for rated_item_id, rating in user.ratings.items():
            rated_item = items[rated_item_id]

            #Calculate similarity based on shared tags
            similarity = jaccard_similarity(item.tags, rated_item.tags)

            #Weight similarity by the user's rating
            score += similarity * rating

        scores[item_id] = score

    #Normalize scores to a 0-1 range for fair comparison
    if scores:
        max_score = max(scores.values())
        min_score = min(scores.values())

        for item_id in scores:
            #Avoid division by zero if all scores are equal
            if max_score - min_score > 0:
                scores[item_id] = (scores[item_id] - min_score) / (max_score - min_score)
            else:
                scores[item_id] = 0.0

    #Rank items by highest normalized score
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return ranked[:top_n]
