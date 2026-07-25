import streamlit as st
import datetime
import base64

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Gururaj & Vaishnavi | Our Story ❤️",
    page_icon="💍",
    layout="centered"
)

# --- HELPER FUNCTION TO CONVERT IMAGE TO BASE64 FOR HTML RENDERING ---
def get_image_base64(path):
    try:
        with open(path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()
            return f"data:image/jpeg;base64,{encoded}"
    except Exception:
        return None

# Load images
gururaj_img = get_image_base64("assets/Gururaj.jpeg") or get_image_base64("assets/gururaj.jpg")
vaishnavi_img = get_image_base64("assets/Vaishnavi.jpeg") or get_image_base64("assets/vaishnavi.jpg")

# --- CUSTOM ROMANTIC STYLING ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;400;600&family=Great+Vibes&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #FFF0F2 0%, #FFE4E8 100%);
        font-family: 'Poppins', sans-serif;
    }
    
    .main-title {
        font-family: 'Dancing Script', cursive;
        color: #B22222;
        text-align: center;
        font-size: 3.2rem !important;
        margin-bottom: 0px;
    }
    
    .sub-title {
        text-align: center;
        color: #7A3E3E;
        font-size: 1.1rem;
        font-style: italic;
        margin-bottom: 25px;
    }

    /* --- ATTRACTIVE PHOTO CARDS (PERFECT SIZE ALIGNMENT) --- */
    .photo-grid {
        display: flex;
        gap: 20px;
        justify-content: center;
        align-items: center;
        margin-top: 15px;
        margin-bottom: 25px;
    }

    .photo-card {
        flex: 1;
        background: #FFFFFF;
        padding: 14px;
        border-radius: 22px;
        box-shadow: 0px 10px 30px rgba(255, 75, 75, 0.18);
        border: 2px solid #FFCCD5;
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .photo-card:hover {
        transform: translateY(-6px);
        box-shadow: 0px 15px 35px rgba(255, 75, 75, 0.28);
    }

    .photo-card img {
        width: 100%;
        height: 380px; /* Fixed equal height for both pictures */
        object-fit: cover;
        object-position: top center;
        border-radius: 16px;
    }

    .photo-caption {
        font-family: 'Poppins', sans-serif;
        font-size: 1.25rem;
        font-weight: 600;
        color: #B22222;
        margin-top: 12px;
        margin-bottom: 4px;
    }

    /* Mobile Responsive Fix */
    @media (max-width: 600px) {
        .photo-grid {
            flex-direction: column;
        }
        .photo-card img {
            height: 340px;
        }
    }

    /* --- TIMELINE CARDS STYLING --- */
    .timeline-card {
        background: rgba(255, 255, 255, 0.9);
        padding: 20px;
        border-radius: 18px;
        box-shadow: 0px 6px 18px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border-left: 6px solid #FF4B4B;
    }

    .timeline-date {
        font-weight: 700;
        color: #B22222;
        font-size: 1.1rem;
        margin-bottom: 6px;
    }

    .love-card {
        background: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.06);
        text-align: center;
    }

    /* --- ROMANTIC SECRET LETTER STYLING --- */
    .romantic-letter {
        background: linear-gradient(135deg, #FFFFFF 0%, #FFF5F6 100%);
        padding: 32px 28px;
        border-radius: 24px;
        border: 2px solid #FFB6C1;
        box-shadow: 0px 12px 35px rgba(255, 75, 75, 0.2);
        position: relative;
        overflow: hidden;
        margin-top: 20px;
    }

    .romantic-letter::before {
        content: "💌";
        position: absolute;
        top: 10px;
        right: 15px;
        font-size: 2.2rem;
        opacity: 0.3;
    }

    .letter-heading {
        font-family: 'Dancing Script', cursive;
        color: #B22222;
        font-size: 2.3rem;
        margin-top: 0;
        margin-bottom: 15px;
        border-bottom: 2px dashed #FFCCD5;
        padding-bottom: 8px;
    }

    .letter-body {
        font-size: 1.08rem;
        color: #4A3E3E;
        line-height: 1.8;
        font-family: 'Poppins', sans-serif;
    }

    .letter-footer {
        text-align: right;
        margin-top: 20px;
    }

    .lots-of-love {
        font-family: 'Dancing Script', cursive;
        font-size: 1.8rem;
        color: #FF4B4B;
        font-weight: bold;
        margin-bottom: 2px;
    }

    .signature {
        font-size: 1.15rem;
        font-weight: 600;
        color: #B22222;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("<h1 class='main-title'>Gururaj ❤️ Vaishnavi</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Two strangers, one Instagram request, and a lifetime of forever. ✨</p>", unsafe_allow_html=True)

# --- LIVE REAL-TIME JS COUNTDOWN TIMER ---
st.components.v1.html("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    body { font-family: 'Poppins', sans-serif; background: transparent; margin: 0; }
    .countdown-card {
        background: #FFFFFF;
        padding: 18px;
        border-radius: 20px;
        box-shadow: 0px 8px 25px rgba(255, 75, 75, 0.15);
        text-align: center;
        border: 2px solid #FF8585;
    }
    .countdown-box {
        display: flex;
        justify-content: space-around;
        margin-top: 10px;
    }
    .time-unit {
        background: #FFF0F2;
        padding: 10px 14px;
        border-radius: 12px;
        min-width: 60px;
    }
    .time-number {
        font-size: 1.6rem;
        font-weight: 700;
        color: #B22222;
    }
    .time-label {
        font-size: 0.75rem;
        color: #666;
        text-transform: uppercase;
    }
    </style>

    <div class='countdown-card'>
        <h3 style='color: #B22222; margin:0; font-size: 1.3rem;'>💍 Engagement Countdown</h3>
        <p style='color: #777; margin-bottom: 8px; font-size: 0.85rem;'>August 18, 2026 at 11:00 AM</p>
        <div class='countdown-box'>
            <div class='time-unit'><div id='cd-days' class='time-number'>0</div><div class='time-label'>Days</div></div>
            <div class='time-unit'><div id='cd-hours' class='time-number'>0</div><div class='time-label'>Hours</div></div>
            <div class='time-unit'><div id='cd-mins' class='time-number'>0</div><div class='time-label'>Mins</div></div>
            <div class='time-unit'><div id='cd-secs' class='time-number'>0</div><div class='time-label'>Secs</div></div>
        </div>
    </div>

    <script>
    function updateTimer() {
        const target = new Date("August 18, 2026 11:00:00").getTime();
        const now = new Date().getTime();
        const diff = target - now;

        if (diff > 0) {
            const d = Math.floor(diff / (1000 * 60 * 60 * 24));
            const h = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const m = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
            const s = Math.floor((diff % (1000 * 60)) / 1000);

            document.getElementById('cd-days').innerText = d;
            document.getElementById('cd-hours').innerText = h;
            document.getElementById('cd-mins').innerText = m;
            document.getElementById('cd-secs').innerText = s;
        }
    }
    updateTimer();
    setInterval(updateTimer, 1000);
    </script>
""", height=180)

st.write("---")

# --- ATTRACTIVE PHOTO HIGHLIGHT SECTION ---
st.markdown("<h2 style='text-align: center; color: #B22222; font-family: \"Dancing Script\", cursive; font-size: 2.6rem; margin-bottom: 15px;'>🤵🏻‍♂️ The Groom & The Bride 👰🏻‍♀️</h2>", unsafe_allow_html=True)

# Render HTML Photo Cards with exact matching height
st.markdown(f"""
<div class='photo-grid'>
    <div class='photo-card'>
        <img src='{gururaj_img if gururaj_img else ""}' alt='Gururaj' />
        <div class='photo-caption'>Gururaj 🤵🏻‍♂️</div>
    </div>
    <div class='photo-card'>
        <img src='{vaishnavi_img if vaishnavi_img else ""}' alt='Vaishnavi' />
        <div class='photo-caption'>Vaishnavi 👰🏻‍♀️</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("---")

# --- OUR STORY TIMELINE ---
st.markdown("### 📖 How Destiny Played Its Part")

st.markdown("""
<div class='timeline-card'>
    <div class='timeline-date'>🗓️ May 11 | The Near Miss</div>
    <p>You attended a function where I wasn't present... Destiny was quietly waiting for the perfect time! 😉</p>
</div>

<div class='timeline-card'>
    <div class='timeline-date'>🏠 June 16 | The Height Check Moment! 📏</div>
    <p>The formal meeting at my home! Amongst all the traditions, checking our heights was hands down the cutest and funniest moment we'll always laugh about.</p>
</div>

<div class='timeline-card'>
    <div class='timeline-date'>📲 July 11 | The Instagram Plot Twist 🙈</div>
    <p>I sent a request and immediately deleted it out of nervousness! But you caught it, requested back, sent that first message, and our endless chats began!</p>
</div>

<div class='timeline-card'>
    <div class='timeline-date'>💍 August 18, 2026 | 11:00 AM</div>
    <p>The moment we officially lock our forever commitment!</p>
</div>
""", unsafe_allow_html=True)

st.write("---")

# --- INTERACTIVE QUIZ SECTION ---
st.markdown("### 💖 Fun Question For You")

with st.container():
    st.markdown("<div class='love-card'>", unsafe_allow_html=True)
    answer = st.radio(
        "**Who actually made the first move on Instagram?** 🙈",
        ["Vaishnavi (sent & deleted instantly)", "Gururaj (sent back & texted)", "Both of us (Destiny!)"],
        index=None
    )
    
    if answer:
        st.snow()     # Snow Effect
        st.balloons() # Festive Balloons Effect
        st.markdown("<br>", unsafe_allow_html=True)
        st.progress(100)
        st.markdown("<p style='color: #B22222; font-weight: 600; font-size: 1.1rem;'>Match Compatibility: 100% Perfect! ❤️</p>", unsafe_allow_html=True)
        if answer == "Vaishnavi (sent & deleted instantly)":
            st.info("Hey! I panicked and deleted it... but you were quick enough to notice! 😉")
        elif answer == "Gururaj (sent back & texted)":
            st.success("You took the lead and made our story happen! ✨")
        elif answer == "Both of us (Destiny!)":
            st.success("It was written in the stars! 🌟")
    st.markdown("</div>", unsafe_allow_html=True)

st.write("---")

# --- SPECIAL SECRET MESSAGE SECTION ---
st.markdown("### 💌 A Special Message Just For You")

if st.checkbox("Tap to Unfold My Letter ✉️"):
    st.snow()     # Snow Effect
    st.balloons() # Festive Balloons Effect
    st.markdown("""
        <div class='romantic-letter'>
            <div class='letter-heading'>Dearest Gururaj, ❤️</div>
            <div class='letter-body'>
                From that hilarious height-check moment at my home to talking for endless nights, 
                every single moment with you feels effortlessly warm, comforting, and special. 🌸
                <br><br>
                Even though our families brought us together through an arranged setup, 
                falling for you and choosing you is the easiest and best decision I have ever made. 💖
                <br><br>
                <b>I can't wait for August 18th at 11:00 AM to officially hold your hand and start our forever journey together!</b> 💍✨
            </div>
            <div class='letter-footer'>
                <div class='lots-of-love'>Lots of Love & Hugs, 💕</div>
                <div class='signature'>— Always Yours, Vaishnavi 👰🏻‍♀️</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.write("")
st.markdown("<p style='text-align: center; color: #888888; font-size: 0.85rem;'>Crafted with ❤️ by Vaishnavi</p>", unsafe_allow_html=True)