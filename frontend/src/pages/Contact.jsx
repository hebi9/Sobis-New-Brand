import { Helmet } from "react-helmet";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import NavScrollExample from "../components/Navbar";

const API_BASE_URL =
  window.location.hostname === "localhost"
    ? "http://localhost:8000"
    : "https://hebi.pythonanywhere.com";


function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.startsWith(name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}


export default function Contact() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    nombre: "",
    asunto: "",
    correo: "",
    descripcion: "",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const csrftoken = getCookie("csrftoken");
      const response = await fetch(`${API_BASE_URL}/api/crm/contacto/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        navigate("/contacto/exito");
      } else {
        alert("Error de conexión con el servidor ❌" + window.location.hostname);
      }
    } catch (error) {
      console.error("Error:", error);
      alert("Error de conexión con el servidor ❌" + window.location.hostname);
    }
  };

  return (
    <>
      <Helmet>
        <title>Contacto</title>
      </Helmet>
      <div>
        <NavScrollExample />
        <div className="container mt-4">
          <h2>Formulario de Contacto</h2>
          <Form onSubmit={handleSubmit}>
            <Form.Group className="mb-3">
              <Form.Label>Nombre</Form.Label>
              <Form.Control
                type="text"
                name="nombre"
                value={formData.nombre}
                onChange={handleChange}
                required
              />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Asunto</Form.Label>
              <Form.Control
                type="text"
                name="asunto"
                value={formData.asunto}
                onChange={handleChange}
                required
              />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Correo electrónico</Form.Label>
              <Form.Control
                type="email"
                name="correo"
                value={formData.correo}
                onChange={handleChange}
                required
              />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Descripción</Form.Label>
              <Form.Control
                as="textarea"
                rows={4}
                name="descripcion"
                value={formData.descripcion}
                onChange={handleChange}
                required
              />
            </Form.Group>

            <Button variant="primary" type="submit">
              Enviar
            </Button>
          </Form>
        </div>
      </div>
    </>
  );
}
