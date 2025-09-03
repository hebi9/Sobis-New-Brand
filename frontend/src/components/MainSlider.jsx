import React, { useEffect, useRef, useState } from "react";
import { Container, Card, CardBody } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import img1 from '../assets/img/img1.jpg';
import img2 from '../assets/img/img2.jpg';
import img3 from '../assets/img/img3.jpg';
import img4 from '../assets/img/img4.jpg';

export default function MainSlider() {
  const images = [img1, img2, img4];
  const items = [    
    // <Card style={{ width: "300px", height: "300px", borderRadius: "50%", boxShadow: "0 0 10px rgba(0, 0, 0, 0.5)" }}
    //                     className="mb-3 p-5 ">
    //                     <CardBody className="text-center fs-4 d-flex justify-content-center align-items-center">Elemento 1</CardBody>
    //                 </Card>
  ];
  images.map((img, index) => {
    items.push(
      <figure key={index}>
        <img src={img} alt={`img-${index + 1}`} style={{ maxWidth: "100%"}} />
      </figure>
    );
  });

  return <>
    <div style={{ margin: "100px 0 150px 0"}}>
      <InfiniteFlowSlider items={items} />
    </div>
  </>;
}

function InfiniteFlowSlider({ items }) {
  const [slides] = useState([...items, ...items, ...items, ...items]);
  const trackRef = useRef(null);

  // estado para UI
  const [paused, setPaused] = useState(false);
  // referencia para animación
  const pausedRef = useRef(paused);

  useEffect(() => {
    pausedRef.current = paused; // sincronizamos el ref con el estado
  }, [paused]);

  useEffect(() => {
    const track = trackRef.current;
    let animationFrame;
    let offset = 0;
    const speed = 1;

    const animate = () => {
      if (!pausedRef.current) {
        offset -= speed;
        track.style.transform = `translateX(${offset}px)`;

        const firstSlide = track.children[0];
        if (firstSlide && -offset >= firstSlide.offsetWidth) {
          track.appendChild(firstSlide);
          offset += firstSlide.offsetWidth;
        }
      }
      animationFrame = requestAnimationFrame(animate);
    };

    animationFrame = requestAnimationFrame(animate);
    return () => cancelAnimationFrame(animationFrame);
  }, []); // 👈 sin dependencia de paused

  return (
    <Container fluid className=" py-4 overflow-hidden">
      <div
        className="slider"
        style={{ overflow: "hidden", width: "100%" }}
        onMouseEnter={() => setPaused(true)}
        onMouseLeave={() => setPaused(false)}
      >
        <div
          ref={trackRef}
          style={{ display: "flex", willChange: "transform" }}
        >
          {slides.map((node, i) => (
            <div
              key={i}
              style={{
                flex: "0 0 40%",
                padding: "0.5rem",
                boxSizing: "border-box",
              }}
            >
              {node}
            </div>
          ))}
        </div>
      </div>
    </Container>
  );
}
