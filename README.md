<a id="top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="https://github.com/Pramit726/CompreHive/assets/149934842/da9d2975-76c8-4a3f-ac06-4984bc100d82" alt="Logo" width="80" height="80">
  </a>
  <h3 align="center">CompreHive</h3>

  <p align="center">
    Enhance understanding effortlessly with customized reading passages and questions
    <br />
    <a href="https://github.com/Pramit726/CompreHive/assets/149934842/32865eac-efb9-4448-840f-1d741f73ac41">View Demo</a>
    ·
    <a href="https://github.com/Pramit726/CompreHive/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/Pramit726/CompreHive/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
## Table of Contents

1. [Project Overview](#project-overview)
2. [Project Demo](#project-demo)
3. [Required API Keys](#required-api-keys)
4. [Project Setup](#project-setup)
5. [Deployment on AWS](#deployment-on-aws)
6. [Dependencies](#dependencies)
7. [Author](#author)

<!-- PROJECT OVERVIEW -->
## Project Overview

<div align="justify"> 
This Streamlit application, powered by Google GEMINI 1.5 Pro, generates comprehension exercises based on user input of topics, keywords, and desired question types. Users have the flexibility to specify the number of multiple-choice, short-answer, and long-answer questions according to their preferences. Moreover, users can conveniently download the generated content in the form of text and PDF files, enhancing accessibility and offline usage.
</div>
</br>

<div align="justify"> 
The application incorporates robust logging and exception handling mechanisms to ensure smooth operation and error detection. Additionally, a setup module is implemented to streamline the installation process and manage dependencies effectively.
</div>
</br>

<div align="justify"> 
Deployed on Amazon Web Services (AWS), the application offers easy access and utilization for users. AWS also ensures scalability, allowing the application to handle varying user loads seamlessly. 
</div>

<!-- PROJECT DEMO -->
## Project Demo

- **App Recording**



https://github.com/Pramit726/CompreHive/assets/149934842/32865eac-efb9-4448-840f-1d741f73ac41



<br/>

- **Text File Screenshot**

<!-- ![App Screenshot](https://github.com/Pramit726/CompreHive/assets/149934842/8acc6b76-40f8-4137-9b74-9413ea2af5de) --> 
<img src="https://github.com/Pramit726/CompreHive/assets/149934842/8acc6b76-40f8-4137-9b74-9413ea2af5de" alt="Text-screenshot" width="500" height="700">

<br/>
<br/>

- **PDF File Screenshot**

<!-- ![App Screenshot](https://github.com/Pramit726/CompreHive/assets/149934842/fa5c1253-155c-4dbb-b499-032628fe7cab)--> 
<img src="https://github.com/Pramit726/CompreHive/assets/149934842/fa5c1253-155c-4dbb-b499-032628fe7cab" alt="PDF-screenshot" width="500" height="874">

<!-- REQUIRED API KEYS -->
## Required API Keys

This project requires two API keys:

- **Google API key:** Required for accessing the GEMINI 1.5 Pro model.
- **LangChain API key:** Required for LangSmith tracking.

LangSmith facilitates usage tracking and provides valuable insights into user behavior through seamless integration. The screenshot below illustrates a sample view of CompreHive usage data within the LangSmith platform.

<!-- !![Screenshot 2024-05-16 101226](https://github.com/Pramit726/CompreHive/assets/149934842/7e25da75-2c49-4f7c-a78e-6a484748aca3)--> 

![App Screenshot](https://github.com/Pramit726/CompreHive/assets/149934842/7e25da75-2c49-4f7c-a78e-6a484748aca3)
<br/>
<br/>

Ensure that you obtain these API keys before running the project.

<!-- PROJECT SETUP -->
## Project Setup

**Clone this GitHub repository**

```bash
(base)$: git clone https://github.com/Pramit726/CompreHive.git
```

**Go to the project directory**

```bash
(base)$: cd CompreHive
```

**Configure environment**

- Create the conda environment

```bash
(base)$: conda  create -p venv python==3.10 -y
```

- Activate the environment

```bash
(base)$: conda activate venv
```
- Install the required dependencies

```bash
(venv)$: pip install -r requirements.txt
```
**Run it**

```bash
(venv)$: streamlit run app.py
```

As soon as you run the script, a local Streamlit server will spin up, and your app will open in a new tab in your default web browser.

Or you can navigate to ``http://localhost:8501.``

<!-- DEPLOYMENT ON AWS-->
## Deployment on AWS

**Step 1**

First login to the AWS: https://aws.amazon.com/console/

**Step 2**

Search about EC2 in the services section.

**Step 3**

Configure the Ubuntu machine.

**Step 4**

Launch the instance.

**Step 5**

Do the port mapping to this port: 8501

**Step 6**

Run the following commands.

```bash
sudo apt update
```

```bash
sudo apt-get update
```
```bash
sudo apt upgrade -y
```
```bash
sudo apt install git curl unzip tar make sudo vim wget -y
```
```bash
git clone https://github.com/Pramit726/CompreHive.git
```

```bash
cd CompreHive
```

```bash
sudo apt install python3-pip
```

```bash
sudo apt install python3-venv
```

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

```bash
pip3 install -r requirements.txt
```

**If you want to add the API keys**

- Create .env file in the AWS server using  touch .env

- Next write vi .env

- Press i 

- Copy API keys and paste it

- Press : , then wq! and hit enter

**Step 7**
```bash
#Temporary running
python3 -m streamlit run app.py
```

```bash
#Permanent running
nohup python3 -m streamlit run app.py
```
<!-- DEPENDENCIES -->
## Dependencies

- langchain
- langchain-core
- langchain-google-genai
- python-dotenv
- reportlab
- streamlit

<!-- AUTHOR -->
## Author
**Pramit De**
- <img src="https://github.com/tandpfun/skill-icons/blob/main/icons/Github-Dark.svg" alt="GitHub" width="20"/> [Pramit726](https://github.com/Pramit726)
- <img src="https://github.com/tandpfun/skill-icons/blob/main/icons/Gmail-Dark.svg" alt="Email" width="20"/> pramitde726@gmail.com / pramit.de.cse.2021@tint.edu.in
- Department of CSE, Techno International New Town, West Bengal, India

© 2024 CompreHive by Pramit De

<p align="right">
    <a href="#top">Back to Top</a>
</p>


















