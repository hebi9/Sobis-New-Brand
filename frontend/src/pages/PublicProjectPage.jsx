import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const PublicProjectPage = () => {
  const { token } = useParams();
  const [project, setProject] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`/api/project/public/${token}/`)
      .then((res) => {
        if (!res.ok) throw new Error('Proyecto no encontrado');
        return res.json();
      })
      .then((data) => setProject(data))
      .catch((err) => setError(err.message));
  }, [token]);

  if (error) return <div>Error: {error}</div>;
  if (!project) return <div>Cargando proyecto...</div>;

  return (
    <div className="public-project-page">
      <h1>Proyecto: {project.name}</h1>
      <p><strong>Descripción:</strong> {project.description}</p>
      <p><strong>Estado:</strong> {project.status}</p>
      <p><strong>Cliente:</strong> {project.customer_name || project.customer}</p>
      <p><strong>Creado:</strong> {new Date(project.created_at).toLocaleString()}</p>

      {/* Agrega aquí botón de aceptación de términos si es necesario */}
    </div>
  );
};

export default PublicProjectPage;
