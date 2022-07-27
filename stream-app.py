import streamlit as st
import pandas as pd
 
 # Create Session object
class StreamlitSession:
 
 st.header('Create Roles')
 with st.form("Create Role form"):
   current_role = st.text_input('Enter current Role')
   role_name = st.text_input('Enter new Role Name')
   comment = st.text_input('Enter Comment')
   env = st.text_input('Enter Env')
   
   submitted = st.form_submit_button("Create")
 if(submitted):
    print("Role = ",current_role,"New Role = ", role_name , "comment = ",comment, "env = ", env)