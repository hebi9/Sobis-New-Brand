import { Helmet } from "react-helmet";
import { Link } from "react-router-dom";  // Importa Link de React Router
import Button from 'react-bootstrap/Button';
import NavScrollExample from "../components/Navbar";
import OrbitCarousel from "../components/OrbitCarousel";
import Carrousel3D from '../components/Carrousel3D';

import '../assets/css/Landing.css';


export default function Landing() {
  return (
    <>
      <Helmet>
        <title>Landing SEO - Mi Sitio</title>
        <meta name="description" content="Landing page optimizada para motores de búsqueda." />
      </Helmet>
      <NavScrollExample />

      <div className="landing-container">
        <h2 className="text-end">“Convertiremos tus ideas en realidad”</h2>
        <h1 className="mt-3 ml-3">Servicio de diseño <br />web en México</h1>
        <Carrousel3D />
        {/* <Button as={Link} to="/login" variant="primary">
          Iniciar sesión
        </Button> */}
        {/* <OrbitCarousel /> */}
      </div>
    </>
  );
}
