import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothe')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.text('Avacado Toast')
streamlit.header('Build your own fruit smoothe')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')




fruits_selected = streamlit.multiselect("Pick some fruit:", list(my_fruit_list.index),['Avacado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
                                   
streamlit.dataframe(my_fruit_list)











