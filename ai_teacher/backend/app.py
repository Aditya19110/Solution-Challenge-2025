from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from langchain_community.vectorstores import Chroma
from langchain_community.llms import CTransformers
from langchain_community.embeddings import HuggingFaceEmbeddings  # ✅ Updated Import
from pydantic import BaseModel  # ✅ Using Pydantic v2 directly
from werkzeug.serving import WSGIRequestHandler

WSGIRequestHandler.timeout = 180  

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend interaction

# ✅ Load Intel Neural Chat Model & Vector Database
print("🚀 Loading Intel Neural Chat model...")
MODEL_PATH = "models/neural-chat-7b-v3-1.Q4_K_M.gguf"

try:
    llm = CTransformers(
        model=MODEL_PATH,
        model_type="mistral",  # Make sure this is correct for your Intel Neural Chat model
        config={"max_new_tokens": 150, "temperature": 0.7}  # Adjust the max tokens & temperature
    )
    print("✅ Intel Neural Chat Model Loaded Successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")

# ✅ Initialize Vector Database (ChromaDB)
embedding_func = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

try:
    vector_store = Chroma(persist_directory="./chroma_db", embedding_function=embedding_func)
    print("✅ ChromaDB Initialized!")
except Exception as e:
    print(f"❌ Error initializing ChromaDB: {e}")

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "✅ AI Teacher Feedback System is running with Adaptive Learning!"})

def generate_feedback(assignment_text):
    """
    Generates AI feedback based on assignment text and past feedback.
    """
    try:
        print("🔍 Retrieving similar feedback from ChromaDB...")
        similar_feedbacks = vector_store.similarity_search(assignment_text, k=2)
        
        context = "\n\n".join([doc.page_content for doc in similar_feedbacks]) if similar_feedbacks else "No similar feedback found."

        print("📝 Creating AI prompt...")
        prompt = f"""
        You are an AI teacher providing **detailed** feedback on student assignments.

        **Assignment:** "{assignment_text}"

        🔍 **Similar Past Feedback:**  
        {context}

        Now generate **new feedback** considering these examples.

        1️⃣ **Score (out of 10)**: Assign a fair score.  
        2️⃣ **Strengths**: Highlight 2-3 key points.  
        3️⃣ **Weaknesses**: Identify issues with explanations.  
        4️⃣ **Suggestions**: Give actionable improvement steps.  

        📌 Keep feedback **specific and constructive**. Avoid generic comments.
        """

        print("🤖 Sending prompt to Intel Neural Chat model...")
        response = llm.invoke(prompt)  # ✅ Track if Intel LLM is hanging
        
        if not response:
            return jsonify({"error": "❌ No response generated from the model"}), 500
        
        print("✅ AI Feedback generated successfully!")
        return response

    except Exception as e:
        print(f"❌ Error in generating feedback: {str(e)}")
        return jsonify({"error": f"❌ Error: {str(e)}"}), 500

@app.route("/upload", methods=["POST"])
def upload_assignment():
    """
    Handles file upload, extracts text, and generates AI feedback.
    """
    print("📥 Received /upload request.")

    if "file" not in request.files:
        return jsonify({"error": "❌ No file uploaded"}), 400

    file = request.files["file"]
    
    if file.filename == "":
        return jsonify({"error": "❌ No selected file"}), 400

    # ✅ Read file content
    try:
        file_content = file.read().decode("utf-8")
        print(f"📜 File content preview: {file_content[:100]}...")  # Show first 100 characters
        
        # ✅ Generate AI Feedback
        print("📥 Generating feedback for assignment...")
        feedback = generate_feedback(file_content)
        
        return jsonify({"feedback": feedback})
    except Exception as e:
        print(f"❌ Error processing file: {str(e)}")
        return jsonify({"error": f"❌ Error: {str(e)}"}), 500

@app.route("/submit", methods=["POST"])
def submit_text():
    """
    Handles direct text submission and generates feedback.
    """
    data = request.get_json()
    
    if "text" not in data or not data["text"].strip():
        return jsonify({"error": "❌ No text provided"}), 400
    
    print(f"📜 Received text submission: {data['text'][:100]}...")  # Preview first 100 chars
    
    # ✅ Generate AI Feedback
    feedback = generate_feedback(data["text"])
    
    return jsonify({"feedback": feedback})

if __name__ == "__main__":
    app.run(debug=True)