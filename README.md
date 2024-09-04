# Gemini Explorer
## Overview
Create a Streamlit chat interface integrating Google's advanced language model, Gemini, for an accessible exploration of large language model applications. The goal is to provide an accessible platform for exploring and demonstrating the capabilities of advanced language models. This project Gemini Explorer is a chatbot application built using [Google Vertex AI](https://cloud.google.com/vertex-ai) and [Streamlit](https://streamlit.io/). The application integrates the Gemini Pro model from Vertex AI to facilitate dynamic, interactive conversations, providing a seamless chat experience.

## Features
- **Interactive Chat:** Engage with the chatbot, powered by Vertex AI's Gemini Pro model.
- **Multi-turn Conversations:** The chatbot maintains context over multiple conversation turns.
- **Customizable Configuration:** Configure settings like temperature to adjust the model's responses.
- **Streamlit UI:** User-friendly and responsive chat interface built with Streamlit.

## Installation

### Prerequisites
- [Python 3.8+](https://www.python.org/downloads/)
- [Streamlit](https://docs.streamlit.io/)
- [Vertex AI SDK](https://cloud.google.com/vertex-ai?hl=en&authuser=1)
- [Google Cloud SDK](https://cloud.google.com/sdk?hl=en)

### Setup
1. **Clone the repository:**
```bash
git clone https://github.com/RohitSiva2004/RadicalAI-Gemini_Explorer
```
2. **Navigate to the project directory:**
```bash
cd gemini-explorer
```

3. **Install the required packages:**
```bash
pip install streamlit
```

4. **Set up Google Cloud:**
- Ensure that your Google Cloud project is set up with Vertex AI enabled and all recommended API's enabled.
- Authenticate using Google Cloud SDK and log into your Cloud project's account:
```bash
gcloud auth application-default login
```
- Initialize Vertex AI with your Google Cloud project ID in the script(refer to Billing for project-ID).

### **5. Set Up a Virtual Environment**
It is always recommended to create a virtual environment to test your Python projects. This helps keep your project dependencies isolated. If you have venv installed, create a new environment with:.
```bash
python -m venv .venv
```

Activate the virtual environment:

Windows (PowerShell):
```bash
.venv\Scripts\Activate.ps1
```

Windows (CMD):
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

## Usage

### **1.Run the Streamlit application**
```bash
streamlit run gemini_explorer.py
```
### **2.Accessing the Application**
When streamlit run gemini_explorer.py is run in the terminal, you can begin accessing the chat model at http://localhost:8501.

### **3.Interact with the chat model**
- Enter your queries in the input box.
- The chatbot will respond based on the context and configuration.

## Configuration
You can adjust the following configurations:
- Temperature: Controls the randomness of responses (default: 0.4).

## Example
Here's a sample interaction with the Gemini Explorer chatbot:

```bash
User: Hello, who are you?
Bot: Hello! I am ReX, an assistant powered by Google Gemini. How can I assist you today? 😊
```
![image](https://github.com/user-attachments/assets/b7a66ff7-ce0c-4c19-b691-0bb01868136b)

## How the Program Works

### 1. Vertex AI Initialization
The program begins by initializing Vertex AI with your Google Cloud project. This setup allows the application to communicate with Google's Vertex AI services, specifically the **Gemini Pro** model.

### 2. Configuration Setup
A configuration is created using Vertex AI's `GenerationConfig` class. In this case, the `temperature` parameter is set to 0.4, which controls the randomness of the model's responses. A lower temperature value results in more focused and deterministic answers, while a higher value makes the responses more creative and varied.

### 3. Loading the Model
The **Gemini Pro** model is loaded with the specified configuration. This model powers the chatbot's responses, making it capable of handling dynamic, multi-turn conversations.

### 4. Starting a Chat Session
A chat session is initiated with the model. This session maintains the conversation's context, allowing the chatbot to remember previous messages and provide coherent responses over multiple turns.

### 5. Handling User Input and Displaying Responses
The `llm_function` is responsible for managing the interaction between the user and the chatbot:
- When a user sends a query, the function passes it to the chat session, where the model generates a response.
- The response is then displayed in the Streamlit interface using Markdown, providing a clean and readable chat format.
- The user's query and the model's response are stored in the session state to keep track of the conversation history.

### 6. Session Memory and History
The program maintains a session memory using Streamlit's `st.session_state`. This memory holds all previous user queries and model responses, allowing the chatbot to reference past interactions during the conversation.

The conversation history is updated with each new interaction. This history is essential for multi-turn conversations, as it enables the chatbot to respond contextually based on the entire conversation, not just the latest query.

### 7. Initial Prompt
When the chat session begins, the chatbot introduces itself as **ReX**, a friendly assistant powered by Google Gemini, and uses emojis to make the interaction more engaging. This initial message is pre-configured and helps set the tone for the conversation.

### 8. User Interface
The entire chat interface is built using Streamlit, a Python framework for creating interactive web applications. The user interacts with the chatbot through a simple input box, and the responses are rendered directly on the web page.

### 9. Handling User Queries
When a user inputs a query:
- The input is sent to the `llm_function`, which processes it and generates a response.
- The response is displayed in the chat interface, and the conversation continues with the model aware of all prior exchanges, allowing for a coherent multi-turn dialogue.

### 10. Multi-Turn Conversations
The chat session supports multi-turn conversations, meaning the model can maintain context across multiple user queries. For example, if you ask the chatbot a follow-up question, it will remember the context from the previous interaction and provide a relevant response.

### 11. Running the Program
To run the program, execute the Streamlit app with the `streamlit run app.py` command. This will start the chatbot interface in your web browser, where you can begin interacting with **Gemini Explorer**.

### Summary
In summary, **Gemini Explorer** leverages Google Vertex AI's powerful **Gemini Pro** model to create an engaging and intelligent chatbot. The program manages user interactions, stores conversation history, and provides a dynamic and responsive chat experience, all within a Streamlit-powered user interface.


