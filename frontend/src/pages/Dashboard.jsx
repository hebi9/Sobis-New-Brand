import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import jwtDecode from "jwt-decode";
import axios from "axios";
import { Helmet } from "react-helmet";
import NavScrollExample from "../components/Navbar";


export default function Dashboard() {
  const navigate = useNavigate();
  const [message, setMessage] = useState("");

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) return navigate("/login");

    try {
      const decoded = jwtDecode(token);
      const API_BASE_URL =
        window.location.hostname === "localhost"
          ? "http://localhost:8000"
          : "https://hebi.pythonanywhere.com";
      axios.get(`${API_BASE_URL}/api/dashboard/`, {
        headers: { Authorization: `Bearer ${token}` }
      }).then(res => setMessage(res.data.message));
    } catch {
      navigate("/login");
    }
  }, []);

  return (
    <>
      <Helmet>
        <title>Dashboard - Usuario</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>
      <NavScrollExample />
      
      <div>{message}</div>
    </>
  );
}
