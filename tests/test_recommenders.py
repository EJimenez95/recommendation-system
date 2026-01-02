import unittest
from app.utils import load_users, load_items, load_ratings
from app.recommenders import collaborative, content_based, hybrid

class TestRecommenders(unittest.TestCase):

    def setUp(self):
        #Load users from CSV
        self.users = load_users()
        #Load items from CSV
        self.items = load_items()
        #Load ratings and assign to users
        load_ratings(self.users)
        #Select a sample user for testing
        self.user = self.users[1]

    def test_collaborative_recommend(self):
        #Generate collaborative filtering recommendations for the user
        recs = collaborative.recommend(self.user, self.users, top_n=5)
        #Check that exactly 5 recommendations are returned
        self.assertEqual(len(recs), 5)
        #Check that recommended item IDs exist in the items list
        for item_id, score in recs:
            self.assertIn(item_id, self.items)

    def test_content_based_recommend(self):
        #Generate content-based recommendations for the user
        recs = content_based.recommend(self.user, self.items, top_n=5)
        #Check that exactly 5 recommendations are returned
        self.assertEqual(len(recs), 5)
        #Check that the recommendation score is between 0 and 1
        for item_id, score in recs:
            self.assertTrue(0 <= score <= 1)

    def test_hybrid_recommend(self):
        #Generate hybrid recommendations combining collaborative and content-based
        recs = hybrid.recommend(self.user, self.users, self.items, alpha=0.6, top_n=5)
        #Check that exactly 5 recommendations are returned
        self.assertEqual(len(recs), 5)
        #Check that recommended item IDs exist in the items list
        for item_id, score in recs:
            self.assertIn(item_id, self.items)

if __name__ == "__main__":
    #Run all unit tests in this file
    unittest.main()
