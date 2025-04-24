import streamlit as st
from tajweed_model import analyze_tajweed_image
from utils import color_rule_map
import os

st.set_page_config(page_title="Détecteur de Tajweed", layout="centered")
st.title("📖 Détection des règles de Tajweed à partir d'une image")

st.markdown("Uploade une page du Coran en couleur pour détecter les règles de Tajweed utilisées.")

doc_image = st.file_uploader("📷 Choisir une image", type=["png", "jpg", "jpeg"])

if doc_image:
    os.makedirs("uploads", exist_ok=True)
    upload_path = os.path.join("uploads", doc_image.name)
    with open(upload_path, "wb") as f:
        f.write(doc_image.getbuffer())

    st.image(upload_path, caption="Image uploadée", use_column_width=True)

    with st.spinner("🔍 Analyse en cours..."):
        result = analyze_tajweed_image(upload_path)

    st.success("✅ Analyse terminée")
    st.subheader("📌 Règles détectées :")
    for rule, count in result.items():
        st.markdown(f"- **{rule}** : {count} occurrence(s)")

    if st.checkbox("📚 Afficher les correspondances Couleurs → Règles"):
        st.dataframe(color_rule_map)
else:
    st.info("Veuillez uploader une image de page du Coran.")
