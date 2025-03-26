import streamlit as st
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import random
import requests
import io

# Page Configuration
st.set_page_config(page_title="00263838 Web App", page_icon="✨", layout="wide")

# Sidebar Navigation
st.sidebar.title("🚪 Navigation")
page = st.sidebar.radio("Go to:", ["Home", "AI Chatbot", "Contact", "Gallery", "To-Do List", "FAQ", "Weather"])

# Live Clock
def get_current_time():
    return datetime.now().strftime('%H:%M:%S')

st.sidebar.markdown(f"🕐 **Current Time:** {get_current_time()}")

# Function to create PDF (In-memory PDF creation)
def create_pdf_with_reportlab(name, bio, img_path):
    pdf_output = io.BytesIO()  # Create in-memory file
    c = canvas.Canvas(pdf_output, pagesize=letter)
    
    # Set fonts and register a custom font if necessary
    c.setFont("Helvetica-Bold", 16)
    c.setStrokeColor(colors.darkblue)
    
    # Title with Unicode 
    c.drawString(200, 750, "🌟 User Profile 🌟")
    
    # Add Profile Picture 
    if img_path:
        c.drawImage(img_path, 100, 580, width=100, height=100)  
    
    # Add Name
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 500, f"Name: {name}")
    
    # Add Bio 
    c.setFont("Helvetica", 12)
    text_object = c.beginText(100, 470)
    text_object.textLines(f"Bio: {bio}")
    c.drawText(text_object)
    
    # Draw a line for separation
    c.setStrokeColor(colors.black)
    c.line(50, 740, 550, 740)
    
    # Add a stylish footer
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(200, 50, "💻 Created with using Streamlit & ReportLab")
    
    # Save the PDF to the in-memory buffer
    c.save()

    # Move to the beginning of the in-memory file
    pdf_output.seek(0)
    return pdf_output

# Function to get weather data using OpenWeatherMap API
def get_weather(city):
    API_KEY = '1afafe59d9fd1da6746ebe9bede3f00b'
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
    
    # Make the API request
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Convert temperature to Celsius
    }
    
    response = requests.get(BASE_URL, params=params)
    
    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        description = weather['description']
        return f"Temperature: {temperature}°C\nCondition: {description.capitalize()}"
    else:
        return "Sorry, could not fetch weather data. Please try again later."

# Home
if page == "Home":
    st.title("🔰 Python Streamlit Web App")
    st.write("A dynamic website built with Python & Streamlit! 🛡️")

    # Profile Picture Upload
    uploaded_file = st.file_uploader("📷 Upload your profile picture:", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Your Profile Picture", width=200)
    
    # User Input
    name = st.text_input("Enter your name:", "")
    bio = st.text_area("Write a short bio about yourself:")

    if name:
        st.success(f"Hello, {name}! 😁 Welcome to my website.")

    # Generate Profile PDF
    if st.button("📄 Download Profile as PDF"):
        if uploaded_file:
            # Save the uploaded image file temporarily to disk
            img_path = f"temp_image.{uploaded_file.type.split('/')[1]}"
            with open(img_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Generate PDF using ReportLab
            pdf_output = create_pdf_with_reportlab(name, bio, img_path)

            # After successful PDF generation, show success message with download button
            st.success("✅ Profile PDF Generated! You can download it below.")

            # Provide the in-memory file for download as button
            st.download_button(
                label="Download PDF",
                data=pdf_output,
                file_name="profile.pdf",
                mime="application/pdf"
            )

        else:
            st.error("Please upload a profile picture first.")

# AI Chatbot
elif page == "AI Chatbot":
    st.title("🤖 AI Chatbot")
    st.write("Talk to our AI chatbot!")
    user_input = st.text_input("Type your message:", "")
    if user_input:
        response = "Hello! I am your AI chatbot. How can I help you?"
        st.write(f"👻 AI: {response}")

# Contact
elif page == "Contact":
    st.title("📞 Contact Me")
    st.write("You can reach out to me via: **Brooklyn@example.com**")
    
    # 💬 Feedback Form
    feedback = st.text_area("Write your feedback here:")
    if st.button("Submit"):
        st.success("Thank you for your feedback! 👁️‍🗨️")

# Gallery
elif page == "Gallery":
    st.title("🎨 Gallery")
    st.write("Explore my collection of artwork and photography.")
    
    # images 
    st.image(["images/art1.jpg", "images/art2.jpg", "images/art3.jpg"], caption=["Art 1", "Art 2", "Art 3"], width=300)

# To-Do List
elif page == "To-Do List":
    st.title("✅ To-Do List")
    st.write("Manage your tasks and goals.")
    
    # To-Do list
    tasks = st.text_area("Enter your tasks here (separate tasks with a comma):", "")
    if tasks:
        task_list = tasks.split(",")
        st.write("### Your Tasks:")
        for task in task_list:
            st.write(f"- {task.strip()}")

# FAQ
elif page == "FAQ":
    st.title("❓ Frequently Asked Questions")
    st.write("Here are some common questions and answers.")
    
    faqs = {
        "What is this website?": "This is a dynamic website built using Python and Streamlit.",
        "How can I contact you?": "You can contact me via email at Brooklyn@example.com.",
        "What is your mission?": "To create engaging and interactive websites using modern technologies."
    }
    
    for question, answer in faqs.items():
        st.write(f"**{question}**")
        st.write(f"{answer}")

# Weather
elif page == "Weather":
    st.title("🌦️ Weather Information")
    st.write("Get real-time weather updates based on your location.")
    
    city = st.text_input("Enter city name:", "")
    if city:
        weather_info = get_weather(city)
        st.write(f"### Weather in {city}:")
        st.write(weather_info)

# Quote of the Day
quotes = [
    "Have confidence in yourself and everything you are capable of!",
    "Success isn't permanent, and failure isn't the end; it's the bravery to persist that truly matters.",
    "The key to doing remarkable work is to be passionate about what you do.",
    "Dream boldly and embrace the possibility of failure.",
    "Don’t focus on the time; be like the clock. Just keep moving forward."
]
st.sidebar.markdown(f"💎 **Quote of the Day:** {random.choice(quotes)}")

# Footer
st.write("---")
st.write("©️ by Muhammad Ahmed")
