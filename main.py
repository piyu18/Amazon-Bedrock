import streamlit as st 
import  app as demo 

st.title("Hi, This is Chatbot:sunglasses:") # **Modify this based on the title you want in want

#3 LangChain memory to the session cache
st.session_state.memory = demo.demo_memory() #** Modify the import and memory function() attributes initialize the memory

if 'chat_history' not in st.session_state: #see if the chat history hasn't been created yet
    st.session_state.chat_history = [] #initialize the chat history

for message in st.session_state.chat_history: 
    with st.chat_message(message["role"]): 
        st.markdown(message["text"]) 

#6 Enter the details for chatbot input box 
     
input_text = st.chat_input("Powered by Bedrock and LLama 2") # **display a chat input box
if input_text: 
    
    with st.chat_message("user"): 
        st.markdown(input_text) 
    
    st.session_state.chat_history.append({"role":"user", "text":input_text}) 

    chat_response = demo.demo_conversation(input_text=input_text, memory=st.session_state.memory) #** replace with ConversationChain Method name - call the model through the supporting library
    
    with st.chat_message("assistant"): 
        st.markdown(chat_response) 
    
    st.session_state.chat_history.append({"role":"assistant", "text":chat_response}) 