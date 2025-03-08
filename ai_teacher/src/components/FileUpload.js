import { useState } from "react";

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
      setError(""); // Clear previous error
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
      const response = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      if (!response.ok) throw new Error(data.error || "Failed to upload file");

      setFeedback(`✅ AI Feedback: ${data.feedback}`);
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="file-upload-container">
      <h2>📤 Upload Assignment</h2>
      
      {/* ✅ File Input */}
      <input
        type="file"
        accept=".txt,.pdf"
        onChange={handleFileChange}
        className="file-input"
      />
      
      {/* ✅ Upload Button */}
      <button onClick={handleUpload} className="upload-btn" disabled={loading}>
        {loading ? "Uploading..." : "Upload"}
      </button>

      {/* ✅ Show Feedback */}
      {feedback && <p className="feedback-text">{feedback}</p>}

      {/* ❌ Show Errors */}
      {error && <p className="error-text">{error}</p>}
    </div>
  );
}