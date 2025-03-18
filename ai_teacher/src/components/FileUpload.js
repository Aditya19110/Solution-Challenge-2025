import { useState } from "react";
import API_BASE_URL from "../config";  

export default function FileUpload() {
  const [file, setFile] = useState(null);
  const [feedback, setFeedback] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];

    if (selectedFile) {
      const allowedTypes = ["text/plain", "application/pdf"];
      if (!allowedTypes.includes(selectedFile.type)) {
        setError("❌ Only .txt and .pdf files are allowed.");
        setFile(null);
        return;
      }

      setFile(selectedFile);
      setError(""); 
    }
  };

  const handleUpload = async () => {
    if (!file) {
      setError("❌ Please select a file.");
      return;
    }

    setLoading(true);
    setFeedback("");
    setError("");

    const formData = new FormData();
    formData.append("file", file);

    try {
      console.log("📤 Sending file to API...");
      
      const response = await fetch(`${API_BASE_URL}/upload`, {
        method: "POST",
        body: formData,
      });

      console.log("✅ API Response:", response);

      const data = await response.json();
      console.log("📄 Response JSON:", data);

      if (!response.ok) throw new Error(data.error || "Failed to upload file");

      setFeedback(`✅ AI Feedback:\n${data.feedback}`);
    } catch (error) {
      console.error("❌ Upload Error:", error.message);
      setError(`❌ ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="file-upload-container">
      <h2>📤 Upload Assignment</h2>
      
      <input
        type="file"
        accept=".txt,.pdf"
        onChange={handleFileChange}
        className="file-input"
      />
      
      <button onClick={handleUpload} className="upload-btn" disabled={loading}>
        {loading ? "Uploading..." : "Upload"}
      </button>

      {feedback && <p className="feedback-text">{feedback}</p>}

      {error && <p className="error-text">{error}</p>}
    </div>
  );
}