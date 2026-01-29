# My Portfolio - Built with Streamlit

A clean, professional portfolio website built using Streamlit. Perfect for showcasing your projects, skills, and experience to potential employers and clients.

## Features

- **Multi-page navigation** with sidebar menu
- **Responsive design** that works on desktop and mobile
- **Project showcase** with technologies and links
- **Skills section** with categorized expertise
- **Experience timeline** with education details
- **Contact form** for getting in touch
- **Professional styling** with custom CSS

## Setup Instructions

### 1. Clone or Create Project
```bash
mkdir my-portfolio
cd my-portfolio
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Customize Your Portfolio

Edit `streamlit_portfolio.py` and replace:
- `[Your Name]` with your actual name
- Profile image URL with your image
- All the placeholder content with your information
- Social media links
- Project details
- Work experience
- Skills and technologies

### 5. Run Locally
```bash
streamlit run streamlit_portfolio.py
```

The app will open at `http://localhost:8501`

## Deployment to Streamlit Cloud

### Step 1: Push to GitHub
1. Create a GitHub repository
2. Push your code:
```bash
git init
git add .
git commit -m "Initial portfolio"
git branch -M main
git remote add origin https://github.com/yourprofile/my-portfolio.git
git push -u origin main
```

### Step 2: Deploy to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Connect your GitHub repository
4. Select the branch and file (`streamlit_portfolio.py`)
5. Click "Deploy"

Your portfolio will be live at: `https://your-username-portfolio.streamlit.app`

## File Structure
```
my-portfolio/
├── streamlit_portfolio.py    # Main application
├── requirements.txt          # Python dependencies
├── .streamlit/
│   └── config.toml          # Streamlit configuration
└── README.md                # This file
```

## Information to Customize

### Home Section
- Your name and title
- Headline/tagline
- Metrics (projects, experience, skills count)

### About Section
- Professional summary (2-3 paragraphs)
- Education background
- Career journey
- Current role/goals
- Location, languages, current learning

### Projects Section
- Project title
- Brief description
- Technologies used
- GitHub/live link
- Project image

### Skills Section
- Programming languages
- Data science/ML skills
- Tools and libraries
- Databases
- Other relevant skills

### Experience Section
- Job title
- Company name
- Duration (dates)
- Brief description of responsibilities
- Educational degrees and institutions

### Contact Section
- Email address
- LinkedIn profile URL
- GitHub profile URL
- Twitter/other social media (optional)

## Customization Tips

### Adding Images
Replace placeholder URLs with your own images:
```python
st.image("path/to/your/image.jpg", use_column_width=True)
```

### Adding Styled Boxes
Use expanders for collapsible sections:
```python
with st.expander("See more"):
    st.write("Hidden content here")
```

### Embedding External Content
Use markdown to embed links:
```python
st.markdown("[View on GitHub](https://github.com/yourprofile/project)")
```

## Color Scheme
You can customize colors in `.streamlit/config.toml`:
- Primary Color: #1f77b4 (Blue)
- Background: #ffffff (White)
- Secondary Background: #f0f2f6 (Light Gray)
- Text: #262730 (Dark)

## Technologies Used
- **Streamlit** - Web framework
- **Python 3.8+** - Programming language
- **Pillow** - Image processing
- **Requests** - HTTP requests

## Tips for Better Results

1. **Professional Photos**: Use a high-quality headshot
2. **Clear Descriptions**: Make project descriptions concise but informative
3. **GitHub Links**: Always link to your actual GitHub repositories
4. **Keep Updated**: Update your portfolio as you gain new skills/projects
5. **Optimize Performance**: Use `@st.cache_data` for expensive operations
6. **Test Responsiveness**: Check how it looks on mobile

## Troubleshooting

**Images not loading?**
- Ensure the image URL is publicly accessible
- Test the URL in a browser first

**Form not working?**
- You'll need to add a backend service (e.g., EmailJS) for actual email sending
- Currently, it shows a success message

**Deployment fails?**
- Check that `requirements.txt` is in the root directory
- Ensure all imports in your code are listed in requirements.txt

## Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Cloud Deployment](https://docs.streamlit.io/streamlit-cloud/get-started)
- [Streamlit Components](https://docs.streamlit.io/library/api-reference)

## License

Feel free to use this template for your portfolio!

## Next Steps

1. Customize all placeholder content
2. Add your real images and links
3. Test locally with `streamlit run`
4. Deploy to Streamlit Cloud
5. Share your portfolio with the world!

---

**Need Help?** Check the Streamlit documentation or post in the [Streamlit community forums](https://discuss.streamlit.io)
