import streamlit as st
from datetime import datetime
import requests
from PIL import Image
from io import BytesIO
import base64
import os

# Page configuration
st.set_page_config(
    page_title="Sakshi Kotur - Portfolio",
    page_icon="👨‍💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to convert image to base64
def get_base64_image(image_path):
    """Convert local or remote image to base64 for CSS background"""
    try:
        # Check if it's a URL
        if image_path.startswith('http://') or image_path.startswith('https://'):
            response = requests.get(image_path)
            response.raise_for_status()
            return base64.b64encode(response.content).decode()
        else:
            # Local file
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.warning(f"⚠️ Image file '{image_path}' not found. Make sure it's in the same folder as this script!")
        return None
    except requests.exceptions.RequestException:
        st.warning(f"⚠️ Could not fetch image from URL: {image_path}")
        return None

# ============== IMPORTANT: Set your image filename here ==============
# Change 'Background.jpg' to your actual image filename
IMAGE_FILENAME = "https://bhullarinfotech.com/wp-content/uploads/2023/02/portfolio-ten-1-3.jpg"  # ← UPDATE THIS WITH YOUR IMAGE NAME
# ====================================================================

# Get base64 of background image
bg_base64 = get_base64_image(IMAGE_FILENAME)

# Set background style
if bg_base64:
    bg_style = f"background-image: url('data:image/jpg;base64,{bg_base64}'); background-attachment: fixed; background-size: cover; background-position: center;"
else:
    bg_style = "background-color: #f5f5f5;"  # Fallback color if image not found

# Custom CSS for better styling with background image - WHITE TEXT VERSION
st.markdown(f"""
<style>
    .stApp {{
        {bg_style}
    }}
    .main {{
        background-color: rgba(0, 0, 0, 0.7);
        border-radius: 10px;
        padding: 20px;
    }}
    .stMarkdown, .stWrite, h1, h2, h3, .stInfo {{
        color: white !important;
    }}
    .stDivider {{
        background-color: rgba(255, 255, 255, 0.3) !important;
    }}
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.title("🎯 Navigation")
    page = st.radio(
        "Go to:",
        ["Home", "About", "Projects", "Skills", "Experience", "Contact"]
    )

# ============== PAGE: HOME ==============
if page == "Home":
    # Center the content
    st.markdown("""
    <div style="text-align: center; color: white;">
        <h1>Hi! I'm Sakshi Kotur 👋</h1>
        <h3>Aspiring Data Scientist | Machine Learning Enthusiast | Python Developer</h3>
        <p>Welcome to my portfolio! I'm passionate about turning data into actionable insights and building intelligent, real-world solutions using machine learning and analytics.</p>
        <p>With a strong foundation in Python and hands-on experience in AI and data science projects, I enjoy solving complex problems and creating impactful, data-driven applications.</p>
    </div>
    """, unsafe_allow_html=True)

# ============== PAGE: ABOUT ==============
elif page == "About":
    st.title("About Me")
    col1, col2 = st.columns([2, 1], gap="large")
    with col1:
        st.header("Professional Summary")
        st.write("""
Aspiring Data Analyst and Data Scientist with a strong foundation in Python, machine learning, and data analysis concepts. Hands-on experience in building AI-driven projects and developing end-to-end solutions using tools such as Pandas, NumPy, Scikit-learn, Streamlit, and FastAPI. Familiar with data cleaning, visualization, and extracting meaningful insights from datasets. A motivated fresher with strong problem-solving skills, a continuous learning mindset, and a passion for applying data science and AI techniques to real-world challenges.
        """)
    with col2:
        st.header("Quick Facts")
        st.info("""
📍 Location: Bengaluru, Karnataka
🎓 Education: B.E in Artificial Intelligence and Data Science from S.G.Balekundri Institute of Technology, Belagavi, CGPA: 8.65
🌍 Languages: English, Kannada, Hindi
🎯 Currently: Fresher
        """)

# ============== PAGE: PROJECTS ==============
elif page == "Projects":
    st.title("Projects")
    projects = [
        {
            "title": "Project 1: AI-Based Park Surveillance System",
            "description": "Developed a web-based park surveillance system using machine learning for activity monitoring and basic anomaly detection, with an interactive dashboard for visualization.",
            "technologies": ["Python", "Machine Learning", "OpenCV", "Streamlit"],
            "link": "https://github.com/Springboard-Internship-2025/AI-Based-Intel-Video-Surv-Platform-for-Activity-Recognition-and-Sec-Mgt-in-Parks_Nov_Batch-6_2025/tree/SakshiSK966",
            "image_url": "https://www.freepik.com/free-vector/isometric-public-security-composition-street-scenery-with-walking-people-person-having-his-face-recognized_17102695.htm#fromView=keyword&page=1&position=3&uuid=af321a7c-256f-48b5-b7c8-1a1fc0b84349&query=Security+camera+cityscape"
        },
        {
            "title": "Project 2: AI Powered Research Assistant",
            "description": "Built an AI-powered research assistant to fetch, analyze, and summarize information using large language models, providing an interactive interface for efficient research workflows.",
            "technologies": ["Python", "LangChain", "Streamlit", "Hugging Face", "APIs"],
            "link": "https://github.com/SakshiSK966/AI-powered-Research-Assistant",
            "image_url": "https://via.placeholder.com/300x200?text=Research+Assistant"  # Using placeholder since local path won't work
        }
    ]

    for i, project in enumerate(projects):
        with st.container():
            col1, col2 = st.columns([1, 2], gap="large")
            with col1:
                try:
                    st.image(project["image_url"], width=250)
                except:
                    st.info("Image not available")
            with col2:
                st.subheader(project["title"])
                st.write(project["description"])
                # Technologies
                st.write("**Technologies:**")
                tech_html = " ".join([
                    f'<span style="background-color: #0066cc; color: white; padding: 5px 10px; border-radius: 5px; margin-right: 5px;">{tech}</span>'
                    for tech in project["technologies"]
                ])
                st.markdown(tech_html, unsafe_allow_html=True)
                # Links
                col_link1, col_link2 = st.columns(2)
                with col_link1:
                    st.markdown(f"[View Code]({project['link']})")
            if i < len(projects) - 1:
                st.divider()

# ============== PAGE: SKILLS ==============
elif page == "Skills":
    st.title("Skills & Expertise")
    skills_data = {
        "Programming Languages": ["Python", "SQL"],
        "Data Science & ML": ["Data Analysis & Data Cleaning", "Machine Learning Fundamentals", "Exploratory Data Analysis (EDA)", "Data Visualization"],
        "Tools & Libraries": ["Pandas", "NumPy", "Scikit-learn", "TensorFlow", "Streamlit"],
        "Databases": ["MySQL", "PostgreSQL", "SQLite", "MongoDB (basic)"],
        "Other": ["Git & GitHub", "Statistics for Data Science", "Problem Solving & Analytical Thinking"]
    }

    for category, skills in skills_data.items():
        st.subheader(category)
        skill_html = " ".join([
            f'<span style="background-color: #28a745; color: white; padding: 5px 10px; border-radius: 5px; margin-right: 5px;">{skill}</span>'
            for skill in skills
        ])
        st.markdown(skill_html, unsafe_allow_html=True)
        st.write("")

# ============== PAGE: EXPERIENCE ==============
elif page == "Experience":
    st.title("Work Experience")
    experiences = [
        {
            "title": "Artificial Intelligence Intern",
            "company": "Infosys Springboard 6.0",
            "duration": "Nov 27, 2025 - Jan 21, 2026",
            "description": "Developed an AI-powered park surveillance web application integrating machine learning for activity monitoring and basic anomaly detection. Built an interactive web interface to visualize surveillance insights and improve safety analysis."
        },
        {
            "title": "Data Science Intern",
            "company": "Echo Brains (A Dextris Company), Bengaluru",
            "duration": "Jan 27, 2026 - Present",
            "description": "Assisted in understanding data science and NLP workflows, including data preprocessing and basic text analysis techniques. Gained hands-on exposure to industry tools, collaborative development practices, and real-world data science use cases."
        }
    ]

    for i, exp in enumerate(experiences):
        with st.container():
            st.subheader(exp["title"])
            col1, col2 = st.columns([2, 1])
            with col1:
                st.write(f"**{exp['company']}**")
            with col2:
                st.write(f"*{exp['duration']}*")
            st.write(exp["description"])
            if i < len(experiences) - 1:
                st.divider()

# ============== PAGE: CONTACT ==============
elif page == "Contact":
    st.title("Get In Touch")
    st.write("I'd love to hear from you! Feel free to reach out through any of these channels:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("""
📧 **Email**
sakshikotur19@gmail.com
        """)
    with col2:
        st.info("""
💼 **LinkedIn**
https://www.linkedin.com/in/sakshi-s-k/
        """)
    with col3:
        st.info("""
🐙 **GitHub**
https://github.com/SakshiSK966
        """)

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: white;">
    <p>© 2025 Sakshi Kotur. All rights reserved.</p>
    <p>Built with Streamlit | Last updated: """ + datetime.now().strftime("%B %d, %Y") + """</p>
</div>
""", unsafe_allow_html=True)
