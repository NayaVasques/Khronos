import streamlit as st
import pandas as pd
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests

def get_sheet_data():
    api_key = os.getenv("GOOGLE_API_KEY")
    sheet_id = "1Jwzm9Ce9_BMUrPeYrQZemlQ3lGJf0NEd0M8EXJU4NHM"
    range_name = "Sheet1!AA9999:EE9999"  

    url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/{range_name}?key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get("values", [])
    else:
        st.error(f"Erro ao acessar a API do Google Sheets: {response.status_code}")
        return None

# Pegar os dados da planilha
data = get_sheet_data()

# Exibir os dados na aplicação Streamlit
if data:
    st.write(data)


"""# connect to Google Sheets
def connect_to_gsheets():
    api_key = os.getenv("GOOGLE_API_KEY")
    client = gspread.Client(auth=api_key)
    client.session = gspread.httpsession.HTTPSession()
    sheet = client.open_by_key("1Jwzm9Ce9_BMUrPeYrQZemlQ3lGJf0NEd0M8EXJU4NHM").sheet1 
    return sheet

# Substitua 'YOUR_API_KEY' pela sua API Key
sheet = connect_to_gsheets()""" 

# Função para adicionar uma linha na planilha
def append_data_to_sheet(sheet, data):
    sheet.append_row(data)

# Função para traduzir
def translate(language, en_text, fr_text):
    if language == 'English':
        return en_text
    else:
        return fr_text

# Título da Aplicação
st.title('CHRONOS')

# Seleção de Idioma
language = st.selectbox('Choose your language / Choisissez votre langue', ['English', 'Français'])

# Nome do Usuário
name = st.text_input(translate(language, "Your Name", "Votre Nom"))

# Número do Estudante
studentNumber = st.text_input(translate(language, "Your Student Number", "Votre No étudiant"))

# Disponibilidade
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

# Verificação dos Campos Obrigatórios
if st.button(translate(language, 'Submit Availability', 'Envoyer la Disponibilité')):
    if not name or not studentNumber:
        st.error(translate(language, "Please provide your Name and Student Number.", "Veuillez fournir votre Nom et Numéro d'étudiant."))
    else:
        # Conectar ao Google Sheets
        sheet = connect_to_gsheets()

        # Dados para o Google Sheets
        data = [name, studentNumber, ', '.join(monday), ', '.join(tuesday), ', '.join(wednesday), ', '.join(thursday), ', '.join(friday)]

        # Adicionar os dados ao Google Sheets
        append_data_to_sheet(sheet, data)

        st.success(translate(language, 'Availability submitted!', 'Disponibilité envoyée!'))
