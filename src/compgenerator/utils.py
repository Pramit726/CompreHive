import sys
from src.compgenerator.logger import logging
from src.compgenerator.exception import CustomException
import streamlit as st
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import base64
import json

try:
    # Function to preview comprehension
    def preview(topic, response):
        st.markdown("## Topic")
        st.write(topic)
        
        # Remove ```json and ``` if present
        response = response.strip().replace("```json", "").replace("```", "")
        # Convert response string to dictionary
        response_dict = eval(response)
        
        st.write("### Comprehension Passage")
        st.write(response_dict["comprehension_passage"])

        
        if (len(response_dict["mcqs"]) != 0):
            st.markdown("### Multiple Choice Questions")
            for mcq in response_dict["mcqs"]:
                st.write("**Question:**", mcq["question"])
                st.write("**Options:**", "\n", mcq["options"])
                st.write("**Correct Answer:**", mcq['options'][mcq['answer_key']])

        if (len(response_dict["short_answer_questions"]) != 0):
            st.markdown("### Short Answer Questions")
            for short_answer in response_dict["short_answer_questions"]:
                st.write("**Question:**", short_answer["question"])
                st.write("**Demo Answer:**", short_answer["demo_answer"])

        if (len(response_dict["long_answer_questions"]) != 0):
            st.markdown("### Long Answer Questions")
            for long_answer in response_dict["long_answer_questions"]:
                st.write("**Question:**", long_answer["question"])
                st.write("**Demo Answer:**", long_answer["demo_answer"])

    # Function to generate text content
    def generate_txt(topic, response):
        content = "## Topic\n"
        content += topic + "\n\n"

        # Remove ```json and ``` if present
        response = response.strip().replace("```json", "").replace("```", "")
        # Convert response string to dictionary
        response_dict = eval(response)
        
        content += "### Comprehension Passage\n"
        content += response_dict["comprehension_passage"] + "\n\n"

        if response_dict["mcqs"]:
            content += "### Multiple Choice Questions\n"
            for mcq in response_dict["mcqs"]:
                content += "**Question:** " + mcq["question"] + "\n"
                options_str = "\n".join(mcq["options"])  # Convert list to string
                content += "**Options:**\n" + options_str + "\n"
                content += "**Correct Answer:** " + str(mcq['options'][mcq['answer_key']]) + "\n\n"  # Convert answer_key to string

        if response_dict["short_answer_questions"]:
            content += "### Short Answer Questions\n"
            for short_answer in response_dict["short_answer_questions"]:
                content += "**Question:** " + short_answer["question"] + "\n"
                content += "**Demo Answer:** " + short_answer["demo_answer"] + "\n\n"

        if response_dict["long_answer_questions"]:
            content += "### Long Answer Questions\n"
            for long_answer in response_dict["long_answer_questions"]:
                content += "**Question:** " + long_answer["question"] + "\n"
                content += "**Demo Answer:** " + long_answer["demo_answer"] + "\n\n"

        return content

    # Function to generate PDF content
    def generate_pdf_content(topic, response):
        # Create PDF content
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()

        # Content for PDF
        pdf_content = []

        # Add topic to PDF
        topic_text = "<b>Topic:</b> {}\n\n".format(topic)
        pdf_content.append(Paragraph(topic_text, styles["Title"]))

        # Remove ```json and ``` if present
        response = response.strip().replace("```json", "").replace("```", "")
        # Convert response string to dictionary
        response_dict = eval(response)
        
        # Add comprehension passage to PDF
        passage_text = "<b>Comprehension Passage:</b> {}\n\n".format(response_dict["comprehension_passage"])
        pdf_content.append(Paragraph(passage_text, styles["Normal"]))

        # Add multiple choice questions to PDF
        if response_dict["mcqs"]:
            mcq_text = "<b>Multiple Choice Questions:</b>\n\n"
            pdf_content.append(Paragraph(mcq_text, styles["Heading2"]))
            for mcq in response_dict["mcqs"]:
                mcq_question = "<b>Question:</b> {}\n".format(mcq["question"])
                mcq_options = "<b>Options:</b><br />"
                for option in mcq["options"]:
                    mcq_options += "- {}<br />".format(option)
                
                mcq_answer_key = "<b>Correct Answer:</b> {}\n\n".format(mcq['options'][mcq['answer_key']])
                pdf_content.append(Paragraph(mcq_question, styles["Normal"]))
                pdf_content.append(Paragraph(mcq_options, styles["Normal"]))

        # Add short answer questions to PDF
        if response_dict["short_answer_questions"]:
            saq_text = "<b>Short Answer Questions:</b>\n\n"
            pdf_content.append(Paragraph(saq_text, styles["Heading2"]))
            for saq in response_dict["short_answer_questions"]:
                saq_question = "<b>Question:</b> {}\n".format(saq["question"])
                saq_demo_answer = "<b>Demo Answer:</b> {}\n\n".format(saq["demo_answer"])
                pdf_content.append(Paragraph(saq_question, styles["Normal"]))

        # Add long answer questions to PDF
        if response_dict["long_answer_questions"]:
            laq_text = "<b>Long Answer Questions:</b>\n\n"
            pdf_content.append(Paragraph(laq_text, styles["Heading2"]))
            for laq in response_dict["long_answer_questions"]:
                laq_question = "<b>Question:</b> {}\n".format(laq["question"])
                laq_demo_answer = "<b>Demo Answer:</b> {}\n\n".format(laq["demo_answer"])
                pdf_content.append(Paragraph(laq_question, styles["Normal"]))

        # Add line breaks in the PDF content
        pdf_content.append(Spacer(1, 12))  
        pdf_content.append(Spacer(1, 12))  

        # Adding answers
        mcq_ans_head = "<b>Multiple Choice Questions Answers:</b>\n\n"
        pdf_content.append(Paragraph(mcq_ans_head, styles["Heading2"]))
        for mcq in response_dict["mcqs"]:
            mcq_answer_key = "<b>Correct Answer:</b> {}\n\n".format(mcq['options'][mcq['answer_key']])
            pdf_content.append(Paragraph(mcq_answer_key, styles["Normal"]))

        sa_ans_head = "<b>Short Answer Questions Answers:</b>\n\n"
        pdf_content.append(Paragraph(sa_ans_head, styles["Heading2"]))
        for saq in response_dict["short_answer_questions"]:
            saq_demo_answer = "<b>Demo Answer:</b> {}\n\n".format(saq["demo_answer"])
            pdf_content.append(Paragraph(saq_demo_answer, styles["Normal"]))
        
        la_ans_head = "<b>Long Answer Questions Answers:</b>\n\n"
        pdf_content.append(Paragraph(la_ans_head, styles["Heading2"]))
        for laq in response_dict["long_answer_questions"]:
            laq_demo_answer = "<b>Demo Answer:</b> {}\n\n".format(laq["demo_answer"])
            pdf_content.append(Paragraph(laq_demo_answer, styles["Normal"]))

        # Build PDF
        doc.build(pdf_content)
        
        # Get PDF content as bytes
        pdf_bytes = buffer.getvalue()
        buffer.close()
        
        return pdf_bytes

    # Function to create download link
    def create_download_link(file_content, file_name, link_text):
        if isinstance(file_content, str):
            file_content = file_content.encode("utf-8")
        b64 = base64.b64encode(file_content).decode()
        href = f'<a href="data:application/pdf;base64,{b64}" download="{file_name}">{link_text}</a>'
        return href

except Exception as e:
    # Log the exception
    logging.exception(e)
    # Raise custom exception
    raise CustomException(e, sys)