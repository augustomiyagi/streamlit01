import streamlit as st
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# Ejemplo 1

chart_data = pd.DataFrame(
     np.random.randn(10, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
st.write(chart_data)
st.write('Hello, *World!* :sunglasses:')

# Ejemplo 2

st.write(12345)

# Ejemplo 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4, 5] ,
     'second column': [10, 20, 30, 40,50]
     })
st.write(df)

# Ejemplo 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Ejemplo 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
