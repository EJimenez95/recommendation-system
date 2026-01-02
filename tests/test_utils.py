import unittest
from app.utils import load_users, load_items, load_ratings

class TestUtils(unittest.TestCase):

    def setUp(self):
        #Load users from CSV
        self.users = load_users()
        #Load items from CSV
        self.items = load_items()
        #Load ratings and assign to users
        load_ratings(self.users)

    def test_load_users(self):
        #Check that users were loaded
        self.assertTrue(len(self.users) > 0, "Users should be loaded")
        #Verify each user has a username and a ratings dictionary
        for user_id, user in self.users.items():
            self.assertIsNotNone(user.username)
            self.assertIsInstance(user.ratings, dict)

    def test_load_items(self):
        #Check that items were loaded
        self.assertTrue(len(self.items) > 0, "Items should be loaded")
        #Verify each item has a name, valid alignment, and a list of tags
        for item_id, item in self.items.items():
            self.assertIsNotNone(item.name)
            self.assertIn(item.alignment, ["Hero", "Villain", "Neutral"])
            self.assertIsInstance(item.tags, list)

    def test_load_ratings(self):
        #Verify that each user's ratings are numeric values
        for user in self.users.values():
            for item_id, rating in user.ratings.items():
                self.assertIsInstance(rating, (int, float))

if __name__ == "__main__":
    #Run all unit tests in this file
    unittest.main()
