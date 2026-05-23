import streamlit as st
import requests
from chempy import balance_stoichiometry
from streamlit_lottie import st_lottie

# ====================================
# CONFIG
# ====================================
st.set_page_config(
    page_title="Kalkulator Stoikiometri",
    page_icon="🧪",
    layout="wide"
)

# ====================================
# LOAD LOTTIE (ATOM ANIMATION)
# ====================================
def load_lottie(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

atom_anim = load_lottie("https://assets10.lottiefiles.com/packages/lf20_2ks3pjua.json")

# ====================================
# CSS GLOW + FLOAT LIGHT (SAFE INPUT)
# ====================================
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: radial-gradient(circle at top left,
        #e0f7ff,
        #cfe8ff,
        #bfe6ff,
        #dff6ff
    );
}

/* FLOAT LIGHTS */
.stApp::before,
.stApp::after {
    content: "";
    position: fixed;
    width: 200%;
    height: 200%;
    background-image: radial-gradient(circle, rgba(255,255,255,0.5) 2px, transparent 3px);
    background-size: 60px 60px;
    animation: floatLights 30s linear infinite;
    opacity: 0.35;
    z-index: 0;
    pointer-events: none;
}

.stApp::after {
    animation-duration: 45s;
    opacity: 0.2;
}

@keyframes floatLights {
    from {transform: translateY(0px);}
    to {transform: translateY(-800px);}
}

/* TITLE */
.title {
    text-align:center;
    font-size:60px;
    font-weight:900;
    color:#0369a1;
    text-shadow:0 0 20px rgba(56,189,248,0.6);
}

/* CARD */
.card {
    background: rgba(255,255,255,0.8);
    padding:25px;
    border-radius:20px;
    box-shadow:0 10px 25px rgba(0,0,0,0.1);
    backdrop-filter: blur(10px);
}

/* INPUT FIX */
.stTextInput, .stNumberInput, .stSelectbox {
    position: relative;
    z-index: 10;
}

/* BUTTON */
.stButton > button {
    background: linear-gradient(90deg, #0284c7, #38bdf8);
    color:white;
    border-radius:12px;
    height:45px;
    width:100%;
}

</style>
""", unsafe_allow_html=True)

# ====================================
# MENU
# ====================================
menu = st.sidebar.radio(
    "📚 Menu",
    ["🏠 Home", "⚖️ Setarakan Reaksi", "🧪 Mol", "🎮 Quiz", "👥 About"]
)

# ====================================
# HOME (ATOM COVER)
# ====================================
if menu == "🏠 Home":

    st.markdown("<div class='title'>🧪 KALKULATOR STOIKIOMETRI</div>", unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align:center;color:#075985;font-size:18px;'>
    Aplikasi Kimia Interaktif Modern ⚗️
    </div>
    """, unsafe_allow_html=True)

    # ATOM ANIMATION
    if atom_anim:
        st_lottie(atom_anim, height=350)

    st.markdown("""
    <div class="card">

    📌 Fitur aplikasi:
    <br><br>

    ✔ Menyetarakan reaksi kimia otomatis  
    ✔ Menghitung mol  
    ✔ Quiz stoikiometri  
    ✔ Visualisasi kimia modern  

    <br>

    💡 Cara pakai:
    Masukkan reaksi belum setara → klik tombol → hasil keluar ⚖️

    </div>
    """, unsafe_allow_html=True)

# ====================================
# SETARAKAN REAKSI
# ====================================
elif menu == "⚖️ Setarakan Reaksi":

    st.title("⚖️ Setarakan Reaksi Kimia")

    reaksi = st.text_input("Contoh: H2 + O2 -> H2O")

    if reaksi:
        if st.button("⚡ Setarakan"):

            try:
                kiri, kanan = reaksi.split("->")

                reaktan = set(x.strip() for x in kiri.split("+"))
                produk = set(x.strip() for x in kanan.split("+"))

                hasil = balance_stoichiometry(reaktan, produk)

                kiri_hasil = [f"{v}{k}" for k, v in hasil[0].items()]
                kanan_hasil = [f"{v}{k}" for k, v in hasil[1].items()]

                hasil_akhir = " + ".join(kiri_hasil) + " → " + " + ".join(kanan_hasil)

                st.success("✨ HASIL SETARA")
                st.markdown(f"<div class='card'><h3>{hasil_akhir}</h3></div>", unsafe_allow_html=True)

            except:
                st.error("Format salah 😭 pakai ->")

# ====================================
# MOL
# ====================================
elif menu == "🧪 Mol":

    st.title("🧪 Kalkulator Mol")

    massa = st.number_input("Massa (gram)", min_value=0.0)
    mr = st.number_input("Mr", min_value=1.0)

    if st.button("Hitung"):
        mol = massa / mr
        st.success(f"✨ Mol = {mol:.2f}")

# ====================================
# QUIZ
# ====================================
elif menu == "🎮 Quiz":

    st.title("🎮 Quiz Stoikiometri")

    soal = st.selectbox("Pilih soal:", [
        "H2 + O2 -> H2O",
        "N2 + H2 -> NH3",
        "Fe + O2 -> Fe2O3"
    ])

    jawaban = st.text_input("Jawaban kamu")

    if st.button("Cek"):
        if jawaban:
            st.success("✔ Jawaban diterima")
        else:
            st.warning("Isi dulu ya")

# ====================================
# ABOUT
# ====================================
elif menu == "👥 About":

    st.title("👥 Kelompok 10")

    st.markdown("""
    <div class="card">

    1. Faturrahman Chandika (2560630)  
    2. Naisyla Nazwa S. (2560705)  
    3. Nassya Alifha Rasyikha (2560710)  
    4. Reva Aulia (2560749)  
    5. Sarah Nur Ichsani (2560774)  

    </div>
    """, unsafe_allow_html=True)