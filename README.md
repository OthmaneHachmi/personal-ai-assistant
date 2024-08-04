# Personal AI Assistant

This project is a web-based personal AI assistant that leverages the Groq API for text generation . The assistant allows users to generate responses based on text prompts.

## Features
- **Text Generation:** Generate responses to user prompts using the Groq API.

## Installation

### Prerequisites

- Python 3.6 or higher
- `pip` (Python package installer)

### Clone the Repository

```sh
git clone https://github.com/OthmaneHachmi/personal-ai-assistant.git
cd personal-ai-assistant
```
### Install Dependencies
Create a virtual environment and install the required packages:

```sh
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
### Set Up Environment Variables
Create a .env file with the following content:

```sh
GROQ_API_KEY=your_groq_api_key
```
Replace your_groq_api_key with your actual API key from Groq.

### Running the Application
To start the application, use the following command:
```sh
python user_interface.py
```
