# streamlit_bahasa

### Why
I'm going to travel around Indonesia/Malaysia for a bit and want to cram the language with something better than Duolingo (low bar).

The Bahasa Indonesia https://www.livelingua.com/course/peace_corps/bahasa_indonesian_language_course_-_1 PDFs are available online for free but just reading through it is boring and it'd just be nicer to have a tutor walk me through it and make it more interactive and fun.

### How to Run Locally
```
git clone https://github.com/pmespresso/streamlit_bahasa
cd streamlit_bahasa

source venv/bin/activate
pip install -r requirements.txt

streamlit run Chatbot.py
```

### Overview
I've already loaded the Bahasa Indonesia Peace Corps learning material PDF to Pinecone VectorDB, but you can also embed whatever learning material you wish and point the chatbot to your personal vector db instance wherever it may be hosted. Have fun!
