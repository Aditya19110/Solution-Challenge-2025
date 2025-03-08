import FileUpload from "../components/FileUpload"; // Importing FileUpload Component

export default function UploadAssignment() {
  return (
    <div className="upload-page-container">
      <h2 className="upload-page-title">Upload Assignment</h2>
      <FileUpload /> 
    </div>
  );
}