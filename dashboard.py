
import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
df = pd.read_csv("cleaned_netflix.csv")

# Title
st.title("Netflix Dashboard")

# Sidebar Filters
genre = st.sidebar.selectbox(
    "Genre",
    ["All"] + sorted(list(df['listed_in'].dropna().unique()))
)

year = st.sidebar.slider(
    "Release Year",
    int(df['release_year'].min()),
    int(df['release_year'].max()),
    int(df['release_year'].max())
)

# KPIs
st.metric(
    "Total Titles",
    len(df)
)

st.metric(
    "Movies",
    len(df[df['type'] == "Movie"])
)

st.metric(
    "TV Shows",
    len(df[df['type'] == "TV Show"])
)

# Movies vs TV Shows
fig = px.pie(
    df,
    names='type',
    title='Movies vs TV Shows'
)

st.plotly_chart(fig)

# Content Growth
growth = (
    df.groupby('release_year')
      .size()
      .reset_index(name='count')
)

fig = px.line(
    growth,
    x='release_year',
    y='count',
    title='Content Growth'
)

st.plotly_chart(fig)

# Top Countries
top_country = (
    df['country']
      .value_counts()
      .head(10)
)

fig = px.bar(
    x=top_country.index,
    y=top_country.values,
    labels={'x':'Country','y':'Titles'},
    title='Top 10 Countries'
)

st.plotly_chart(fig)
