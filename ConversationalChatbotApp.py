import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import ( AIMessage, HumanMessage, SystemMessage )


st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("Hi, I am your ChatGPT")
chat = ChatOpenAI(temperature=0)

if "sessionMessages" not in st.session_state:
    st.session_state.sessionMessages = [
        SystemMessage(content="You are a helpful assistant")
    ]

def load_answer(question):
    st.session_state.sessionMessages.append(HumanMessage(content=question))
    ai_answer = chat(st.session_state.sessionMessages)
    st.session_state.sessionMessages.append(AIMessage(content=ai_answer.content))
    return ai_answer.content

def get_question():
    input_text = st.text_input("You: ", key=input)
    return input_text

user_input = get_question()
submit = st.button("Generate")

if submit:
    answer = load_answer(user_input)
    st.subheader("Answer: ")
    st.write(answer, key=1)

