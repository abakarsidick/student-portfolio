import streamlit as st

# Set page config
st.set_page_config(page_title="My Digital Footprint", page_icon="🚀", layout="wide")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Skills", "Testimonials", "Contact"])

# Home Page
if page == "Home":
    st.title("🚀 My Digital Footprint – Showcasing My Journey")
    
    uploaded_image = st.file_uploader("Upload Profile Picture", type=["jpg", "png"])
    if uploaded_image:
        st.image(uploaded_image, width=150, caption="Profile Picture")
    else:
        st.image("king.jpg", width=150, caption="Profile Picture")    
    
    name = st.text_input("Your Name", "Abakar Sidick")
    location = st.text_input("Location", "Musanze, Rwanda")
    field_of_study = st.text_input("Field of Study", "Software Engineering, Year 3")
    university = st.text_input("University", "INES Ruhengeri")
    
    st.write(f"📍 {location}")    
    st.write(f"📚 {field_of_study}")
    st.write(f"🎓 {university}")
    
    try:
        with open("My Resume1.pdf", "rb") as file:
            resume_bytes = file.read()
        st.download_button(label="📄 Download Resume", data=resume_bytes, file_name="resume1.pdf", mime="application/pdf")    
    except FileNotFoundError:
        st.warning("⚠ Resume file not found. Please upload your resume.")

# Projects Page
elif page == "Projects":
    st.title("💻 My Projects")
    
    project_filter = st.selectbox("Filter by Category", ["All", "Year 1", "Year 2", "Year 3", "Dissertation"])
    
    projects = {
        "Year 1": "Library Management System - Python & SQLite",
        "Year 2": "Hotel Management System - Java & MySQL",
        "Year 3": "Car Rental System - Python & SQLite",
        "Dissertation": "Community Hub Group Management Platform - Java & MySQL"
    }
    
    for year, description in projects.items():
        if project_filter == "All" or project_filter == year:
            with st.expander(f"📌 {year} - {description}"):
                st.write(f"*Project Type:* Individual")
                st.write(f"*Description:* A system designed for {description}.")
                st.write("🔗 [GitHub Repo](#)")

# Skills Page
elif page == "Skills":
    st.title("⚡ Skills and Achievements")
    
    skills = {"Python": 90, "JavaScript": 80, "SQL": 85, "Machine Learning": 60, "Web Development": 75}
    
    for skill, value in skills.items():
        st.subheader(skill)
        st.progress(value)
    
    st.subheader("🏆 Certifications & Achievements")
    st.write("✔ Google Data Analytics Certification")
    st.write("✔ AI in Research & Education")
    st.write("✔ Certificate of baccalaureat in high school")

# Testimonials Page
elif page == "Testimonials":
    st.title("🗣 Testimonials")
    
    st.write("🌟Ali is an exceptional problem solver! His final year project was highly innovative. – Dr. Theodore")
    st.write("🌟 An AI Programmer, always eager to learn and contribute! – Mclement")

# Contact Page
elif page == "Contact":
    st.title("📬 Contact Me")
    
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("✅ Message sent successfully!")
    
    st.write("📧 Email:Abakarsidickbaba@gmail.com")
    st.write("[🔗 LinkedIn](linkedin.com/in/abakar-4979071ab)")
    st.write("[📂 GitHub](https://github.com/abakarsidick)")