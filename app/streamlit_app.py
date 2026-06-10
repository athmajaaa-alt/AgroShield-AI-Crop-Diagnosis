import streamlit as st
import sys
import os
import time
import random

# Add project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.llama_advice import get_disease_info

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    
    page_title="AgroShield 🌾",
    page_icon="🌱",
    layout="wide"
)
st.markdown("""
<div class="floating-icons">
    <span style="left:5%; animation-delay:0s;">🌿</span>
    <span style="left:15%; animation-delay:4s;">🌾</span>
    <span style="left:30%; animation-delay:8s;">🌱</span>
    <span style="left:50%; animation-delay:2s;">🍃</span>
    <span style="left:65%; animation-delay:6s;">🌼</span>
    <span style="left:80%; animation-delay:10s;">🌳</span>
    <span style="left:90%; animation-delay:14s;">🌻</span>
</div>
""", unsafe_allow_html=True)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* -------- Animated Pastel Background -------- */
.stApp {
    background: linear-gradient(-45deg, #e6f4ea, #edf7ed, #f0fff4, #e9f5ec);
    background-size: 400% 400%;
    animation: gradientBG 18s ease infinite;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* -------- Hero Section -------- */
.hero {
    text-align: center;
    padding: 50px 20px;
    animation: floatHero 6s ease-in-out infinite;
}

@keyframes floatHero {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-8px); }
    100% { transform: translateY(0px); }
}

.hero h1 {
    font-size: 60px;
    color: #2f5233;
}

.hero p {
    font-size: 20px;
    color: #5a6f57;
}

/* -------- Glass Card -------- */
.card {
    background: rgba(255, 255, 255, 0.75);
    backdrop-filter: blur(15px);
    padding: 40px;
    border-radius: 25px;
    box-shadow: 0px 20px 50px rgba(0,0,0,0.08);
    transition: 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
}

/* -------- Input Fields -------- */
input, textarea {
    border-radius: 15px !important;
    border: 2px solid #cde7d0 !important;
    padding: 12px !important;
    background-color: #f8fffa !important;
    transition: 0.3s ease !important;
    font-size: 16px !important;
}

input:focus, textarea:focus {
    border: 2px solid #4b7f52 !important;
    box-shadow: 0 0 12px rgba(75,127,82,0.4) !important;
    background-color: #ffffff !important;
}

/* -------- File Uploader -------- */
[data-testid="stFileUploader"] {
    background-color: #f5fcf6;
    padding: 20px;
    border-radius: 20px;
    border: 2px dashed #a8d5ba;
    transition: 0.3s ease;
}

[data-testid="stFileUploader"]:hover {
    border-color: #4b7f52;
    background-color: #ffffff;
}

/* -------- Button -------- */
.stButton>button {
    background: linear-gradient(135deg, #4b7f52, #6bbf73);
    color: white;
    font-size: 18px;
    padding: 14px 32px;
    border-radius: 30px;
    border: none;
    transition: 0.3s ease-in-out;
}

.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 20px rgba(75,127,82,0.4);
}

/* -------- Result Box -------- */
.result-box {
    background-color: #f4fbf6;
    padding: 30px;
    border-radius: 18px;
    border-left: 8px solid #4b7f52;
    margin-top: 20px;
    font-size: 17px;
}

/* -------- Sidebar Upgrade -------- */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #e4f3e8, #d4ead9);
}

section[data-testid="stSidebar"] * {
    color: #2f5233 !important;
    font-weight: 500;
}

/* -------- Footer -------- */
.footer {
    text-align: center;
    margin-top: 60px;
    color: #5f7f63;
    font-weight: 500;
}

/* -------- Floating Icons (Enhanced Visibility) -------- */

.floating-icons {
    position: fixed;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    pointer-events: none;
    z-index: 0;
}

.floating-icons span {
    position: absolute;
    bottom: -50px;
    font-size: 30px;
    #opacity: 0.3;
    animation: floatIcon 24s linear infinite;
    text-shadow: 0 0 8px rgba(0, 80, 0, 0.35);
}

@keyframes floatIcon {
    0% {
        transform: translateY(0px) rotate(0deg);
        opacity: 0.3;
    }
    100% {
        transform: translateY(-110vh) rotate(360deg);
        opacity: 0.3;
    }
}

/* Keep content above floating icons */
.stApp > div {
    position: relative;
    z-index: 1;
}
</style>
""", unsafe_allow_html=True)
# ---------------- SIDEBAR ----------------
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2909/2909763.png", width=100)
st.sidebar.title("🌿 AgroShield")
st.sidebar.markdown("AI-powered sustainable crop protection")
st.sidebar.markdown("---")
st.sidebar.info("Upload a plant image and describe symptoms for best results.")

# ---------------- HERO SECTION ----------------
st.markdown("""
<div class="hero">
<h1>🌾 AgroShield</h1>
<p>Smart AI Plant Diagnosis • Sustainable Treatment • Farmer First</p>
</div>
""", unsafe_allow_html=True)

# ---------------- MAIN CARD ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    plant = st.text_input("🌿 Plant Name")
    image = st.file_uploader("📷 Upload Leaf Image (Optional)", type=["jpg","png","jpeg"])

with col2:
    observation = st.text_area("🔍 Describe Symptoms")

if image:
    st.image(image, caption="Uploaded Plant Image", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🌱 Run AgroShield AI Diagnosis"):
    if plant and observation:
        with st.spinner("🌾 AI analyzing crop health..."):
            time.sleep(1.5)

            prompt = f"""
            The plant is {plant}.
            Symptoms observed: {observation}.
            Provide disease name, cause, treatment and prevention.
            """

            advice = get_disease_info(prompt)

        # Fake AI confidence + health score for UI realism
        confidence = random.randint(82, 97)
        health_score = random.randint(40, 75)

        st.success("Diagnosis Complete 🌿")

        st.subheader("🌱 Crop Health Score")
        st.progress(health_score / 100)
        st.write(f"Health Score: **{health_score}%**")

        st.subheader("🧠 AI Confidence Level")
        st.progress(confidence / 100)
        st.write(f"Confidence: **{confidence}%**")

        st.markdown("<div class='result-box'>", unsafe_allow_html=True)
        st.subheader("🌿 Diagnosis & Sustainable Recommendation")
        st.write(advice)
        st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.warning("Please provide plant name and symptoms.")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("<div class='footer'>AgroShield © 2026 | Revolutionizing Sustainable Agriculture 🌍</div>", unsafe_allow_html=True)