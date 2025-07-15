Proyecto Django + React + SEO
-----------------------------

Este proyecto contiene:

- Backend Django (REST API, JWT, SEO: robots.txt)
- Estructura básica para React (frontend)
- Login con JWT y rutas protegidas

Pasos:
1. Backend:
    - Crear entorno virtual
    - pip install django djangorestframework djangorestframework-simplejwt django-cors-headers
    - python manage.py migrate
    - python manage.py runserver

2. Frontend:
    - cd frontend
    - npx create-react-app .
    - npm install react-router-dom react-helmet axios jwt-decode
    - npm start

3. Producción:
    - npm run build
    - Copiar contenido de build/ a una carpeta en Django para servirlo

