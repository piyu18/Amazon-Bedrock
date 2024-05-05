import os
from langchain_community.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from dotenv import load_dotenv
# Load environment variables
load_dotenv()

def demo_chatbot():
    demo_llm = Bedrock(
       credentials_profile_name='default',
       model_id='meta.llama2-70b-chat-v1',
       streaming=True,
       callbacks=[StreamingStdOutCallbackHandler()],
       model_kwargs= {
        "temperature": 0.9,
        "top_p": 0.5,
        "max_gen_len": 512})
    return demo_llm
    
#2b Test out the LLM with Predict method
   # return demo_llm.predict(input_text)
#response = demo_chatbot('what is the temprature in london like ?')
#print(response)

#3 Create a Function for ConversationBufferMemory (llm and max token limit)
def demo_memory():
    llm_data=demo_chatbot()
    memory = ConversationBufferMemory(llm=llm_data, max_token_limit= 512)
    return memory

#4 Create a Function for Conversation Chain - Input text + Memory
def demo_conversation(input_text,memory):
    llm_chain_data = demo_chatbot()
    llm_conversation= ConversationChain(llm=llm_chain_data,memory= memory,verbose=True)

#5 Chat response using Predict (Prompt template)
    chat_reply = llm_conversation.predict(input=input_text)
    return chat_reply
