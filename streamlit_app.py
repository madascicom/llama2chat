import streamlit as st
from llamaapi import LlamaAPI
import json


st.title('🦙 Llama Chat Test')

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
    
llama = LlamaAPI('Llama_API_Token')

def get_bot_response(prompt):
    response = llama.generate(prompt, max_tokens=100, temperature=0.5, top_p=0.3)
    return response.text

user_input = get_user_input() 

if user_input:
    output = get_bot_response(user_input)
    
    st.session_state.generated.append({"role":"user", "content":user_input})
    st.session_state.generated.append({"role":"assistant", "content":output})
