import React, { useEffect, useRef } from "react";
import '../assets/css/OrbitCarousel.css';

export default function OrbitCarousel() {
  const itemsRef = useRef([]);

  useEffect(() => {
    const items = itemsRef.current;
    const radius = 150;
    let angle = 0;

    function animate() {
      angle += 0.01; // velocidad

      items.forEach((item, index) => {
        const itemAngle = angle + (index * (2 * Math.PI)) / 3; // separación entre los 3
        const x = radius * Math.cos(itemAngle);
        const y = radius * Math.sin(itemAngle);

        item.style.transform = `translate(${x}px, ${y}px)`;

        // Tamaño dinámico según ángulo
        const normalized = Math.cos(itemAngle); // -1 a 1
        const scale = (normalized + 1) / 2; // 0 a 1

        const height = 50 + 75 * scale; // entre 50 y 125
        item.style.height = `${height}px`;
        item.style.width = `${height}px`; // opcional: circular

        // Z-index para profundidad
        item.style.zIndex = Math.round(100 * scale);
      });

      requestAnimationFrame(animate);
    }

    animate();
  }, []);

  return (
    <div className="orbit-container">
      {[0, 1, 2].map((_, i) => (
        <div
          key={i}
          className="orbit-item"
          ref={(el) => (itemsRef.current[i] = el)}
        ></div>
      ))}
    </div>
  );
}