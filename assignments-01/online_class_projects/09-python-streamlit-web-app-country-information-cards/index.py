import streamlit as st
import requests

# App title
st.title("🌍 Country Information Cards")

# User input for country name
country = st.text_input("Enter Country Name", "")

if country:
    # Fetch country data from API
    url = f"https://restcountries.com/v3.1/name/{country}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()[0]  # First result
        
        # Extracting details
        country_name = data.get("name", {}).get("common", "N/A")
        capital = data.get("capital", ["N/A"])[0]
        population = data.get("population", "N/A")
        region = data.get("region", "N/A")
        currency = list(data.get("currencies", {}).keys())[0] if "currencies" in data else "N/A"
        language = list(data.get("languages", {}).values())[0] if "languages" in data else "N/A"
        flag_url = data.get("flags", {}).get("png", "")

        # Display country details
        st.image(flag_url, width=300, caption=f"Flag of {country_name}")
        st.subheader(f"📍 {country_name}")
        st.write(f"**Capital:** {capital}")
        st.write(f"**Population:** {population:,}")
        st.write(f"**Region:** {region}")
        st.write(f"**Currency:** {currency}")
        st.write(f"**Language:** {language}")
    
    else:
        st.error("⚠️ Country not found! Please check the spelling.")