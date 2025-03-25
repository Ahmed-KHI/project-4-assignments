import streamlit as st

# Streamlit Title
st.title("🎭 Mad Libs Story Generator 🎭")

# Taking inputs from the user
name = st.text_input("Enter a name:")
place = st.text_input("Enter a place:")
adjective = st.text_input("Enter an adjective (e.g., funny, scary, amazing):")
verb = st.text_input("Enter a verb (e.g., jump, run, fly):")
animal = st.text_input("Enter an animal:")
food = st.text_input("Enter a food item:")
emotion = st.text_input("Enter an emotion (e.g., happy, sad, excited):")

# Button to generate the story
if st.button("Generate Story"):
    if name and place and adjective and verb and animal and food and emotion:
        # Mad Libs Story
        story = f"""
        Once upon a time, {name} went to {place}. 
        It was a very {adjective} day. Suddenly, {name} saw a {animal} that was trying to {verb}! 
        Shocked and {emotion}, {name} decided to give the {animal} some {food}. 
        And from that day on, they became best friends! 🎉
        """
        st.subheader("✨ Your Mad Libs Story ✨")
        st.write(story)
    else:
        st.warning("⚠️ Please fill in all the fields before generating the story!")