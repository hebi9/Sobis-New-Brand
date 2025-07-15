import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import { NavLink } from 'react-router-dom';
import Navbar from 'react-bootstrap/Navbar';
import logo from '../assets/img/logo.svg';
import '../assets/css/Navbar.css';

export default function NavScrollExample() {
  return (
    <Navbar expand="md" className="bg-body-tertiary   p-0" sticky="top"
      style={{
        backgroundColor: 'rgba(255, 255, 255, 0.)',
      }}
    >
      <Container fluid>
        <Navbar.Brand href="/">
            <img
                src={logo}
                alt="Logo"
                width="160"
                height="70"
                className="d-inline-block align-top"
            />
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="navbarScroll" />
        <Navbar.Collapse id="navbarScroll">
          <Nav
            className="ms-auto my-2 my-md-0"
            style={{ maxHeight: '120px' }}
            navbarScroll
          >
            <Nav.Link as={NavLink} to="/" className="mx-3">Inicio</Nav.Link>
            <Nav.Link as={NavLink} to="/servicios" className="mx-3">Servicios</Nav.Link>            
            <Nav.Link as={NavLink} to="/contacto"  className="mx-3">
              Contacto
            </Nav.Link>
          </Nav>
          
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

