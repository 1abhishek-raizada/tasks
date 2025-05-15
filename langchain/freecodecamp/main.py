import langchain_helper as lch
import streamlit as st


st.title("Pet Name Generator")

animal_type=st.sidebar.selectbox("What is your pet?",("Cat","Dog","Cow","Hamster"))

if animal_type=="Cat":
    pet_color=st.sidebar.text_area("what color is your Cat?", max_chars=15)
if animal_type=="Dog":
    pet_color=st.sidebar.text_area("what color is your Dog?", max_chars=15)
if animal_type=="Cow":
    pet_color=st.sidebar.text_area("what color is your Cow?", max_chars=15)
if animal_type=="Hamster":
    pet_color=st.sidebar .text_area("what color is your Hamster?", max_chars=15)    
    