import streamlit as st
import pandas as pd
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets
def connect_to_gsheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("khronos.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("khronos").sheet1  # open file
    return sheet

# add line
def append_data_to_sheet(sheet, data):
    sheet.append_row(data)

# function to translate
def translate(language, en_text, fr_text):
    if language == 'English':
        return en_text
    else:
        return fr_text

# tittle
st.title('CHRONOS')

# choose the language
language = st.selectbox('Choose your language / Choisissez votre langue', ['English', 'Français'])

# user's name
name = st.text_input(translate(language, "Your Name", "Votre Nom"))

# study number
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

if st.button(translate(language, 'Submit Availability', 'Envoyer la Disponibilité')):
    # conect to Google Sheets
    sheet = connect_to_gsheets()

    # data for Google Sheets
    data = [name, studentNumber, ', '.join(monday), ', '.join(tuesday), ', '.join(wednesday), ', '.join(thursday), ', '.join(friday)]

    # add data to Google Sheets
    append_data_to_sheet(sheet, data)

    st.success(translate(language, 'Availability submitted!', 'Disponibilité envoyée!'))

    st.success(translate(language, 'Availability submitted!', 'Disponibilité envoyée!'))


