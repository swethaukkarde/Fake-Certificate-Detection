import streamlit as st
import numpy as np
from PIL import Image
import cv2
from tensorflow.keras.models import load_model

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Fake Certificate Detector", layout="wide")

# ------------------ CUSTOM CSS ------------------
st.markdown("""
    <style>
    body {
        background: linear-gradient(120deg, #1f1c2c, #928dab);
        color: white;
    }
    .title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        color: #ffffff;
    }
    .subtext {
        text-align: center;
        font-size: 18px;
        color: #dcdcdc;
    }
    .box {
        background: rgba(255,255,255,0.05);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 0px 15px rgba(0,0,0,0.3);
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown('<div class="title">🔍 Fake Certificate Detection</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">Upload a certificate and detect tampering using AI</div>', unsafe_allow_html=True)

st.write("")

# ------------------ LOAD MODEL ------------------
@st.cache_resource
def load_my_model():
    return load_model("model.h5")

model = load_my_model()

# ------------------ PREDICTION FUNCTION ------------------
def predict(image):
    img = image.resize((224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)

    if pred[0][0] > 0.5:
        return "Fake", pred[0][0]
    else:
        return "Real", 1 - pred[0][0]

# ------------------ TAMPER DETECTION ------------------
def detect_tampered_region(image):
    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Edge detection
    edges = cv2.Canny(gray, 50, 150)

    # Convert edges to color heatmap
    heatmap = cv2.applyColorMap(edges, cv2.COLORMAP_JET)

    return heatmap

# ------------------ MAIN LAYOUT ------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.subheader("📤 Upload Certificate")

    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Certificate", use_column_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.subheader("🧠 Detection Result")

    if uploaded_file:
        image = Image.open(uploaded_file)

        if st.button("🚀 Detect Now"):
            with st.spinner("Analyzing Certificate..."):
                result, confidence = predict(image)

                if result == "Fake":
                    st.error(f"❌ Result: {result}")
                else:
                    st.success(f"✅ Result: {result}")

                st.write(f"Confidence: {confidence*100:.2f}%")

                # Tampered region
                st.subheader("📍 Tampered Region")
                tampered = detect_tampered_region(image)
                st.image(tampered, caption="Highlighted Tampered Area", use_column_width=True)

    else:
        st.info("Upload an image to start detection")

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ FOOTER ------------------
st.write("")
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
