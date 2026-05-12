import streamlit as st

# Titre de l'application
st.title("Formulaire Étudiant")

# Champs du formulaire
with st.form("form_etudiant"):
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    age = st.number_input("Âge", min_value=16, max_value=100, step=1)
    email = st.text_input("Email")
    filiere = st.selectbox("Filière", ["Informatique", "Mathématiques", "Physique", "Biologie", "Économie"])
    niveau = st.radio("Niveau", ["Licence", "Master", "Doctorat"])
    motivation = st.text_area("Pourquoi avez-vous choisi cette filière ?")

    # Bouton de soumission
    submitted = st.form_submit_button("Soumettre")

# Affichage des résultats
if submitted:
    st.success("Formulaire soumis avec succès !")
    st.write("### Informations recueillies :")
    st.write(f"👤 Nom : {nom} {prenom}")
    st.write(f"🎂 Âge : {age}")
    st.write(f"📧 Email : {email}")
    st.write(f"📚 Filière : {filiere}")
    st.write(f"🎓 Niveau : {niveau}")
    st.write(f"💡 Motivation : {motivation}")
