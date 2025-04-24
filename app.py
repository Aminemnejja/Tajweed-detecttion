import streamlit as st
from roboflow import Roboflow
import os
from PIL import Image

# Configuration de la page
st.set_page_config(page_title="Détection de Tajweed", layout="centered", page_icon="📖")

# Titre avec du style personnalisé
st.markdown(
    """
    <style>
    .title {
        font-size: 40px;
        color: #4CAF50;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    .subheader {
        font-size: 24px;
        color: #00796B;
        margin-top: 20px;
    }
    .option-radio {
        background-color: #F1F8E9;
        border: 1px solid #C8E6C9;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    }
    .option-radio:hover {
        background-color: #C8E6C9;
    }
    .info-box {
        border: 1px solid #A5D6A7;
        background-color: #E8F5E9;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .image-uploaded {
        border: 2px solid #81C784;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# Titre de l'application
st.markdown('<div class="title">📖 Détection des règles de Tajweed via une image</div>', unsafe_allow_html=True)
st.markdown("Uploade une image d'une page du Coran pour détecter les lettres ou règles de Tajweed.")

# Dictionnaire des informations de Tajweed
tajweed_info = {
    "h_00_nun_sukun": ("نْ (نون ساكنة)", "قاعدة متعلقة: إدغام، إخفاء، إقلاب أو إظهار."),
    "h_00_tanwin": ("ً ٍ ٌ (تنوين)", "قاعدة مشابهة للنون الساكنة – تؤثر على النطق."),
    "h_01_alif": ("ا (ألف)", "حرف مد."),
    "h_02_ba": ("ب (باء)", ""),
    "h_03_ta": ("ت (تاء)", ""),
    "h_04_tsa": ("ث (ثاء)", ""),
    "h_05_jim": ("ج (جيم)", ""),
    "h_06_kha": ("ح (حاء)", ""),
    "h_07_kho": ("خ (خاء)", ""),
    "h_08_dal": ("د (دال)", ""),
    "h_09_dzal": ("ذ (ذال)", ""),
    "h_10_ra": ("ر (راء)", "قد تكون من الحروف الشمسية أو تخضع للتفخيم أو القلقلة."),
    "h_11_za": ("ز (زاي)", ""),
    "h_12_sin": ("س (سين)", ""),
    "h_13_shin": ("ش (شين)", ""),
    "h_14_sad": ("ص (صاد)", ""),
    "h_15_dad": ("ض (ضاد)", ""),
    "h_16_to": ("ط (طاء مفخمة)", ""),
    "h_17_dzo": ("ظ (ظاء مفخمة)", ""),
    "h_18_ain": ("ع (عين)", ""),
    "h_19_ghain": ("غ (غين)", ""),
    "h_20_fa": ("ف (فاء)", ""),
    "h_21_qaf": ("ق (قاف)", "حرف قلقلة."),
    "h_22_kaf": ("ك (كاف)", ""),
    "h_23_lam": ("ل (لام)", "حرف شمسي أو قمري (لام شمسية أو لام قمرية)."),
    "h_24_mim": ("م (ميم)", "قد تدخل في الإخفاء أو الإدغام الشفوي."),
    "h_25_nun": ("ن (نون)", "تخضع لأحكام إذا كانت ساكنة."),
    "h_26_waw": ("و (واو)", "حرف مد."),
    "h_27_ha": ("ه (هاء)", ""),
    "h_28_ya": ("ي (ياء)", "حرف مد.")
}

# Ajout des options interactives
st.markdown("<div class='subheader'>✨ Souhaites-tu ajouter plus de fonctionnalités ?</div>", unsafe_allow_html=True)

option = st.radio(
    "Choisis une option à explorer 👇",
    (
        "🔈 Ajouter des sons audio de chaque lettre",
        "🎨 Appliquer une coloration spécifique par règle de Tajweed",
        "📄 Exporter un rapport d’analyse en PDF",
        "❌ Aucune pour l’instant"
    ),
    label_visibility="collapsed"
)

# Application de l'option sélectionnée
if option == "🔈 Ajouter des sons audio de chaque lettre":
    st.info("👉 Fonctionnalité à venir : lecture audio pour chaque lettre détectée.")
elif option == "🎨 Appliquer une coloration spécifique par règle de Tajweed":
    st.info("👉 Fonctionnalité à venir : surlignage coloré selon la règle (Ikhfa, Idgham, etc.).")
elif option == "📄 Exporter un rapport d’analyse en PDF":
    st.info("👉 Fonctionnalité à venir : export du résultat en format PDF avec image annotée.")

# Uploader une image
uploaded_image = st.file_uploader("📷 Choisir une image", type=["jpg", "jpeg", "png"])

if uploaded_image:
    # Sauvegarder l'image temporairement
    os.makedirs("uploads", exist_ok=True)
    image_path = os.path.join("uploads", uploaded_image.name)
    with open(image_path, "wb") as f:
        f.write(uploaded_image.getbuffer())

    # Afficher l'image téléchargée avec un cadre élégant
    st.image(image_path, caption="📸 Image uploadée", use_container_width=True, width=600)

    # Traitement via Roboflow
    with st.spinner("🔍 Analyse de l'image avec Roboflow..."):
        rf = Roboflow(api_key="vVD7jW73BEVjWpLX7Wgx")
        project = rf.workspace().project("test3_tajweed-detection-test-separate-letter-sfybm")
        model = project.version(1).model
        prediction = model.predict(image_path).json()

    st.success("✅ Analyse terminée !")
    st.subheader("📌 Objets détectés :")

    predictions = prediction.get("predictions", [])
    if predictions:
        for pred in predictions:
            label = pred["class"]
            conf = pred["confidence"]
            name, rule = tajweed_info.get(label, ("Lettre inconnue", "Pas de règle spécifique."))

            st.markdown(f"""
            <div class="info-box">
                <strong>🔠 Lettre détectée :</strong> {name} <br>
                <strong>📈 Confiance :</strong> {conf:.2f} <br>
                <strong>📘 Règle de Tajweed :</strong> {rule or "Aucune règle spécifique."}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Aucune règle ou lettre n’a été détectée.")

    # Option : Afficher l'image avec les annotations
    st.subheader("🖼️ Image avec annotations")
    pred_img_path = os.path.join("uploads", f"pred_{uploaded_image.name}")
    model.predict(image_path).save(pred_img_path)
    st.image(pred_img_path, use_container_width=True)

else:
    st.info("Veuillez uploader une image pour démarrer.")
