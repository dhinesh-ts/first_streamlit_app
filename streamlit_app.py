import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLERROR


streamlit.title('CRD Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')

streamlit.header('Build your own SMOOTHIEEE!!🥑🍞')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.

streamlit.dataframe(my_fruit_list)

streamlit.write('The user entered ', fruit_choice)

# defining a function 

def get_fruity_vice_data (this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return 


# streamlit.text(fruityvice_response)
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit from the above")
  else:
    back_from_function = get_fruity_vice_data(fruit_choice)
    streamlit.dataframe(fruityvice_normalized)
except URLERROR as e:
  streamlit.error()
  
streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
add_my_fruit = streamlit.text_input("select a fruit that you need to add ", '')
streamlit.write("Thanks for adding..", add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('from streamlit')") # select * from pc_rivery_db.public.fruit_load_list
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()

if streamlist.button("Get Fruit Load List"):
  my_cnx = snowflake.conector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()               
  streamnlit.dataframe(my_data_rows)
  streamlit.text(my_data_row)
