import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import CustomerModal from '../components/CustomerModal';


const API_BASE_URL =
  window.location.hostname === "localhost"
    ? "http://localhost:8000"
    : "https://hebi.pythonanywhere.com";


const ProjectDetailsPage = () => {
  const { projectId } = useParams();
  const [project, setProject] = useState(null);
  const [modalOpen, setModalOpen] = useState(false);
  const [loadingEmail, setLoadingEmail] = useState(false);

  useEffect(() => {
  const fetchProject = async () => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/crm/projects/${projectId}/`);
      if (!res.ok) throw new Error('Error al obtener el proyecto');
      const data = await res.json();
      setProject(data);
    } catch (err) {
      console.error('Error fetching project:', err);
    }
  };

  fetchProject();
}, [projectId]);

const sendEmailToClient = async () => {
  setLoadingEmail(true);
  try {
    const res = await fetch(`${API_BASE_URL}/api/crm/project/send-link/${projectId}/`, {
      method: "POST",
    });
    if (!res.ok) throw new Error('Error al enviar correo');
    alert('Correo enviado al cliente');
  } catch (err) {
    alert('Error al enviar el correo');
    console.error(err);
  } finally {
    setLoadingEmail(false);
  }
};

  if (!project) return <p>Cargando...</p>;

  return (
    <div className="project-details-container">
      <h1>Proyecto: {project.name}</h1>
      <p><strong>Descripción:</strong> {project.description}</p>
      <p><strong>Estado:</strong> {project.status}</p>
      <p><strong>Cliente:</strong> {project.customer?.name}</p>

      <div style={{ marginTop: '1rem' }}>
        <button onClick={sendEmailToClient} disabled={loadingEmail}>
          {loadingEmail ? 'Enviando...' : 'Enviar link al cliente'}
        </button>
        <button onClick={() => setModalOpen(true)} style={{ marginLeft: '10px' }}>
          Ver/Editar cliente
        </button>
      </div>

      <CustomerModal
        isOpen={modalOpen}
        onClose={() => setModalOpen(false)}
        customer={project.customer}
        onUpdate={(updatedCustomer) =>
          setProject((prev) => ({ ...prev, customer: updatedCustomer }))
        }
      />
    </div>
  );
};

export default ProjectDetailsPage;
