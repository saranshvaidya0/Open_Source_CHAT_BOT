import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Page config
st.set_page_config(page_title="AI Notes Generator", layout="wide")

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []

# Sidebar (History)
st.sidebar.title("Prompt History")

if st.session_state.history:
    for i, item in enumerate(st.session_state.history[::-1]):
        if st.sidebar.button(item["topic"], key=f"history_{i}"):
            st.session_state.selected = item
else:
    st.sidebar.write("No history yet")

# Clear history button
if st.sidebar.button("Clear History"):
    st.session_state.history = []

# Main UI
st.title("AI Notes Generator")
st.write("Enter a topic and generate structured notes")

topic = st.text_input("Enter Topic")

# Generate Notes                                                                                                                                                                    
if st.button("Generate Notes"):
    if topic.strip():
        with st.spinner("Generating..."):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "user",
                        "content": f"Generate structured notes on {topic} with headings, bullet points, and examples."
                    }
                ]
            )

            notes = response.choices[0].message.content

            # Save to history
            st.session_state.history.append({
                "topic": topic,
                "notes": notes
            })

            st.session_state.selected = {
                "topic": topic,
                "notes": notes
            }

# Display selected or latest notes
if "selected" in st.session_state:
    st.subheader(f"Notes on: {st.session_state.selected['topic']}")
    st.write(st.session_state.selected["notes"])
