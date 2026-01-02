import math

#Compute cosine similarity between two users based on shared ratings
def cosine_similarity(ratings1, ratings2):
    #Find items both users have rated
    common_items = set(ratings1.keys()) & set(ratings2.keys())
    if not common_items:
        return 0

    #Calculate dot product of ratings
    numerator = sum(ratings1[i] * ratings2[i] for i in common_items)

    #Calculate magnitude of each rating vector
    denom1 = math.sqrt(sum(ratings1[i] ** 2 for i in common_items))
    denom2 = math.sqrt(sum(ratings2[i] ** 2 for i in common_items))

    #Avoid division by zero
    if denom1 == 0 or denom2 == 0:
        return 0

    #Return cosine similarity score
    return numerator / (denom1 * denom2)


#Generate recommendations using user-based collaborative filtering
def recommend(user, all_users, top_n=5):
    scores = {}

    #Compare target user with every other user
    for other_user in all_users.values():
        if other_user.user_id == user.user_id:
            continue

        #Measure similarity between users
        similarity = cosine_similarity(user.ratings, other_user.ratings)

        #Weight other users' ratings by similarity
        for item_id, rating in other_user.ratings.items():
            #Only recommend items the user has not rated
            if item_id not in user.ratings:
                scores[item_id] = scores.get(item_id, 0) + similarity * rating

    #Rank items by highest weighted score
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return ranked[:top_n]
