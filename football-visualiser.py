import streamlit as st
import pandas as pd
import altair as alt

# Load the data from a CSV file
data = pd.read_csv('fifa_world_cup_data.csv')

# Create a table with the desired columns
table = data[['Year', 'Winner', 'Host', 'Highest Goal Scorer']]

# Set the table headers
table.columns = ['Year', 'Winner', 'Host', 'Highest Goal Scorer']

# Home Page
st.set_page_config(page_title='FIFA World Cup Visualizer', page_icon=':soccer:', layout='wide')
st.title('FIFA World Cup Visualizer')
st.write('Welcome to the FIFA World Cup Visualizer! This app provides an interactive way to explore World Cup data. Use the sidebar to select different visualizations.')
st.write('🌎🏆🥇🥅')

# Sidebar
st.sidebar.title('Visualizations')
options = ['World Cup Winners', 'Wins by Country', 'Highest Goal Scorer by Year']
choice = st.sidebar.selectbox('Select a visualization', options)


# Display the selected visualization
if choice == 'World Cup Winners':
    st.header('🏆 FIFA World Cup Winners 🏆')
    st.write('This table shows the winners of the FIFA World Cup, along with the host country, highest goal scorer, and the year in which the tournament was held.')
    st.table(table)
elif choice == 'Wins by Country':
    # Create a bar chart showing the number of times each country has won the World Cup
    winners = data['Winner'].value_counts().rename_axis('country').reset_index(name='num_wins')
    chart1 = alt.Chart(winners).mark_bar().encode(
        x='country:N',
        y='num_wins:Q'
    )
    chart1.properties(title='Number of World Cup wins by country')
    st.header('🏆 Number of World Cup wins by country 🌎')
    st.write('This bar chart shows the number of times each country has won the FIFA World Cup.')
    st.altair_chart(chart1, use_container_width=True)
elif choice == 'Wins by Host':
    # Create a pie chart showing the number of times each country has hosted the World Cup
    hosts = data['Host'].value_counts().rename_axis('host').reset_index(name='num_hosts')
    chart2 = alt.Chart(hosts).mark_arc().encode(
        theta='num_hosts:Q',
        color=alt.Color('host:N', legend=None),
        tooltip=['host', 'num_hosts']
    ).properties(
        width=400,
        height=400,
        title='Number of World Cup hosts by country'
    )
    chart2.title = 'Number of World Cup hosts by country'
    st.header('🌎 Number of World Cup hosts by country 🏆')
    st.write('This pie chart shows the number of times each country has hosted the FIFA World Cup.')
    st.altair_chart(chart2, use_container_width=True)
elif choice == 'Highest Goal Scorer by Year':
    # Create a 3D scatter chart showing the relationship between highest goal scorer and year
    scatter_data = data[['Year', 'Highest Goal Scorer']]
    scatter_data.columns = ['Year', 'Highest Goal Scorer']
    chart3 = alt.Chart(scatter_data).mark_circle().encode(
        x='Year:N',
        y='Highest Goal Scorer:N',
        size=alt.Size('count():Q', legend=None),
        color=alt.Color('Year:N', legend=None),
        tooltip=['Year', 'Highest Goal Scorer', 'count()']
    ).properties(
        width=600,
        height=400,
        title='Highest goal scorer by year'
    )
    chart3.title = 'Highest Goal Scorer by Year'
    st.header('🥅 Highest goal scorer by year 📅')
    st.write('This 3D scatter chart shows the relationship between the highest goal scorer and the year in which the tournament was held.')
    st.altair_chart(chart3, use_container_width=True)
