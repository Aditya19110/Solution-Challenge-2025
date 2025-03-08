import { useState } from "react";
export default function UploadAssignment() {
  const [file, setFile] = useState(null);
  return (
    <div className="p-6">
      <h2 className="text-xl font-bold">Upload Assignment</h2>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} className="mt-2" />
      {file && <p className="mt-2">File: {file.name}</p>}
    </div>
  );
}