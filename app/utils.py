import pandas as pd
from app.models import User, Item


#Load users from CSV and create User objects
def load_users(path="data/users.csv"):
    df = pd.read_csv(path)
    users = {}

    #Create a User instance for each row
    for _, row in df.iterrows():
        users[int(row.user_id)] = User(int(row.user_id), row.username)

    return users


#Load items from CSV and create Item objects
def load_items(path="data/items.csv"):
    df = pd.read_csv(path)
    items = {}

    for _, row in df.iterrows():
        #Split tag string into list
        tags = row["tags"].split("|") if pd.notna(row["tags"]) else []

        #Create Item instance with metadata
        items[int(row["item_id"])] = Item(
            int(row["item_id"]),
            row["item_name"],
            row["alignment"],
            tags
        )

    return items


#Load ratings and attach them to existing User objects
def load_ratings(users, path="data/ratings.csv"):
    """Load ratings from CSV and add them to User objects as Python int/float"""
    import pandas as pd

    df = pd.read_csv(path)
    for _, row in df.iterrows():
        user_id = int(row.user_id)
        item_id = int(row.item_id)
        rating = float(row.rating)  # <-- convert to Python float
        #optionally, if you want integers only: rating = int(row.rating)
        user = users[user_id]
        user.add_rating(item_id, rating)
