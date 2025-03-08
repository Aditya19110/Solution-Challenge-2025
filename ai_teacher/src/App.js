import React from "react";
import "./App.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import UploadAssignment from "./pages/UploadAssignment";
import Feedback from "./pages/Feedback";
import Dashboard from "./pages/Dashboard";

function App() {
  return (
    <Router>
      <div className="container">
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/upload" element={<UploadAssignment />} />
          <Route path="/feedback" element={<Feedback />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;