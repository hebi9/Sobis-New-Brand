import React from 'react';
import '../assets/css/Carrousel3D.css';
import img1 from '../assets/img/img1.jpg';
import img2 from '../assets/img/img2.jpg';
import img3 from '../assets/img/img3.jpg';

const images = [img1, img2, img3];

export default function Carrousel3D() {
  return (
    <div className="content-all">
      <div className="content-carrousel">
        {images.map((img, index) => (
          <figure key={index}>
            <img src={img} alt={`img-${index + 1}`} />
          </figure>
        ))}
      </div>
    </div>
  );
}
