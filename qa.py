"""Ask a question to the notion database."""
import faiss
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain
import pickle
import argparse
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser(description='Ask a question to the Bahasa Indonesia Book.')
parser.add_argument('question', type=str, help='The question to ask the Bahasa Indonesia Book.')
args = parser.parse_args()

# Load the LangChain.
index = faiss.read_index("docs.index")

with open("faiss_store.pkl", "rb") as f:
    store = pickle.load(f)

store.index = index
chain = RetrievalQAWithSourcesChain.from_chain_type(llm=ChatOpenAI(temperature=0), retriever=store.as_retriever())
result = chain({"question": args.question})
print(f"Answer: {result['answer']}")
print(f"Sources: {result['sources']}")