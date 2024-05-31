import sys
from src.compgenerator.logger import logging
from src.compgenerator.exception import CustomException
from dotenv import load_dotenv
import os
from langchain_core.prompts.prompt import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from operator import itemgetter

try:
    # Load environment variables from .env file
    load_dotenv()

    # Set the GOOGLE_API_KEY environment variable to the value retrieved from .env file
    os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
    ## Langsmith tracking
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0.5)  # Creating ChatGoogleGenerativeAI instance

    # Template for generating comprehension instructions
    generate_instruction = """
    You are an expert comprehension generator\
    Given a specific {topic} your task is to\  
    generate a comprehension passage within strictly following the given word range of {words} words \
    keeping in mind the difficulty level {difficulty}
    Next you have to have to generate MCQS, short answer type and long answer type questions.
    The number of questions for MCQ will be {mcq_no},do not generate if 0\
    for short answer type{sa_no}, do not generate if 0 and\
    for long answer type{la_no},do not generate if 0.
    Provide the demo answers for all the generated questions of MCQ, short answer and long answer questions at the end.
    The long type question demo answers should be of minimimum 100 words\
    Provide the output in the given format\
    There should not be any marker just the passage and the questions\
    {RESPONSE_JSON}
    """

    # Creating prompt template for generating instructions
    generation_prompt = PromptTemplate(
        input_variables=['topic', 'words', 'difficulty', 'mcq_no', 'sa_no', 'la_no', 'RESPONSE_JSON'],
        template=generate_instruction
    )

    output_parser = StrOutputParser()  # Creating output parser instance

    # Creating chain for generating comprehension instructions
    chain_generation = generation_prompt | llm | output_parser

    # Template for reviewing comprehension
    review_instruction = """
    As an expert in English grammar and writing, your task is to assess a comprehension passage{response}\
    The passage provided is {words} words long and pertains to the topic of {topic}\
    Your evaluation should include an assessment of the passage's difficulty level, as specified {difficulty}\
    Thoroughly check the number of words in the passage as mentioned {words} words  is followed correctly\
    Furthermore, you are required to evaluate multiple-choice questions, short-answer questions, and long-answer questions embedded within the passage\
    If any of the questions do not align with the cognitive and analytical abilities expected of the students, you must suggest changes to ensure they are suitable\
    Additionally, you are to evaluate the provided answers to the questions, ensuring they are accurate and appropriate.
    Please ensure that the output consists solely of the updated comprehension passage and the questions along with their answers\
    as per the given format {RESPONSE_JSON}\
    Ensure that in the {response},commprehension passage and the demo answers does not contain unnecessary line gaps  \
    Also  make sure that the dictionary is enclosed with quotes\
    """

    # Creating prompt template for reviewing comprehension
    review_template = PromptTemplate(
        input_variables=['topic', 'words', 'difficulty', 'response', 'RESPONSE_JSON'],
        template=review_instruction
    )

    # Creating chain for reviewing comprehension
    review_chain = (
        {"response": chain_generation, "difficulty": itemgetter("difficulty"), "topic": itemgetter("topic"),
         "words": itemgetter("words"), "RESPONSE_JSON": itemgetter("RESPONSE_JSON")}
        | review_template
        | llm
        | StrOutputParser()
    )

except Exception as e:
    logging.info(e)  # Logging the exception
    raise CustomException(e, sys)  # Raising CustomException 
