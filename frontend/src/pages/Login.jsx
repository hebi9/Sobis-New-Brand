import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { loginUser } from "../api/auth";
import { Helmet } from "react-helmet";
import Button from 'react-bootstrap/Button';
import NavScrollExample from "../components/Navbar";


export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  async function handleLogin(e) {
    e.preventDefault();
    try {
      const data = await loginUser({ username: email, password });
      localStorage.setItem("token", data.access);
      navigate("/dashboard");
    } catch (err) {
      alert("Credenciales inválidas");
    }
  }

  return (
    <>
      <Helmet>
        <title>Login - Mi Sitio</title>
      </Helmet>
      <NavScrollExample />
      
      <form onSubmit={handleLogin}>
        <input value={email} onChange={e => setEmail(e.target.value)} placeholder="Usuario" />
        <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Contraseña" />
        <Button type="submit">Entrar</Button>
      </form>
    </>
  );
}

