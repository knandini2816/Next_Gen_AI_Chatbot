import streamlit as st
import ollama

st.set_page_config(
    page_title="AI CHATBOT",
    page_icon="🤖",
    layout="centered"
)

# --------------------------------------------------
# CSS
# --------------------------------------------------

st.markdown("""
<style>

/* MAIN BACKGROUND */
.stApp {
    background:
        radial-gradient(circle at 10% 20%, #ff00cc55 0%, transparent 25%),
        radial-gradient(circle at 90% 10%, #00ffff55 0%, transparent 25%),
        radial-gradient(circle at 50% 90%, #7b2cff55 0%, transparent 30%),
        linear-gradient(135deg, #050014, #10002b, #00152e);

    color: white;
}


/* HIDE STREAMLIT HEADER */
header {
    visibility: hidden;
}


/* TITLE */
h1 {
    text-align: center;

    font-size: 65px !important;

    font-weight: 900;

    background:
        linear-gradient(
            90deg,
            #ff00cc,
            #ffea00,
            #00ffff,
            #7b2cff,
            #ff00cc
        );

    background-size: 300%;

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    animation: gradientMove 5s infinite linear;

    text-shadow:
        0 0 10px #ff00cc,
        0 0 25px #00ffff;

    margin-bottom: 5px;
}


/* TITLE ANIMATION */
@keyframes gradientMove {

    0% {
        background-position: 0%;
    }

    50% {
        background-position: 100%;
    }

    100% {
        background-position: 0%;
    }
}


/* SUBTITLE */
.subtitle {

    text-align: center;

    color: white;

    font-size: 20px;

    letter-spacing: 5px;

    margin-bottom: 25px;

    text-shadow:
        0 0 10px #00ffff,
        0 0 20px #00ffff;
}


/* READY STATUS */
.ready {

    text-align: center;

    color: #00ffcc;

    font-size: 14px;

    letter-spacing: 3px;

    margin-bottom: 25px;

    text-shadow:
        0 0 10px #00ffcc,
        0 0 20px #00ffcc;

}


/* INPUT LABEL */
label {

    color: #00ffff !important;

    font-size: 18px !important;

    font-weight: bold !important;
}


/* INPUT BOX */
.stTextInput input {

    background:
        linear-gradient(
            135deg,
            #ffffff,
            #eaffff
        ) !important;

    color: #111111 !important;

    border: 3px solid transparent !important;

    border-radius: 18px !important;

    padding: 16px !important;

    font-size: 18px !important;

    box-shadow:
        0 0 10px #00ffff,
        0 0 25px #ff00cc55;

    transition: 0.3s;
}


/* INPUT HOVER */
.stTextInput input:hover {

    transform: scale(1.02);

    box-shadow:
        0 0 15px #ff00cc,
        0 0 35px #00ffff;
}


/* ASK BUTTON */
.stButton button {

    width: 100%;

    height: 60px;

    border: none;

    border-radius: 18px;

    color: white !important;

    font-size: 21px;

    font-weight: 900;

    letter-spacing: 2px;

    background:
        linear-gradient(
            90deg,
            #ff0080,
            #7928ca,
            #00c6ff,
            #00ffcc
        );

    background-size: 300%;

    animation: buttonGlow 4s infinite;

    box-shadow:
        0 0 10px #ff0080,
        0 0 25px #00ffff;

    transition: 0.3s;
}


/* BUTTON ANIMATION */
@keyframes buttonGlow {

    0% {
        background-position: 0%;
    }

    50% {
        background-position: 100%;
    }

    100% {
        background-position: 0%;
    }
}


/* BUTTON HOVER */
.stButton button:hover {

    transform: scale(1.03);

    box-shadow:
        0 0 20px #ff00cc,
        0 0 40px #00ffff,
        0 0 70px #7b2cff;
}


/* RESPONSE TITLE */
h3 {

    color: #ffe600 !important;

    font-size: 28px !important;

    font-weight: 900;

    text-shadow:
        0 0 10px #ffe600,
        0 0 20px #ff8c00;
}


/* AI RESPONSE BOX */
.response-box {

    background:
        linear-gradient(
            135deg,
            rgba(0,255,255,0.15),
            rgba(255,0,204,0.15),
            rgba(123,44,255,0.2)
        );

    backdrop-filter: blur(20px);

    border: 2px solid #00ffff;

    border-radius: 25px;

    padding: 25px;

    color: white;

    font-size: 18px;

    line-height: 1.8;

    box-shadow:
        0 0 15px #00ffff,
        0 0 35px #ff00cc55;

}


/* FOOTER */
.footer {

    text-align: center;

    margin-top: 35px;

    color: #aaaaaa;

    font-size: 13px;

    letter-spacing: 2px;

}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🤖 AI CHATBOT")

st.markdown(
    '<div class="subtitle">✦ NEXT GENERATION INTELLIGENCE ✦</div>',
    unsafe_allow_html=True
)

# Small replacement for the unwanted box
st.markdown(
    '<div class="ready">● AI SYSTEM ONLINE • READY TO CHAT</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# QUESTION
# --------------------------------------------------

question = st.text_input(
    "💬 ASK YOUR AI ANYTHING",
    placeholder="what is AI?"
)


# --------------------------------------------------
# BUTTON
# --------------------------------------------------

if st.button("⚡ ASK AI"):

    if question:

        with st.spinner("🧠 AI IS THINKING..."):

            response = ollama.chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

        answer = response["message"]["content"]

        st.subheader("✨ AI RESPONSE")

        st.markdown(
            f"""
            <div class="response-box">
                🤖 &nbsp; {answer}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.warning("⚠️ Please enter a question.")


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    '<div class="footer">POWERED BY OLLAMA • LLAMA 3.2 • AI TECHNOLOGY</div>',
    unsafe_allow_html=True
)