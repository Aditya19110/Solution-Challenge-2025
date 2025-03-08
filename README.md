# AI-Powered Teacher Feedback System

## Overview
The **AI-Powered Teacher Feedback System** is an AI-driven platform designed to automate assignment grading and provide personalized feedback to students. It utilizes **LLMs, NLP, and Vector Databases** to evaluate text, handwritten, coding, and MCQ assignments.

### **Features**
- 📖 **Automated Assignment Grading** (Text, Handwritten, Coding, MCQs)
- 🤖 **AI-Powered Personalized Feedback**
- 🔍 **Adaptive Learning with ChromaDB**
- 🚀 **Real-time Processing with Fast API**
- 🧠 **Neural Chat v3.1 for Natural Language Understanding**

---
## Tech Stack
### **Frontend (React.js)**
- **React.js** (UI Framework)
- **TailwindCSS** (Styling)
- **Axios** (API Calls)
- **React Router** (Navigation)

### **Backend (Flask, AI, VectorDB)**
- **Flask** (Backend Framework)
- **CTransformers (Neural Chat v3.1 - GGUF)**
- **LangChain-Community** (LLM Framework)
- **ChromaDB** (Vector Storage for Adaptive Learning)
- **HuggingFace Embeddings** (Text Processing)

---
## Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Aditya19110/Solution-Challenge-2025/tree/main/ai_teacher
cd ai-teacher-feedback
```

### **2️⃣ Setup & Run React Frontend**
```bash
cd frontend
npm install  # Install dependencies
npm start    # Start the React app
```
Your React app will now run at: **http://localhost:3000**

---
## Backend Setup (Windows & macOS/Linux)

### **3️⃣ Navigate to Backend**
```bash
cd backend
```

### **4️⃣ Create a Virtual Environment**
#### ✅ **Windows**
```bash
python -m venv venv
venv\Scripts\activate
```
#### ✅ **macOS/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### **5️⃣ Install Required Dependencies**
```bash
pip install -r requirements.txt
```

### **6️⃣ Run the Flask Backend**
```bash
python app.py
```
Your Flask API will now run at: **http://127.0.0.1:5000**

---
## Usage
- 📝 **Submit Assignments** via the frontend.
- 🤖 **AI evaluates and provides feedback**.
- 📊 **Adaptive Learning** stores embeddings in ChromaDB.

---
## API Routes
### **1️⃣ Test API**
```http
GET /
```
_Response:_ `{ "message": "AI Teacher Feedback System is running!" }`

### **2️⃣ Submit Assignment**
```http
POST /submit
```
_Request Body:_
```json
{ "text": "Your assignment text here" }
```
_Response:_
```json
{ "feedback": "Your AI-generated feedback" }
```

---
## Contributing
💡 Want to contribute? Follow these steps:
1. **Fork the repo**
2. **Create a feature branch**
3. **Commit your changes**
4. **Push and open a PR** 🚀

---
## License
This project is licensed under the **MIT License**. Feel free to use and modify it.

---
## **Contact**
📧 Email: `kulkarniaditya262@gmail.com`  
🔗 LinkedIn: [Your Profile](https://linkedin.com/in/aditya191103)
