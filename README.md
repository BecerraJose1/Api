# API MAXIMO


API MAXIMO es una API RESTful que permite realizar diversas operaciones, como autenticación, gestión de usuarios y manipulación de datos en la base de datos.

Funcionalidades
La API MAXIMO admite las siguientes funcionalidades:

Autenticación: Los usuarios pueden iniciar sesión y obtener un token de autenticación para acceder a las funciones protegidas de la API.

Usuarios: Los usuarios pueden obtener una lista de usuarios registrados y obtener información detallada sobre un usuario específico.

Filec: Permite la creación de registros de Filec, que incluyen información sobre comprobantes.

File1: Permite la creación de registros de File1, que incluyen información sobre documentos, facturas y cuentas.

File2: Proporciona una lista de registros de File2, que contienen detalles sobre cuentas.

File3: Permite la creación, edición y eliminación de registros de File3, que incluyen información sobre personas y ciudades.

File_ciudad: Proporciona una lista de registros de File_ciudad, que contienen detalles sobre ciudades.

Instrucciones de Uso
Clonar el Repositorio: Clona este repositorio en tu máquina local.

Instalar Dependencias: Asegúrate de tener todas las dependencias instaladas. Puedes usar pip para instalar las dependencias listadas en el archivo requirements.txt.

bash
Copy code
pip install -r requirements.txt
Configurar la Base de Datos: Asegúrate de tener una base de datos configurada. Puedes especificar la configuración de la base de datos en el archivo config.py.

Ejecutar la Aplicación: Ejecuta la aplicación con uvicorn.

bash
Copy code
uvicorn main:app --host 0.0.0.0 --port 8000
Realizar Solicitudes a la API: Utiliza una herramienta como curl o Postman para realizar solicitudes a la API. Asegúrate de incluir la autorización en las cabeceras de las solicitudes protegidas.
Ejemplos de Solicitudes
Iniciar Sesión (Login)
bash
Copy code
curl -X POST -H "Content-Type: application/json" -d '{"email": "tu@email.com", "password": "tu_contraseña"}' http://localhost:8000/login
Crear un Registro de Filec
bash
Copy code
curl -X POST -H "Content-Type: application/json" -H "Authorization: TuTokenDeAutenticación" -d '{"comprobante": "Ejemplo", "nombre": "NombreEjemplo", "tipo": "TipoEjemplo"}' http://localhost:8000/create_file_c
Obtener la Lista de Usuarios
bash
Copy code
curl -H "Authorization: TuTokenDeAutenticación" http://localhost:8000/users
Obtener la Lista de Registros de File2
bash
Copy code
curl -H "Authorization: TuTokenDeAutenticación" http://localhost:8000/get_file2
Crear un Registro de File3
bash
Copy code
curl -X POST -H "Content-Type: application/json" -H "Authorization: TuTokenDeAutenticación" -d '{"cedula": 1234567890, "nombre1": "Juan", "nombre2": "Pablo", "apellido1": "López", "apellido2": "González", "direccion": "Calle 123, Ciudad", "celular": "123-456-7890", "correo": "juan@example.com", "id_ciudad": 7}' http://localhost:8000/create_file3
Requisitos del Sistema
Python 3.7 o superior
Base de datos configurada (MySQL en este caso)
Dependencias instaladas (ver archivo requirements.txt)
Notas
Esta es una aplicación de ejemplo y puede requerir ajustes adicionales para adaptarse a tus necesidades específicas.

Asegúrate de proteger tus rutas y funciones según sea necesario para garantizar la seguridad de tu API.

La documentación completa de FastAPI se encuentra en el sitio web oficial.

Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar esta API, por favor, crea un fork del repositorio y envía un pull request.

Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.