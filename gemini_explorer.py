import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession

project = "gemini-explorer-IDNUM"
#initialize vertexai with google cloud project
vertexai.init(project = project)
#create config with presets entered such as temp=0.4
config = generative_models.GenerationConfig(
    temperature = 0.4
)

# Load model with config
model = GenerativeModel(
    "gemini-pro",
    generation_config = config
)
# start chat session
chat = model.start_chat()

# helper function to display, store and send streamlit messages
def llm_function(chat: ChatSession, query):
    # store response by sending query to chat session
    response = chat.send_message(query)
    # get text output
    output = response.candidates[0].content.parts[0].text

    #tells streamlit to create chat message from output and take output text and apply to chat session
    with st.chat_message("model"):
        st.markdown(output)
    #append into session memory that user made a query
    st.session_state.messages.append({
        "role": "user",
        "content": query
    })
    #append models output
    st.session_state.messages.append({
        "role": "model",
        "content": output
    })
#set title of chat model
st.title("Gemini Explorer")

#initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

    #Display and load to chat history, for every message in the session state memory enumerate through them
for index, message in enumerate(st.session_state.messages):
    #store and send content to gemini
    content = Content(
        #send role we have set from earlier
        role = message["role"],
        #put part we are creating into an array, and create part using text message(output appended from earlier)
        parts = [Part.from_text(message["content"])]
    )
    # Display chat messages from session state, skipping the initial greeting message
    if index != 0:
        # Create a chat message in Streamlits User Interface based on the message role
        with st.chat_message(message["role"]):
            # Render the content of the message as Markdown
            st.markdown(message["content"])
    #pass into chat history so chat model is aware of conversation so it becomes a multi turn conversation
    chat.history.append(content)

# For initial message startup
if len(st.session_state.messages) == 0:
    initial_prompt = "Introduce yourself as ReX, an assistant powered by Google Gemini. You use emojis to be interactive"
    llm_function(chat, initial_prompt)

    # For capture user input
query = st.chat_input("Gemini Explorer")
#if input
if query:
    #send role
    with st.chat_message("user"):
        #add to session
        st.markdown(query)
    #call helper function
    llm_function(chat, query)
