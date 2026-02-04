import streamlit as st
import joblib
from pathlib import Path

# -----------------------
# Page config
# -----------------------
st.set_page_config(
    page_title="Nepali News Classifier",
    page_icon="📰",
    layout="centered"
)

st.title("📰 Nepali News Classifier")
st.write("Paste Nepali news text below and classify it.")

# -----------------------
# Load model
# -----------------------
BASE_DIR = Path(__file__).parent
MODEL_PATH = BASE_DIR / "/Users/susananiroula/Desktop/LAB1/assignment 2/nb_model.joblib"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

# -----------------------
# Inputs
# -----------------------
news_text = st.text_area(
    "Nepali News Text",
    height=220,
    placeholder="यहाँ नेपाली समाचार लेख्नुहोस्..."
)

# -----------------------
# Predict
# -----------------------
if st.button("🔍 Classify", type="primary", use_container_width=True):
    if not news_text.strip():
        st.warning("Please enter some text.")
    else:
        # Direct prediction (already a label)
        prediction = model.predict([news_text])[0]

        st.success(f"🧾 Category: **{prediction}**")