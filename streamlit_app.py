import streamlit as st
import pandas as pd
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Função para conectar ao Google Sheets usando variáveis de ambiente
def connect_to_gsheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    # Obter as variáveis de ambiente
    creds_dict = {
        "type": os.getenv("GOOGLE_SHEETS_TYPE"),
        "project_id": os.getenv("GOOGLE_SHEETS_PROJECT_ID"),
        "private_key_id": os.getenv("GOOGLE_SHEETS_PRIVATE_KEY_ID"),
        "private_key": os.getenv("GOOGLE_SHEETS_PRIVATE_KEY").replace('\\n', '\n'),
        "client_email": os.getenv("GOOGLE_SHEETS_CLIENT_EMAIL"),
        "client_id": os.getenv("GOOGLE_SHEETS_CLIENT_ID"),
        "auth_uri": os.getenv("GOOGLE_SHEETS_AUTH_URI"),
        "token_uri": os.getenv("GOOGLE_SHEETS_TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("GOOGLE_SHEETS_AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": os.getenv("GOOGLE_SHEETS_CLIENT_X509_CERT_URL")
    }
    
    # Autenticação e conexão com Google Sheets
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    sheet = client.open("khronos").sheet1  # Abre a planilha correta
    return sheet

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
