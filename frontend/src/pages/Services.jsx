import { Helmet } from "react-helmet";
import { Link } from "react-router-dom";  // Importa Link de React Router
import Button from 'react-bootstrap/Button';
import NavScrollExample from "../components/Navbar";

export default function Services() {
  return (
    <>
      <Helmet>
        <title>Servicios</title>
      </Helmet>
      <div>
        <NavScrollExample />
        <h1>Servicios</h1>
        <Button as={Link} to="/login" variant="primary">
          Iniciar sesión
        </Button>
      </div>
    </>
  );
}
