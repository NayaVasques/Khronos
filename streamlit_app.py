import streamlit as st
import pandas as pd
import os
import gspread
from google.oauth2.service_account import Credentials

# connect to Google Sheets
def connect_to_gsheets():
    credentials = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=[
            "https://www.googleapis.com/auth/spreadsheets",
        ],
    )
    client = gspread.authorize(credentials)
    sheet = client.open_by_key("1Jwzm9Ce9_BMUrPeYrQZemlQ3lGJf0NEd0M8EXJU4NHM").sheet1 
    return sheet

# function to add row
def append_data_to_sheet(sheet, data):
    sheet.append_row(data)

# translate
def translate(language, en_text, fr_text):
    if language == 'English':
        return en_text
    else:
        return fr_text

# title
st.title('CHRONOS')

# language 
language = st.selectbox('Choose your language / Choisissez votre langue', ['English', 'Français'])

# name
name = st.text_input(translate(language, "Your Name", "Votre Nom"))

# student number
studentNumber = st.text_input(translate(language, "Your Student Number", "Votre No étudiant"))

# availability
st.subheader(translate(language, "Select your Availability", "Sélectionnez votre Disponibilité"))
st.write('Please select all available days and times / Veuillez sélectionner tous les jours et heures disponibles')

monday = st.multiselect(translate(language, 'Monday', 'Lundi'),
                        ['08:00-09:00', '09:00-10:00', '10:00-11:00', '11:00-12:00', '12:00-13:00', '13:00-14:00', '14:00-15:00', '15:00-16:00', '16:00-17:00'])
tuesday = st.multiselect(translate(language, 'Tuesday', 'Mardi'),
                        ['08:00-09:00', '09:00-10:00', '10:00-11:00', '11:00-12:00', '12:00-13:00', '13:00-14:00', '14:00-15:00', '15:00-16:00', '16:00-17:00'])
wednesday = st.multiselect(translate(language, 'Wednesday', 'Mercredi'),
                        ['08:00-09:00', '09:00-10:00', '10:00-11:00', '11:00-12:00', '12:00-13:00', '13:00-14:00', '14:00-15:00', '15:00-16:00', '16:00-17:00'])
thursday = st.multiselect(translate(language, 'Thursday', 'Jeudi'),
                        ['08:00-09:00', '09:00-10:00', '10:00-11:00', '11:00-12:00', '12:00-13:00', '13:00-14:00', '14:00-15:00', '15:00-16:00', '16:00-17:00'])
friday = st.multiselect(translate(language, 'Friday', 'Vendredi'),
                        ['08:00-09:00', '09:00-10:00', '10:00-11:00', '11:00-12:00', '12:00-13:00', '13:00-14:00', '14:00-15:00', '15:00-16:00', '16:00-17:00'])

# check the infos
if st.button(translate(language, 'Submit Availability', 'Envoyer la Disponibilité')):
    if not name or not studentNumber:
        st.error(translate(language, "Please provide your Name and Student Number.", "Veuillez fournir votre Nom et Numéro d'étudiant."))
    else:
        try:
            sheet = connect_to_gsheets()
            data = [name, studentNumber, ', '.join(monday), ', '.join(tuesday), ', '.join(wednesday), ', '.join(thursday), ', '.join(friday)]
            sheet.append_row(data)
            st.success(translate(language, 'Availability submitted!', 'Disponibilité envoyée!'))
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
