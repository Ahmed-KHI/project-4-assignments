import streamlit as st

# 🎯 App Title
st.title("💪 Advanced BMI Calculator")

# 📌 Theme Selection
theme = st.radio("🎨 Select Theme:", ["Light", "Dark"])
if theme == "Dark":
    st.markdown("""
        <style>
            body { background-color: #1e1e1e; color: white; }
        </style>
    """, unsafe_allow_html=True)

# 📌 User Inputs
age = st.number_input("🎂 Enter your age:", min_value=1, step=1)
gender = st.radio("🚻 Select your gender:", ["Male", "Female"])
weight = st.number_input("⚖️ Enter your weight (kg):", min_value=1.0, step=0.1)
height = st.number_input("📏 Enter your height (m):", min_value=0.5, step=0.01)

# 🧮 BMI Calculation
if height > 0:
    bmi = weight / (height ** 2)
    st.subheader(f"📊 Your BMI: **{bmi:.2f}**")

    # 🎨 Health Status & Ideal Weight
    if bmi < 18.5:
        st.warning("⚠️ Underweight")
        st.info("🍽️ Eat more nutritious food!")
    elif 18.5 <= bmi < 24.9:
        st.success("✅ Normal weight")
        st.info("🏃 Keep up the good work!")
    elif 25 <= bmi < 29.9:
        st.warning("⚠️ Overweight")
        st.info("🏋️ Try exercising regularly!")
    else:
        st.error("❌ Obese")
        st.info("🥗 Maintain a healthy diet & exercise.")
    
    # 📌 Ideal Weight Calculation (Based on Height)
    min_ideal_weight = 18.5 * (height ** 2)
    max_ideal_weight = 24.9 * (height ** 2)
    st.write(f"🔹 Your ideal weight range: **{min_ideal_weight:.1f} kg - {max_ideal_weight:.1f} kg**")
else:
    st.info("🔹 Please enter a valid height.")

# 🕘 BMI History
if "bmi_history" not in st.session_state:
    st.session_state.bmi_history = []

if height > 0:
    if st.button("📌 Save BMI Record"):
        st.session_state.bmi_history.append(bmi)
        st.success("✅ BMI record saved!")

if st.session_state.bmi_history:
    st.write("📜 BMI History:")
    st.write(st.session_state.bmi_history)

# 🔄 Reset Button
if st.button("🔄 Reset"):
    st.session_state.bmi_history = []
    st.rerun()