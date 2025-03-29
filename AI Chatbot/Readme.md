# **Chatbot using Groq and Streamlit** 🤖💬  

A simple chatbot built with **Streamlit** and **Groq API**, designed to provide AI-powered conversations in a web-based interface. This project stores chat history, streams real-time responses, and ensures smooth interactions.  

---

## **🔧 Features**
✅ **User-friendly UI** – Built with Streamlit for easy interaction.  
✅ **AI-powered responses** – Uses Groq API (or another LLM) for chat responses.  
✅ **Real-time streaming** – Messages are streamed dynamically.  
✅ **Persistent chat history** – Messages stay even when the page refreshes.  

---

## **📌 Installation**
### **1️⃣ Clone the repository**  
```bash
git clone https://github.com/your-username/chatbot-groq-streamlit.git
cd chatbot-groq-streamlit
```

### **2️⃣ Create a virtual environment (optional but recommended)**  
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows
```

### **3️⃣ Install dependencies**  
```bash
pip install -r requirements.txt
```

---

## **🚀 Running the Chatbot**
```bash
streamlit run frontend.py
```
This will open the chatbot in your default web browser.

---

## **📜 Project Structure**
```
📂 chatbot-groq-streamlit
│── 📄 frontend.py      # Streamlit UI and chat logic
│── 📄 backend.py       # Handles API calls to Groq (or another LLM)    
└── 📄 README.md        # Project documentation
```

---

## **🛠 Technologies Used**
- **Python 3.x** 🐍
- **Streamlit** (for web UI)  
- **Groq API / OpenAI API** (for AI responses)  

---

## **💡 How It Works**
1️⃣ **User types a message** → Stored in `st.session_state.messages`  
2️⃣ **Message sent to AI** → Calls `answer(prompt)` (from `backend.py`)  
3️⃣ **AI generates response** → Streams the reply dynamically  
4️⃣ **Chat history is saved** → Messages persist using `st.session_state` 

![image](https://github.com/user-attachments/assets/7992fabf-fa06-4202-8664-72eb2afe08b4)


---

## **🌟 Contributing**
Feel free to fork this repo, improve the chatbot, and submit a pull request! 🚀  


Enjoy chatting with AI! 🚀💬
