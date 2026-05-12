import streamlit as st
import time
#filiere = st.selectbox("filiere", ["Dev Digital", "Infra", "Data"])

#age = st.slider("votre ge", min_value=16, max_value=60, value=20)

#accepte = st.checkbox("J'accepte les conditions")
#if accepte : 
 #   st.write("Merci !")

#choix = st.radio("Genre", ["Homme", "Femme", "Autre"])

#date = st.date_input("Date de naissance")

#if st.button("calculer"):
 #   with st.spinner("calculer en cours..."):
  #      time.sleep(2)
 #       st.success("chargement réussi!")


col1, col2, col3 = st.columns(3)

with col1:
    st.title("calculateur")

    a = st.number_input("Nombre A", value=0.0)
    b = st.number_input("Nombre B", value=0.0)
    operation = st.selectbox("Operation", ["+", "-", "*", "/"])

    if st.button("calculer"):
        if operation == "+": resultat = a + b
        elif operation == "-": resultat = a - b
        elif operation == "*": resultat = a * b
        elif operation == "/": resultat = a / b
        else:
            st.error("Division par Zero !")
            resultat = None
        if resultat is not None:
            st.metric("Resultat", f"{resultat:.2f}")
with col2:
    st.title("column2")
with col3:
    st.title("column3")

st.sidebar.title("Menu")
choix = st.sidebar.selectbox("Page", ["Acceuil", "Notes"])
nom = st.sidebar.text_input("Votre nom")

if choix == "Acceuil":
    st.title("Page d'acceuil")
    st.write("bienvenue dans la page d'acceuil")
elif choix == "Notes":
    st.title("Page des notes")