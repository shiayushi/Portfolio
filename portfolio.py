import streamlit as st
from PIL import Image
from pathlib import Path
# Ayushi Kumari's Portfolio
# Streamlit App
st.set_page_config(page_title="Ayushi Kumari Portfolio", layout="wide", page_icon="💻")


# ---- Hero Section ----
profile_pic = Image.open("photo.jpg")
col1, col2 = st.columns([1, 3])
with col1:
    st.image(profile_pic, width=200)
with col2:
    st.title("Ayushi Kumari")
    st.subheader("👩‍💻 Data Science Enthusiast | Python Developer | AI/ML Learner")
    st.write("B.Tech CSE | Passionate about AI, Data Analysis, and NLP | Let's build something great!")

# ---- Social Links ----
st.markdown("""
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/ayushiikumarii)
[![GitHub](https://img.shields.io/badge/-GitHub-black?style=for-the-badge&logo=github)](https://github.com/shiayushi)
""", unsafe_allow_html=True)



# ---- Navbar ----
st.markdown("""
<style>
.navbar {
    background-color: #f9f9f9;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 25px;
    text-align: center;
}
.navbar a {
    margin: 10px 15px;
    font-weight: bold;
    text-decoration: none;
    font-size: 16px;
    color: #444;
}
.navbar a:hover {
    color: #007ACC;
}
</style>

<div class="navbar">
    <a href="#about-me">About Me</a>
    <a href="#skills">Skills</a>
    <a href="#projects">Projects</a>
    <a href="#resume">Resume</a>
    <a href="#certificates">Certificates</a>
    <a href="#contact-me">Contact Me</a>
</div>
""", unsafe_allow_html=True)

st.divider()

# ---- Page Title ----
# ---- About Me ----
st.markdown('<h2 id="about-me">📌 About Me</h2>', unsafe_allow_html=True)
st.write("""
I am a Computer Science student at Prestige Institute of Management and Research, Bhopal. 
I love building data-driven apps, making interactive dashboards, working with Python, and exploring the fields of NLP and machine learning.
""")

