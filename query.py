import os
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
import argparse
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import module_preprocessing

# Load environment variables

load_dotenv()

# Load environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
module_preprocessing.configure_api(GEMINI_API_KEY)
model = module_preprocessing.create_model()
# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "vulnhunt-gpt-final"

# Ensure the index exists
existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]
if index_name not in existing_indexes:
    raise ValueError(f"Index {index_name} not found. Please ensure the index is created before running this.")


embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
# Load the Pinecone VectorStore = connect to it
vectorstore = PineconeVectorStore(
    index_name=index_name,
    embedding=embeddings
)

llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    model_name='gpt-3.5-turbo',
    temperature=0.01
)

qa = RetrievalQAWithSourcesChain.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)


if __name__ == "__main__":
    print("===================== VULNHUNT-GPT ====================")
    user_input = module_preprocessing.get_user_input()
    chat_session = module_preprocessing.start_chat_session(model, user_input)
    response = module_preprocessing.send_message(chat_session, user_input)
    formatted_response = module_preprocessing.process_response(response)
    module_preprocessing.save_response(formatted_response)
    # print(formatted_response)
    # Tiền xử lý mã Solidity
    user_prompt = """ You are VulnHunt—GPT. You will analyze the Solidity smart contract in order to find any vulnerabilities. When you find vulnerability, you will answer always in this way: 
            You MUST always divide the answer in two sections: 
            — Vulnerabilities: and 
            — Remediation: For Vulnerabilities you will describe any vulnerabilities that you have found and what cause them. For Remediation you will suggest the remediation and any possible fixes to the source code""" + formatted_response
    

    # Gọi LLM để lấy kết quả
    response = qa.invoke(user_prompt)
    
    # Lấy phần "answer" và "sources" từ kết quả trả về
    answer = response.get("answer", "Không tìm thấy câu trả lời.")
    sources = response.get("sources", "Không tìm thấy nguồn.")
    
    # In kết quả định dạng lại
    print("--------------------------------")
    print("\nKết quả truy vấn:")
    print(answer, end= "")
    print(f"\nNguồn:\n{sources}")
    print("--------------------------------")

    