import { Link } from "react-router-dom";
export default function Navbar() {
  return (
    <nav className="bg-blue-600 p-4 text-white flex justify-between">
      <h1 className="text-xl font-bold">AI Teacher Feedback</h1>
      <div>
        <Link className="mr-4" to="/">Home</Link>
        <Link className="mr-4" to="/upload">Upload</Link>
        <Link className="mr-4" to="/feedback">Feedback</Link>
        <Link to="/dashboard">Dashboard</Link>
      </div>
    </nav>
  );
}