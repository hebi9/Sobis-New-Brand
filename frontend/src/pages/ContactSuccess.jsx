import { Helmet } from "react-helmet";
import NavScrollExample from "../components/Navbar";
import Container from "react-bootstrap/Container";


export default function ContactSuccess() {
  return (
    <>
      <Helmet>
        <title>Gracias por contactarnos</title>
      </Helmet>
      <NavScrollExample />
      <div>
        
      <Container fluid className="d-flex justify-content-center align-items-center flex-column" style={{ minHeight: "70vh", textAlign: "center", paddingTop: "50px" }}>
        <h1>Gracias por contactarnos</h1>
        <p>Hemos recibido tu mensaje y nos pondremos en contacto contigo pronto.</p>
        <img src="/logo.svg" alt="Thank You" style={{ maxWidth: "500px", marginTop: "20px" }} />
      </Container>

      </div>
    </>
  );
}