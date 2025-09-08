import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const PublicProjectPage = () => {
  const { token } = useParams();
  const [project, setProject] = useState(null);
  const [error, setError] = useState(null);
  const [accepting, setAccepting] = useState(false);
  const [accepted, setAccepted] = useState(false);

  useEffect(() => {
    fetch(`/api/project/public/${token}/`)
      .then((res) => {
        if (!res.ok) throw new Error('Proyecto no encontrado');
        return res.json();
      })
      .then((data) => {
        setProject(data);
        setAccepted(data.accepted_terms); // Asume que el backend ya lo devuelve
      })
      .catch((err) => setError(err.message));
  }, [token]);

  const acceptTerms = async () => {
    setAccepting(true);
    try {
      const res = await fetch(`/api/project/public/${token}/accept/`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ accepted_terms: true }),
      });
      if (!res.ok) throw new Error("No se pudo aceptar los términos");
      setAccepted(true);
      alert("¡Términos aceptados con éxito!");
    } catch (err) {
      alert(err.message);
    } finally {
      setAccepting(false);
    }
  };

  if (error) return <div>Error: {error}</div>;
  if (!project) return <div>Cargando proyecto...</div>;

  return (
    <div className="public-project-page">
      <h1>Proyecto: {project.name}</h1>
      <p><strong>Descripción:</strong> {project.description}</p>
      <p><strong>Estado:</strong> {project.status}</p>
      <p><strong>Cliente:</strong> {project.customer_name || project.customer}</p>
      <p><strong>Creado:</strong> {new Date(project.created_at).toLocaleString()}</p>

      {accepted ? (
        <p style={{ color: 'green' }}>✅ Términos ya aceptados</p>
      ) : (
        <button onClick={acceptTerms} disabled={accepting}>
          {accepting ? "Enviando..." : "Aceptar Términos y Condiciones"}
        </button>
      )}
    </div>
  );
};

export default PublicProjectPage;
