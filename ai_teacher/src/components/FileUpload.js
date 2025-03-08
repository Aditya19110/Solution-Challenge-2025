import { useState } from "react";
export default function FileUpload() {
  const [file, setFile] = useState(null);
  return (
    <div className="p-4 border rounded bg-white shadow-md">
      <h2 className="text-lg font-semibold">Upload Assignment</h2>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} className="mt-2" />
      {file && <p className="mt-2">File: {file.name}</p>}
    </div>
  );
}