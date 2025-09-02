import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- Page Setup ---
st.set_page_config(page_title="Year 1B Superstar Points", layout="wide")
st.title("🌟 Year 1B Superstar Points 🌟")

# --- Excel File ---
excel_file = "Year1B_Superstar_Final.xlsx"  # make sure this file is in same folder

# --- Load Data (no caching so it reloads each time) ---
def load_data():
    return pd.read_excel(excel_file)

df = load_data()

# --- Refresh Button ---
if st.button("🔄 Refresh Data"):
    df = load_data()
    st.success("Data refreshed from Excel!")

# --- Bar Chart ---
fig = go.Figure(data=[
    go.Bar(
        x=df['Student'],
        y=df['Points Today'],
        text=df['Emoji'],
        textposition='outside',
        marker=dict(color=[
            '#FF5733', '#33FF57', '#3357FF', '#FF33A1',
            '#9D33FF', '#33FFF6', '#FF9633', '#B6FF33',
            '#FF3333', '#3380FF', '#8E33FF', '#FFC133', '#6BFF33'
        ]),
        hovertemplate='<b>%{x}</b><br>Points: %{y} %{text}<extra></extra>'
    )
])

fig.update_layout(
    yaxis=dict(range=[0, 5], dtick=1, showgrid=False),
    plot_bgcolor="white",
    paper_bgcolor="white",
    height=600
)

st.plotly_chart(fig, use_container_width=True)

# --- Sounds ---
st.markdown("### 🎶 Sounds")
if st.button("Play Class Cheer 🎉"):
    st.audio("https://actions.google.com/sounds/v1/crowds/cheer.ogg")
