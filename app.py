import sys
import streamlit as st
from src.compgenerator.compgenerator import review_chain
from src.compgenerator.utils import preview, generate_txt, generate_pdf_content
from pathlib import Path
import json
from src.compgenerator.logger import logging
from src.compgenerator.exception import CustomException

try:
    # Load response JSON
    path = Path("response.json")

    with open(path, 'r') as f:
        RESPONSE_JSON = json.load(f)

    # Set page title
    st.title("CompreHive 📝 ")
    st.markdown("**Generate comprehension and questions effortlessly!** ✨")

    # User input form
    with st.form("user input"):
        # Input box for user's topic
        topic = st.text_input("Enter your topic for the comprehension here")

        # Select box for size of the comprehension
        no_words_options = ['200-300', '300-400', '400-500', '>500']
        no_words = st.selectbox(label="Select size of the comprehension (in words)", options=no_words_options)

        # Dropdown menu for difficulty level
        difficulty_options = ["Easy", "Medium", "Hard", "Expert"]
        difficulty = st.selectbox("Difficulty Level", options=difficulty_options)

        # Input boxes for number of questions
        mcq_count = st.number_input("Number of MCQs", min_value=2, max_value=10, step=1, value=2)
        saq_count = st.number_input("Number of SAQs", min_value=2, max_value=10, step=1, value=2)
        laq_count = st.number_input("Number of LAQs", min_value=1, max_value=5, step=1, value=1)

        # Submit button
        if st.form_submit_button("Create Comprehension"):
            st.session_state.FormSubmitter = "user input-Create Comprehension"

    if "FormSubmitter" in st.session_state and st.session_state.FormSubmitter == "user input-Create Comprehension":
        # Generate comprehension and questions
        @st.cache_data
        def generate_comprehension(topic, difficulty, laq_count, mcq_count, saq_count, no_words):
            return review_chain.invoke({'RESPONSE_JSON': RESPONSE_JSON,
                                        'difficulty': difficulty,
                                        'la_no': laq_count,
                                        'mcq_no': mcq_count,
                                        'sa_no': saq_count,
                                        'topic': topic,
                                        'words': no_words})

        response = generate_comprehension(topic, difficulty, laq_count, mcq_count, saq_count, no_words)

        # Display preview
        preview(topic, response)

        # Generate text and PDF content
        text = generate_txt(topic, response)
        pdf = generate_pdf_content(topic, response)

        # Add spacing between items
        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2= st.columns([1,2])
        # Create a download button for text file
        if col1.download_button("Download Text File", data=text, file_name="comprehension.txt"):
                st.session_state.btn_click_text = True

        # Create a download button for PDF file
        if col2.download_button("Download PDF File", data=pdf, file_name="comprehension.pdf"):
                st.session_state.btn_click_pdf = True

except Exception as e:
    # Log the exception
    logging.info(e)
    # Error message to show in app
    st.header("Error 💥 try 💫 reloading the app!")
    # Raise custom exception
    raise CustomException(e, sys)


footer = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

a:link , a:visited {
    color: blue;
    background-color: transparent;
    text-decoration: underline;
}

a:hover, a:active {
    color: red;
    background-color: transparent;
    text-decoration: underline;
}

.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #F0F0F0;;
    color: black;
    text-align: left;
    padding:5px; 
    font-family: 'Roboto', sans-serif; 
}

.footer p {
    font-weight: bold;
}
</style>
<div class="footer">
<p>Curiosity ignited by AI 🚀: Your questions 🤔, our creation 🎨 - Crafted by Team CompreHive</p>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)
