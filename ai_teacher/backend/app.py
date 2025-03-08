import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_community.vectorstores import Chroma
from langchain_community.llms import CTransformers
from langchain_huggingface import HuggingFaceEmbeddings

# ✅ Initialize Flask App
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# ✅ Define Model Path
MODEL_PATH = os.path.abspath("models/neural-chat-7b-v3-1.Q4_K_M.gguf")
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"❌ Model file not found at {MODEL_PATH}. Please check the path!")

# ✅ Load LLM Model (CTransformers)
try:
    llm = CTransformers(
        model=MODEL_PATH,  # ✅ Corrected parameter
        model_type="mistral",
        config={"max_new_tokens": 200, "temperature": 0.7}
    )
except Exception as e:
    raise RuntimeError(f"❌ Error loading LLM model: {str(e)}")

# ✅ Initialize ChromaDB with HuggingFace Embeddings
CHROMA_DB_PATH = "vector_store"
embedding_model = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
vector_store = Chroma(
    collection_name="teacher_feedback",
    persist_directory=CHROMA_DB_PATH,  # ✅ Persistent storage for ChromaDB
    embedding_function=embedding_model
)

# ✅ Function: Generate AI Feedback
def generate_feedback(assignment_text):
    """
    Generates AI feedback based on assignment text and past feedback.
    """
    try:
        # 🔍 Retrieve Similar Assignments
        similar_feedbacks = vector_store.similarity_search(assignment_text, k=2)
        context = "\n\n".join([doc.page_content for doc in similar_feedbacks]) if similar_feedbacks else "No similar feedback found."

        # 📝 AI Prompt for Feedback Generation
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

        return llm.invoke(prompt)  

    except Exception as e:
        return f"❌ Error in generating feedback: {str(e)}"

# ✅ API Route: Submit Assignment (Adaptive Learning)
@app.route("/submit", methods=["POST"])
def submit_assignment():
    """
    Handles text-based assignment submissions and generates AI feedback.
    """
    try:
        data = request.json
        text = data.get("text", "").strip()

        if not text:
            return jsonify({"error": "No assignment text provided"}), 400

        feedback = generate_feedback(text)

        # 📌 Store Assignment + AI Feedback in ChromaDB
        vector_store.add_texts([text + "\n\n" + feedback])
        vector_store.persist()  # ✅ Save data persistently

        return jsonify({"feedback": feedback})

    except Exception as e:
        return jsonify({"error": f"❌ Submission error: {str(e)}"}), 500

# ✅ API Route: Upload File (Text Assignments)
@app.route("/upload", methods=["POST"])
def upload_file():
    """
    Handles file-based assignment uploads and generates AI feedback.
    """
    try:
        if "file" not in request.files:
            return jsonify({"error": "No file part in request"}), 400

        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "No selected file"}), 400

        text = file.read().decode("utf-8")  # Read file content
        feedback = generate_feedback(text)

        # 📌 Store feedback in ChromaDB
        vector_store.add_texts([text + "\n\n" + feedback])
        vector_store.persist()  # ✅ Save data persistently

        return jsonify({"feedback": feedback})

    except UnicodeDecodeError:
        return jsonify({"error": "❌ File decoding error. Ensure the file is UTF-8 encoded."}), 400
    except Exception as e:
        return jsonify({"error": f"❌ File processing error: {str(e)}"}), 500

# ✅ API Route: Home
@app.route("/", methods=["GET"])
def home():
    """
    Health check route for API status.
    """
    return jsonify({"message": "✅ AI Teacher Feedback System is running with Adaptive Learning!"})

# ✅ Run Flask App
if __name__ == "__main__":
    app.run(debug=True)