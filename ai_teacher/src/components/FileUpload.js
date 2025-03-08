import { useState } from "react";

export default function FileUpload() {
  const [file, setFile] = useState(null);

  return (
    <div className="file-upload-container">
      <h2 className="file-upload-title">Upload Assignment</h2>
      <input 
        type="file" 
        onChange={(e) => setFile(e.target.files[0])} 
        className="file-input"
      />
      {file && <p className="file-name">File: {file.name}</p>}
    </div>
  );
}