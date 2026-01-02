import unittest
from app.models import User, Item, Rating

class TestModels(unittest.TestCase):

    def test_user_add_rating(self):
        #Create a User instance
        user = User(1, "TestUser")
        #Add a rating for item 101 with value 5
        user.add_rating(101, 5)
        #Check that the rating was stored correctly
        self.assertEqual(user.ratings[101], 5)

    def test_item_attributes(self):
        #Create an Item instance
        item = Item(101, "All Might", "Hero", ["Strong", "Symbol"])
        #Check that the name attribute is correct
        self.assertEqual(item.name, "All Might")
        #Check that the alignment attribute is correct
        self.assertEqual(item.alignment, "Hero")
        #Check that the tags include "Strong"
        self.assertIn("Strong", item.tags)

    def test_rating_class(self):
        #Create a Rating instance
        rating = Rating(1, 101, 5)
        #Check that user_id is correct
        self.assertEqual(rating.user_id, 1)
        #Check that item_id is correct
        self.assertEqual(rating.item_id, 101)
        #Check that rating value is correct
        self.assertEqual(rating.rating, 5)

if __name__ == "__main__":
    #Run all unit tests in this file
    unittest.main()
