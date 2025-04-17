import streamlit as st
import pandas as pd
from PIL import Image
import os

# Simulate predictions for demonstration
def load_predictions():
    data = {
        'Player': ['Aaron Judge', 'Shohei Ohtani', 'Mookie Betts'],
        'Team': ['Yankees', 'Dodgers', 'Dodgers'],
        'HR Probability': [0.27, 0.25, 0.22],
        'Ballpark': ['Yankee Stadium', 'Dodger Stadium', 'Dodger Stadium'],
        'Weather': ['72°F, Wind Out 8mph', '75°F, Neutral', '75°F, Neutral'],
        'Logo': ['logos/yankees.png', 'logos/dodgers.png', 'logos/dodgers.png']
    }
    return pd.DataFrame(data)

# Set up the Streamlit app
st.set_page_config(page_title="MLB HR Prop Bot", layout="wide")
st.title("💣 MLB AI Home Run Prop Bot")
st.caption("Live projections based on lineup, matchup, weather, and ballpark")

# Load predictions
df = load_predictions()

# Search and filter
search_term = st.text_input("Search Player or Team")
filtered_df = df[df['Player'].str.contains(search_term, case=False) | df['Team'].str.contains(search_term, case=False)]

# Display with logos
st.subheader("📊 Top HR Projections")
for i, row in filtered_df.iterrows():
    cols = st.columns([1, 3, 2, 2, 2])
    with cols[0]:
        if os.path.exists(row['Logo']):
            st.image(Image.open(row['Logo']), width=50)
    with cols[1]:
        st.markdown(f"**{row['Player']}**")
        st.caption(row['Team'])
    with cols[2]:
        st.metric("HR %", f"{row['HR Probability']*100:.1f}%")
    with cols[3]:
        st.text(row['Ballpark'])
    with cols[4]:
        st.text(row['Weather'])

# Refresh button
if st.button("🔄 Refresh"):
    st.experimental_rerun()
