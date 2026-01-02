import streamlit as st
from app.utils import load_users, load_items, load_ratings
from app.recommenders import collaborative, content_based, hybrid
from app.visualizations import popular_characters_bar


#Load users, items, and ratings from CSV files
users = load_users()
items = load_items()
load_ratings(users)


#Page title
st.title("My Hero Academia Recommendation System")


#Dropdown for selecting a user
usernames = [user.username for user in users.values()]
selected_username = st.selectbox("Select a user:", usernames)

#Find the selected User object
selected_user = next(user for user in users.values() if user.username == selected_username)


#Display recommendations
st.subheader("Recommendations")


#Collaborative filtering results
st.write("**Collaborative Filtering:**")
collab_recs = collaborative.recommend(selected_user, users, top_n=5)
for item_id, score in collab_recs:
    st.write(f"- {items[item_id].name} (score: {score:.2f})")


#Content-based filtering results
st.write("**Content-Based Filtering:**")
content_recs = content_based.recommend(selected_user, items, top_n=5)
for item_id, score in content_recs:
    st.write(f"- {items[item_id].name} (score: {score:.2f})")


#Hybrid filtering results
st.write("**Hybrid Filtering:**")
hybrid_recs = hybrid.recommend(selected_user, users, items, alpha=0.6, top_n=5)
for item_id, score in hybrid_recs:
    st.write(f"- {items[item_id].name} (score: {score:.2f})")


#Visual section
st.subheader("Visualizations")
st.write("Top characters by average rating:")


#Generate bar chart and display it
popular_characters_bar(items, users)
st.image("output/popular_characters.png")
