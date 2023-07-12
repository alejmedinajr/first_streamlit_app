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
sl.dataframe(fruits)