# ---- Skills ----
st.markdown('<h2 id="skills">🛠️ Skills</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col1.write("🔹 Python")
col1.write("🔹 SQL")
col1.write("🔹 Excel")
col2.write("🔹 Power BI")
col2.write("🔹 Tableau")
col2.write("🔹 Streamlit")
col3.write("🔹 Machine Learning")
col3.write("🔹 NLP")
col3.write("🔹 Data Visualization")

st.divider()

# ✅ Projects Section with Expanders
# ---- Projects ----
st.markdown('<h2 id="projects">💻 Projects</h2>', unsafe_allow_html=True)
with st.container():
    st.divider()

with st.expander("💬 NLP Projects"):
    st.write("Here are some of my NLP projects that leverage natural language processing techniques to solve real-world problems. Explore my NLP projects that leverage natural language processing techniques to solve real-world problems"
    "These projects demonstrate my ability to build applications that understand and generate human language.")
    st.divider()

    col1, col2 = st.columns(2)

with col1:
        st.markdown("#### Multilingual Sentiment Analyzer")
        st.image("image/nlp/multilingual_bot.png", width=500)
        st.write("Analyze sentiment in English, Hindi, Hinglish. Built with HuggingFace, Streamlit.")
        st.markdown('[🔗 View Project](https://github.com/shiayushi/Multilingual-sentiment-analysis)', unsafe_allow_html=True)
        

with col2:
        st.markdown("#### AI Interview Bot")
        st.image("image/nlp/interview.png", width=500)
        st.write("Simulates interviews using NLP and provides basic feedback.")
        st.markdown('[🔗 View Project](https://github.com/shiayushi/ai-interview-bot)', unsafe_allow_html=True)


with st.expander("🤖 ML Projects"):
    st.write("Here are some of my machine learning projects that apply algorithms to analyze data and make predictions. Explore my machine learning projects that apply algorithms to analyze data and make predictions. These projects demonstrate my ability to build models that learn from data and provide insights.")
    st.divider()
    col3, col4, col5 = st.columns(3)

with col3:
        st.markdown("""
        <div style='border-right: 1px solid #888; padding-right: 20px;'>""", unsafe_allow_html=True)
        st.markdown("#### 🏠 House Price Prediction")
        st.image("image/ml/house_price.png", width=220)
        st.write("Predict house prices using Linear Regression.")
        st.markdown('[🔗 View Project](https://github.com/shiayushi/House-price-prediction-)', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

with col4:
        st.markdown("""<div style='border-right: 1px solid #888; padding-right: 20px;'>""", unsafe_allow_html=True)
        st.markdown("#### 🌸 Iris Classification")
        st.image("image/ml/iris.png", width=220)
        st.write("Classifies Iris flower species with 95% accuracy.")
        st.markdown('[🔗 View Project](https://github.com/shiayushi/iris-classification)', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

with col5:
        st.markdown("""<div style='padding-right: 20px;'>""", unsafe_allow_html=True)
        st.markdown("#### 📈 Stock Price Prediction")
        st.image("image/ml/stock_price.png", width=220)
        st.write("Forecasts stock prices using ARIMA & LSTM.")
        st.markdown('[🔗 View Project](https://github.com/shiayushi/stock-price-prediction)', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.divider()

# ---- Power BI Dashboards ----
with st.expander("📊 Power BI Dashboards"):
            st.write("Here are some of my Power BI dashboards that visualize data and provide insights. Explore my Power BI dashboards that visualize data and provide insights. These projects demonstrate my ability to create interactive and informative dashboards.")
            st.divider()
            col6, col7, col8 = st.columns(3)
            with col6:
                st.markdown("#### BlinkIt Sales Dashboard")
                st.image("image/power_bi/blinkit.png", width=300)
                st.markdown('[🔗 View Dashboard](https://github.com/shiayushi/Blinkit-sales-analysis-)', unsafe_allow_html=True)
                st.divider()
            with col7:
                st.markdown("#### Hospital Analytics Dashboard")
                st.image("image/power_bi/hospital.png", width=300)
                st.markdown('[🔗 View Dashboard](https://github.com/shiayushi/Hospital-power-bi-project-)', unsafe_allow_html=True)
                st.divider()
            with col8:
                st.markdown("#### HR Analytics Dashboard")
                st.image("image/power_bi/hr_analytics.png", width=300)
                st.markdown('[🔗 View Dashboard](https://github.com/shiayushi/HR-analytics-power-bi-project)', unsafe_allow_html=True)

st.divider()

# ---- Resume ----
st.markdown('<h2 id="resume">📄 Resume</h2>', unsafe_allow_html=True)
with open("resume.pdf", "rb") as file:
    st.download_button(label="📥 Download Resume", data=file, file_name="resume.pdf", mime="application/pdf")

# ✅ Certificates Section
st.markdown('<h2 id="certificates">📜 Certificates</h2>', unsafe_allow_html=True)
with st.container():
    with st.expander("✅ Machine Learning - CodeSoft"):
        st.write("Successfully completed Machine Learning internship with hands-on projects.")
        st.markdown("[🔗 View Certificate](certificate/CODSOFT.pdf)", unsafe_allow_html=True)

    with st.expander("✅ Data Analyst - CodeTechIT"):
        st.write("Completed Data Analyst training with real-world Python scripts.")
        st.markdown("[🔗 View Certificate](certificate/codtechit.png)", unsafe_allow_html=True)

    with st.expander("✅ Data Analyst - Deloite Australia by Forage"):
        st.write("Built dashboards and insights using Power BI and Excel.")
        st.markdown("[🔗 View Certificate](certificate/deloitte.pdf)", unsafe_allow_html=True)

st.divider()

# ---- Contact Me ----
st.markdown('<h2 id="contact-me">📬 Contact Me</h2>', unsafe_allow_html=True)
st.markdown("""
<style>
.contact-container {
    background-color: #2a2a2a;
    padding: 20px;
    border-radius: 10px;
    color: white;
    max-width: 700px;
    margin: auto;
}
.contact-container input, .contact-container textarea {
    width: 100%;
    padding: 10px;
    margin-top: 8px;
    margin-bottom: 16px;
    border: none;
    border-radius: 5px;
    font-size: 16px;
}
.contact-container button {
    background-color: #007ACC;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
}
@media only screen and (max-width: 768px) {
    .contact-container {
        padding: 15px;
    }
    .contact-container input, .contact-container textarea {
        font-size: 14px;
    }
    .contact-container button {
        width: 100%;
    }
}
</style>
<div class="contact-container">
    <form action="https://formsubmit.co/ayushiraj431@gmail.com" method="POST">
        <label>Your Name</label>
        <input type="text" name="name" required>
        <label>Your Email</label>
        <input type="email" name="email" required>
        <label>Message</label>
        <textarea name="message" required></textarea>
        <button type="submit">Send</button>
    </form>
</div>
""", unsafe_allow_html=True)

# ---- Hide Footer ----
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)
