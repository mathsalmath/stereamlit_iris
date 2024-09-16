

import streamlit as  st
import pandas as pd
import plotly.express as px


df = px.data.iris()

st.header("This is Iris dataset")
st.subheader('First five rows of the dataframe')
st.write(df.head())

st.subheader('Last five rows of the dataframe')
st.write(df.tail())

st.subheader('Information of the dataframe')
st.write(df.info())
st.subheader('Statistical analysis of the dataframe')
st.write(df.describe())

st.subheader('Frequency of Each Species')
st.plotly_chart(px.histogram(df, x = 'species', color ='species', text_auto=True))

st.subheader('Scatter Plot Sepal Length and Sepal Width')
st.plotly_chart(px.scatter(df, x = 'sepal_length', y = 'sepal_width', color ='species'))

st.subheader('Box Plot Sepal Length and Species')
st.plotly_chart(px.box(df, y = 'sepal_length', x = 'species', color ='species'))

st.plotly_chart(px.histogram(df, x='species', y ='sepal_length', color='species'))

st.subheader('Sepal Length by Species')
st.plotly_chart(px.bar(df, x='species', y ='sepal_length', color='species', title = 'Sepal Length'))

st.subheader('Sepal Length by Species')
st.write('**Sepal Length**')
st.plotly_chart(px.pie(df, names = 'species', values = 'sepal_length', title= 'Sepal Length Percent'))

st.subheader('Sunburst Chart')
st.plotly_chart(px.sunburst(df, path=['species', 'sepal_width'], values= 'sepal_length'))

st.subheader('random samples from the dataset ')

st.write('Enter the number of samples.')

##input 

sample_number = st.number_input('Enter the number of samples.', min_value = 0, max_value = 11, step = 1)

if sample_number != 0:
    st.markdown(
        f"""
        * sample_size' : {sample_number}
        """
    )






