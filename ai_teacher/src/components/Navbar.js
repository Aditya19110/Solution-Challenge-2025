import { Link } from "react-router-dom";
export default function Navbar() {
  return (
    <nav className="navbar">
      <h1 className="navbar-title">AI Teacher Feedback</h1>
      <div className="nav-links">
        <Link to="/">Home</Link>
        <Link to="/upload">Upload</Link>
        <Link to="/feedback">Feedback</Link>
        <Link to="/dashboard">Dashboard</Link>
      </div>
    </nav>
  );
}
