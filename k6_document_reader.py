from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.llms import OpenAI, HuggingFaceHub
import warnings
import os
os.environ['OPENAI_API_KEY'] = "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"
warnings.simplefilter('ignore')
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
#Simple LLM call with generic knowledge
# llm = OpenAI()
llm = HuggingFaceHub(repo_id = "google/flan-t5-large")
# query="What are the Linux commands to install K6 ?"
query = "What is the currency of India ? Explain the history."
print(llm(query))

#LLM call with pdf as reference
combined_text = ""
data = PdfReader("K6_Installation.pdf")
for i,page in enumerate(data.pages):
    text = page.extract_text()
    if text:
        combined_text += text

#Converting the text into vectores
# text_splitter = CharacterTextSplitter(
#     separator="\n",
#     chunk_size=200,
#     chunk_overlap=20,
#     length_function=len
# )
#
# final_Data = text_splitter.split_text(combined_text)
# embeddings = OpenAIEmbeddings()
# document_Search = FAISS.from_texts(final_Data, embeddings)
# chain = load_qa_chain(llm, chain_type="stuff")
# docs = document_Search.similarity_search(query)
# res = chain.run(input_documents=docs, question=query)
# print(res)