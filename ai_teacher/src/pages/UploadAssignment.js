import { useState } from "react";
export default function UploadAssignment() {
  const [file, setFile] = useState(null);
  return (
    <div className="content">
      <h2>Upload Assignment</h2>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      {file && <p>File: {file.name}</p>}
    </div>
  );
}