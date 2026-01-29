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
# Use a web image URL for the background
IMAGE_FILENAME = "https://bhullarinfotech.com/wp-content/uploads/2023/02/portfolio-ten-1-3.jpg"  # ← UPDATE THIS WITH YOUR IMAGE URL
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
    /* Background styling */
    .stApp {{
        {bg_style}
    }}
    
    /* Dark overlay for better text readability */
    [data-testid="stAppViewContainer"] {{
        background-color: rgba(0, 0, 0, 0.65);
    }}
    
    /* Main content area - semi-transparent white */
    .main {{ 
        padding: 2rem;
        background-color: rgba(255, 255, 255, 0.97);
        border-radius: 15px;
        margin: 2rem;
    }}
    
    /* ALL TEXT - WHITE COLOR */
    body, p, div, span, li {{
        color: white !important;
    }}
    
    /* Headings - White */
    h1, h2, h3, h4, h5, h6 {{
        color: white !important;
        font-weight: 600;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
    }}
    
    /* Input and Text areas - Dark background with dark text */
    input, textarea {{
        color: #333 !important;
        background-color: white !important;
    }}
    
    .stTextInput label, .stTextArea label, .stSelectbox label {{
        color: white !important;
    }}
    
    /* Info boxes - White text */
    .stInfo, .stWarning, .stError, .stSuccess {{
        color: white !important;
    }}
    
    .stInfo {{
        background-color: rgba(25, 118, 210, 0.3) !important;
        border-color: rgba(25, 118, 210, 0.6) !important;
    }}
    
    .highlight {{ 
        color: #64d5ff; 
        font-weight: bold; 
    }}
    
    .project-card {{ 
        background-color: rgba(240, 242, 246, 0.95); 
        padding: 1.5rem; 
        border-radius: 10px; 
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        border-left: 5px solid #1f77b4;
        color: #333;
    }}
    
    .skill-badge {{
        display: inline-block;
        background: linear-gradient(135deg, #1f77b4 0%, #164a7f 100%);
        color: white;
        padding: 0.6rem 1.2rem;
        border-radius: 25px;
        margin: 0.4rem;
        font-size: 0.9rem;
        box-shadow: 0 4px 12px rgba(31, 119, 180, 0.3);
        font-weight: 500;
    }}
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, rgba(31, 119, 180, 0.95) 0%, rgba(31, 119, 180, 0.85) 100%);
        box-shadow: 2px 0 10px rgba(0, 0, 0, 0.3);
    }}
    
    [data-testid="stSidebar"] * {{
        color: white !important;
    }}
    
    /* Buttons */
    .stButton > button {{
        background-color: #1f77b4;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.6rem 1.5rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }}
    
    .stButton > button:hover {{
        background-color: #164a7f;
        box-shadow: 0 4px 12px rgba(31, 119, 180, 0.4);
        transform: translateY(-2px);
    }}
    
    /* Links - Light blue */
    a {{
        color: #64d5ff !important;
        text-decoration: none;
    }}
    
    a:hover {{
        color: #ff6b6b !important;
    }}
    
    /* Divider */
    hr {{
        border-color: rgba(255, 255, 255, 0.2) !important;
    }}
    
    /* Radio buttons and checkboxes */
    .stRadio > label, .stCheckbox > label {{
        color: white !important;
    }}
    
    /* Form text */
    .stForm {{
        color: white !important;
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
        <div style='text-align: center; padding: 4rem 2rem;'>
            <h1 style='color: white; font-size: 3rem; margin-bottom: 1rem;'>Hi! I'm Sakshi Kotur 👋</h1>
            <h3 style='color: #64d5ff; font-size: 1.5rem; margin-bottom: 2rem;'>Aspiring Data Scientist | Machine Learning Enthusiast | Python Developer</h3>
            <p style='color: white; font-size: 1.1rem; line-height: 1.8; max-width: 800px; margin: 0 auto 2rem;'>
                Welcome to my portfolio! I'm passionate about turning data into actionable insights 
                and building intelligent, real-world solutions using machine learning and analytics.
            </p>
            <p style='color: white; font-size: 1.1rem; line-height: 1.8; max-width: 800px; margin: 0 auto;'>
                With a strong foundation in Python and hands-on experience in AI and data science projects, 
                I enjoy solving complex problems and creating impactful, data-driven applications.
            </p>
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
            "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0A31DNMIqpK9SDween4l6C_uNP4Yf_Qy7t6A8l7O0okOX77UknQxZV_cZ6pt126oLg_g&usqp=CAU"
        },
        {
            "title": "Project 2: AI Powered Research Assistant",
            "description": "Built an AI-powered research assistant to fetch, analyze, and summarize information using large language models, providing an interactive interface for efficient research workflows.",
            "technologies": ["Python", "LangChain", "Streamlit", "Hugging Face", "APIs"],
            "link": "https://github.com/SakshiSK966/AI-powered-Research-Assistant",
            "image_url": "https://images.unsplash.com/photo-1516534775068-bb57a39cbb28?w=500&h=500&fit=crop"
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
                    f'<span class="skill-badge">{tech}</span>' 
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
        "Databases": ["MySQL" ,"PostgreSQL", "SQLite", "MongoDB (basic)"],
        "Other": ["Git & GitHub", "Statistics for Data Science", "Problem Solving & Analytical Thinking"]
    }
    
    for category, skills in skills_data.items():
        st.subheader(category)
        skill_html = " ".join([
            f'<span class="skill-badge">{skill}</span>' 
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
            "duration": "Nov 27,2025 - Jan 21,2026",
            "description": "Developed an AI-powered park surveillance web application integrating machine learning for activity monitoring and basic anomaly detection. Built an interactive web interface to visualize surveillance insights and improve safety analysis."
        },
        {
            "title": "Data Science Intern",
            "company": "Echo Brains(A Dextris Company), Bengaluru",
            "duration": "Jan 27,2026 - Present",
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
    <div style='text-align: center; color: white; padding: 2rem; background-color: rgba(0, 0, 0, 0.5); border-radius: 15px; margin: 2rem;'>
    <p style='font-size: 16px; margin: 0;'>© 2025 Sakshi Kotur. All rights reserved.</p>
    <p style='font-size: 14px; color: #ccc; margin: 0.5rem 0 0 0;'>Built with Streamlit | Last updated: """ + datetime.now().strftime("%B %d, %Y") + """</p>
    </div>
""", unsafe_allow_html=True)
