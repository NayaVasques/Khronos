import streamlit as st
import pandas as pd
import os

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
    # DataFrame 
    new_entry = pd.DataFrame({
        'Name': [name],
        'Student Number': [studentNumber],
        'Monday': [', '.join(monday)],
        'Tuesday': [', '.join(tuesday)],
        'Wednesday': [', '.join(wednesday)],
        'Thursday': [', '.join(thursday)],
        'Friday': [', '.join(friday)]
    })

    # csv file
    file_exists = os.path.isfile('availability_data.csv')

    # create or add info
    if file_exists:
        df = pd.read_csv('availability_data.csv')
        df = pd.concat([df, new_entry], ignore_index=True)
    else:
        df = new_entry

    # save file
    df.to_csv('availability_data.csv', index=False)

    st.success(translate(language, 'Availability submitted!', 'Disponibilité envoyée!'))


