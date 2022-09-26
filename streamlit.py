import streamlit as st
import pandas as pd
import numpy as np
# import scipy as sp
import chart_studio.plotly as py
import plotly.figure_factory as ff
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title('MSBA 352 Assignment')

DATE_COLUMN = 'date/time'
# DATA_URL = ('C:\Users\eslam\OneDrive\Desktop\MSBA\MSBA325\sales.py')

@st.cache
def load_data(nrows):
    data = pd.read_csv(r'C:\Users\eslam\OneDrive\Desktop\MSBA\MSBA325\sales.csv', encoding= 'unicode_escape', nrows=nrows , )
    # lowercase = lambda x: str(x).lower()
    # data.rename(lowercase, axis='columns', inplace=True)
    # data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

st.text('This data is about sales of a company which shows the id of products, quantity sold, prices, sales, county from where people are purchasing and we will analyze the given data to see how the company is doing.')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


st.subheader("Data Visualization 1")
st.text('This visualization show the different products in the company and the amount of sales for each product over three years and the animations show how the sales of the product are changeing over time')

df = pd.read_csv("sales.csv", encoding= 'unicode_escape')
fig = px.bar(df, x="Products", y="Sales", color="Products",
  animation_frame="YEAR_ID", animation_group="Products", range_y=[0,10000])
st.plotly_chart(fig, use_container_width=True)

st.subheader("Data Visualization 2")
st.text('This visualization show the different countries where customers are purchasing products from and the amount of sales we have from each country')

data = [go.Bar(x=df.COUNTRY,
            y=df.Sales)]
st.plotly_chart(data, filename='jupyter-basic_bar')

st.subheader("Data Visualization 3")
st.text('This visualization is similar to the previous one but with a pie chart to show the presentage of sales we have from each country')

# df = pd.read_csv("sales.csv", encoding= 'unicode_escape')
df.loc[df['Sales'] < 2.e6, 'COUNTRU'] = 'Other countries' # Represent only large countries
fig = px.pie(df, values='Sales', names='COUNTRY', title='Sales per country')
st.plotly_chart(fig, use_container_width=True)

st.subheader("Data Visualization 4")
st.text('This visualization show the total sales for the three years and as you can see, the company was doing well in 2003, and the sales increased in 2004 by around 1.5M but in 2005, it decreased rapidly and it is much lower than 2003')

# df = pd.read_csv("sales.csv", encoding= 'unicode_escape')
# df['category'] = [str(i) for i in df.index]
color_discrete_sequence = ['#ec7c34']*len(df)
color_discrete_sequence[5] = '#609cd4'
fig = px.bar(df, x="YEAR_ID", y="Sales", color = 'YEAR_ID',
           color_discrete_sequence=color_discrete_sequence,
           )
st.plotly_chart(fig, use_container_width=True)

st.subheader("Data Visualization 5")
st.text('This visualization show the total sales of each product while coloring the bars based on the country')

fig = px.bar(df, x="Products", y="Sales", color="COUNTRY", title="Sales of products per country")
st.plotly_chart(fig, use_container_width=True)

