from dotenv import find_dotenv, load_dotenv
from langchain.document_loaders import PyPDFLoader
import os
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

loader = UnstructuredPDFLoader("../Result/ChungminLee_Resume.pdf")
pages = loader.load_and_split()
_ = load_dotenv(find_dotenv())  # read local .env file
embeddings = OpenAIEmbeddings(openai_api_key = os.getenv('OPENAI_API_KEY'))
docsearch = Chroma.from_documents(pages, embeddings).as_retriever()

query = "Who is Chungmin Lee?"
docs = docsearch.get_relevant_documents(query)

chain = load_qa_chain(ChatOpenAI(temperature=0), chain_type="stuff")
output = chain.run(input_documents=docs, question=query)
print(output)