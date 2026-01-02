#Represents a user in the recommendation system
class User:
    def __init__(self, user_id, username):
        #Unique identifier for the user
        self.user_id = user_id

        #Display name for the user
        self.username = username

        #Dictionary mapping item_id to rating value
        self.ratings = {}

    #Add or update a rating for an item
    def add_rating(self, item_id, rating):
        self.ratings[item_id] = rating


#Represents an item (character) that can be recommended
class Item:
    def __init__(self, item_id, name, alignment="", tags=None):
        #Unique identifier for the item
        self.item_id = item_id

        #Name of the character
        self.name = name

        #Alignment classification (Hero, Villain, Neutral)
        self.alignment = alignment

        #List of descriptive tags used for content-based filtering
        self.tags = tags or []


#Represents a single user-item rating record
class Rating:
    def __init__(self, user_id, item_id, rating):
        #ID of the user who submitted the rating
        self.user_id = user_id

        #ID of the item being rated
        self.item_id = item_id

        #Numeric rating value (e.g., 1–5)
        self.rating = rating
