import cv2
import numpy as np
from PIL import Image
import easyocr
import requests
from bs4 import BeautifulSoup
import re
from tensorflow.keras.models import load_model

# ---------------- LOAD MODEL ----------------
model = load_model("model.h5")

# ---------------- OCR ----------------
reader = easyocr.Reader(['en'])

# ---------------- CNN PREDICTION ----------------
def predict_certificate(image):
    img = image.resize((224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)[0][0]

    if pred > 0.5:
        return "Fake", float(pred)
    else:
        return "Real", float(1 - pred)

# ---------------- OCR TEXT ----------------
def extract_text(image):
    result = reader.readtext(np.array(image))
    text = " ".join([res[1] for res in result])
    return text

# ---------------- EXTRACT URL ----------------
def extract_url(text):
    urls = re.findall(r'https?://\S+', text)
    return urls[0] if urls else None

# ---------------- GET WEBSITE TEXT ----------------
def get_name_from_link(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=5)

        soup = BeautifulSoup(response.text, "html.parser")

        # Get full visible text
        page_text = soup.get_text(separator=" ").lower()

        return page_text

    except:
        return None

# ---------------- EXTRACT NAME FROM OCR ----------------
def extract_name_from_text(text):
    text = text.lower()

    # Try to find name after common phrases
    patterns = [
        r"this certifies that ([a-z ]+)",
        r"presented to ([a-z ]+)",
        r"awarded to ([a-z ]+)",
        r"certified to ([a-z ]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1).strip()

    # fallback: return first 3 words
    words = text.split()
    return " ".join(words[:3])

# ---------------- NAME COMPARISON ----------------
def compare_names(ocr_text, website_text):
    if not website_text:
        return "Unknown"

    name = extract_name_from_text(ocr_text)

    ocr_words = set(name.split())
    web_words = set(website_text.split())

    common = ocr_words.intersection(web_words)

    if len(common) >= 2:
        return "Match"
    else:
        return "Mismatch"

# ---------------- TAMPERING DETECTION ----------------
def detect_tampering(image):
    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # blur + edges
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    output = img.copy()

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 800:  # filter noise
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(output, (x, y), (x+w, y+h), (0, 0, 255), 2)

    return output
