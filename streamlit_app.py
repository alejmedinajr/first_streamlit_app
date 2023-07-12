import streamlit as sl
import pandas as pd

sl.title('My Parents New Healthy Diner') # title
sl.header('Breakfast Menu') # header

sl.text('🥣 Omega 3 & Blueberry Oatmeal')
sl.text('🥗 Kale, Spinach & Rocket Smoothie')
sl.text(' 🐔 Hard-Boiled Free-Range Egg')
sl.text('🥑🍞 Avocado Toast')

sl.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇') # smoothie header
 
fruits = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

fruit = fruit.set_index('Fruit') # so that the index of the fruit list makes sense when the readers read

# ability to pick a list so that user can pick the fruit that they want to include
sl.multiselect("Pick some fruits:", list(fruits.index))

sl.dataframe(fruits) # display the table on the page
