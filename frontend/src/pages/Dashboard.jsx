import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import jwtDecode from "jwt-decode";
import axios from "axios";
import { Helmet } from "react-helmet";
import NavScrollExample from "../components/Navbar";
import Card from "react-bootstrap/Card";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";

const API_BASE_URL =
  window.location.hostname === "localhost"
    ? "http://localhost:8000"
    : "https://hebi.pythonanywhere.com";

const PROJECT_STATUS = [
  ["NEW", "Nuevo"],
  ["APPROVED", "Aprobado"],
  ["DESIGN", "Diseño"],
  ["DEVELOPMENT", "Programación"],
  ["DEPLOYMENT", "Despliegue"],
  ["COMPLETED", "Completado"],
  ["ARCHIVED", "Archivado"],
];

export default function Dashboard() {
  const navigate = useNavigate();
  const [message, setMessage] = useState("");
  const [projects, setProjects] = useState([]);
  const [filters, setFilters] = useState({
    customer: "",
    category: "",
    search: "",
    month: "",
  });
  const [customers, setCustomers] = useState([]);
  const [categories, setCategories] = useState([]);

  // Validar token y mensaje
  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) return navigate("/login");

    try {
      jwtDecode(token);
      axios
        .get(`${API_BASE_URL}/api/dashboard/`, {
          headers: { Authorization: `Bearer ${token}` },
        })
        .then((res) => setMessage(res.data.message));
    } catch {
      navigate("/login");
    }
  }, [navigate]);

  // Cargar clientes y categorías para filtros
  useEffect(() => {
    axios.get(`${API_BASE_URL}/api/crm/customers/`).then((res) => setCustomers(res.data));
    axios.get(`${API_BASE_URL}/api/crm/categories/`).then((res) => setCategories(res.data));
  }, []);

  // Cargar proyectos desde backend con filtros
  useEffect(() => {
    const params = new URLSearchParams();

    if (filters.customer) params.append("customer", filters.customer);
    if (filters.category) params.append("categories", filters.category);
    if (filters.search) params.append("search", filters.search);
    if (filters.month) params.append("created_at__month", filters.month);

    fetch(`${API_BASE_URL}/api/crm/projects/?${params.toString()}`)
      .then((res) => res.json())
      .then((data) => setProjects(data))
      .catch((err) => console.error("Error cargando proyectos:", err));
  }, [filters]);

  // Agrupar proyectos por status
  const groupedProjects = {};
  PROJECT_STATUS.forEach(([key]) => {
    groupedProjects[key] = projects.filter((p) => p.status === key) || [];
  });

  // Drag & Drop handlers
  const handleDragStart = (e, projectId) => {
    e.dataTransfer.setData("projectId", projectId);
  };

  const handleDrop = async (e, newStatus) => {
    e.preventDefault();
    const projectId = e.dataTransfer.getData("projectId");

    // Optimistic UI update
    setProjects((prev) =>
      prev.map((proj) =>
        proj.id.toString() === projectId
          ? { ...proj, status: newStatus }
          : proj
      )
    );

    // Actualizar en backend
    try {
      await fetch(`${API_BASE_URL}/api/crm/projects/${projectId}/`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ status: newStatus }),
      });
    } catch (err) {
      console.error("❌ Error actualizando status:", err);
    }
  };

  const handleDragOver = (e) => e.preventDefault();

  // Generar opciones de meses disponibles según los proyectos
  const monthOptions = Array.from(
    new Set(projects.map((p) => {
      const date = new Date(p.created_at);
      return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, "0")}`;
    }))
  ).sort((a, b) => b.localeCompare(a));

  return (
    <>
      <Helmet>
        <title>Dashboard - Usuario</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>
      <NavScrollExample />

      <Container fluid className="p-3">
        {/* Filtros arriba a la derecha */}
        <Row className="mb-3 justify-content-end">
          <Col xs="auto">
            <Form.Select
              value={filters.customer}
              onChange={(e) => setFilters({ ...filters, customer: e.target.value })}
            >
              <option value="">Filtrar por cliente</option>
              {customers.map((c) => (
                <option key={c.id} value={c.id}>{c.name}</option>
              ))}
            </Form.Select>
          </Col>
          <Col xs="auto">
            <Form.Select
              value={filters.category}
              onChange={(e) => setFilters({ ...filters, category: e.target.value })}
            >
              <option value="">Filtrar por categoría</option>
              {categories.map((cat) => (
                <option key={cat.id} value={cat.id}>{cat.name}</option>
              ))}
            </Form.Select>
          </Col>
          <Col xs="auto">
            <Form.Select
              value={filters.month}
              onChange={(e) => setFilters({ ...filters, month: e.target.value })}
            >
              <option value="">Filtrar por mes</option>
              {monthOptions.map((m) => (
                <option key={m} value={m.split("-")[1]}>{m}</option>
              ))}
            </Form.Select>
          </Col>
          <Col xs="auto">
            <Form.Control
              type="text"
              placeholder="Buscar..."
              value={filters.search}
              onChange={(e) => setFilters({ ...filters, search: e.target.value })}
            />
          </Col>
          <Col xs="auto">
            <Button onClick={() => setFilters({ customer: "", category: "", search: "", month: "" })}>
              Limpiar
            </Button>
          </Col>
        </Row>

        <Row className="flex-nowrap overflow-auto">
          {PROJECT_STATUS.map(([key, label]) => (
            <Col key={key} xs={12} sm={6} md={4} lg={3} className="mb-3">
              <div
                className="p-2 bg-light rounded h-100"
                style={{ minHeight: "300px" }}
                onDrop={(e) => handleDrop(e, key)}
                onDragOver={handleDragOver}
              >
                <h5 className="fw-bold text-center mb-3">{label}</h5>

                {groupedProjects[key].map((project) => (
                  <Card
                    key={project.id}
                    className="mb-2 shadow-sm"
                    draggable
                    onDragStart={(e) => handleDragStart(e, project.id.toString())}
                  >
                    <Card.Body>
                      <Card.Title>{project.name}</Card.Title>
                      <Card.Text>{project.description}</Card.Text>
                    </Card.Body>
                  </Card>
                ))}

                {groupedProjects[key].length === 0 && (
                  <div style={{ minHeight: "50px" }} />
                )}
              </div>
            </Col>
          ))}
        </Row>
      </Container>
    </>
  );
}
