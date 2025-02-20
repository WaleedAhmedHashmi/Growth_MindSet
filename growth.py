import streamlit as st



challenges = {
    "Day 1": {
        "prompt": "What are your goals for the next month?",
        "exercise": "Write down three specific goals and why they're important to you."
    },
    "Day 2": {
        "prompt": "What's one thing you've been putting off?",
        "exercise": "Write down the reasons why you've been putting it off, and then brainstorm three ways to take action on it today."
    }
    
}

# st.set_page_config(page_title="Growth Mindset", layout='wide')
st.title('Daily Challenges ')
st.subheader('Track and overcome your daily challenges with motivation')
# st.write('Welcome to the growth mindset challenge! This challenge is designed to help you cultivate a growth mindset and achieve your goals.')


day = st.selectbox("Choose a day", list(challenges.keys()))
st.write(challenges[day]["prompt"])
st.write(challenges[day]["exercise"])
    
st.header("Set Your Learning Goal ")
learning_goal = st.text_input("What new skill or concept do you want to develop?")
    
if st.button("Submit Goal"):
        if learning_goal:
            st.success("Great choice! Stay consistent and keep learning: ")
        else:
            st.warning("Please enter a goal before submitting.")
    
st.header("Reflect on Your Growing Skills")
reflection = st.text_area("What challenges have you faced recently and how did you overcome them?")
    
if st.button("Share Reflection"):
        if reflection:
            st.success("Reflection saved! Keep embracing challenges and growing.")
        else:
            st.warning("Please enter your reflection before submitting.")
    
st.header("Stay Positive & Motivated ")
if st.button("Get Motivation"):
        st.info("A strong, positive self-image is the best possible preparation for success.")



