from . import collaborative, content_based

#Generate recommendations using a hybrid approach
def recommend(user, users, items, alpha=0.6, top_n=5):
    #Get collaborative filtering scores for all candidate items
    collab_scores = dict(collaborative.recommend(user, users, top_n=None))

    #Get content-based filtering scores (already normalized 0-1)
    content_scores = dict(content_based.recommend(user, items, top_n=None))

    combined_scores = {}

    #Create a unified set of item IDs from both methods
    all_item_ids = set(collab_scores.keys()) | set(content_scores.keys())

    #Combine scores using weighted average
    for item_id in all_item_ids:
        c_score = collab_scores.get(item_id, 0)
        cb_score = content_scores.get(item_id, 0)

        #Alpha controls balance between collaborative and content-based signals
        combined_scores[item_id] = alpha * c_score + (1 - alpha) * cb_score

    #Rank items by highest combined score
    ranked = sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)
    return ranked[:top_n]
