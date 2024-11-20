# ConsultaPagosTransportadores

## Descripción

**ConsultaPagosTransportadores** es una aplicación web interactiva desarrollada con **Streamlit** que permite a los transportadores de una empresa consultar información sobre sus pagos, anticipos y saldos. La aplicación está conectada a una base de datos PostgreSQL y ofrece funcionalidades para realizar búsquedas por rangos de fechas, visualizar datos detallados y generar gráficos informativos.

## Características

- **Autenticación segura**: Los transportadores pueden iniciar sesión utilizando su número de proveedor.
- **Consulta personalizada**: Permite consultar datos filtrados por rango de fechas o por mes en curso.
- **Visualización de datos**: Muestra los pagos y anticipos en tablas interactivas.
- **Gráficos informativos**: Genera gráficos dinámicos que resumen la información de anticipos y saldos por semana.
- **Despliegue en la nube**: La aplicación está alojada en Streamlit Cloud para fácil acceso.

## Tecnologías Utilizadas

- **Python**: Lenguaje principal para el desarrollo.
- **Streamlit**: Framework para construir aplicaciones web interactivas.
- **PostgreSQL**: Base de datos utilizada para almacenar y consultar la información.
- **Plotly**: Librería para generar gráficos dinámicos.
- **SQLAlchemy**: ORM para interactuar con la base de datos.

## Requisitos

### Librerías de Python

Las librerías necesarias están especificadas en el archivo `requirements.txt`:


### Dependencias del Sistema

Las dependencias del sistema están especificadas en el archivo `packages.txt` y deben instalarse en el servidor:


## Configuración del Proyecto

1. Clona el repositorio:
   ```bash
   git clone https://github.com/MiguelData2030/ConsultaPagosTransportadores.git
   cd ConsultaPagosTransportadores
pip install -r requirements.txt
streamlit run Pepsicargo_Pagos.py
Uso de la Aplicación
Inicio de sesión: Introduce tu número de proveedor para acceder a tu información.
Opciones de consulta:
Filtra por rango de fechas para ver anticipos y saldos.
Consulta información del mes en curso con un solo clic.
Visualización de datos:
Explora tablas interactivas con detalles de anticipos y saldos.
Genera gráficos semanales que resumen los totales de anticipos y saldos.
Estructura del Proyecto

ConsultaPagosTransportadores/
├── Pepsicargo_Pagos.py      # Código principal de la aplicación
├── requirements.txt         # Dependencias de Python
├── packages.txt             # Dependencias del sistema
├── README.md                # Documentación del proyecto
└── Untitled-1.ipynb         # Notas o experimentos en Jupyter Notebook

Aquí está el contenido listo para copiar y pegar directamente en tu archivo README.md:

markdown
Copiar código
# ConsultaPagosTransportadores

## Descripción

**ConsultaPagosTransportadores** es una aplicación web interactiva desarrollada con **Streamlit** que permite a los transportadores de una empresa consultar información sobre sus pagos, anticipos y saldos. La aplicación está conectada a una base de datos PostgreSQL y ofrece funcionalidades para realizar búsquedas por rangos de fechas, visualizar datos detallados y generar gráficos informativos.

## Características

- **Autenticación segura**: Los transportadores pueden iniciar sesión utilizando su número de proveedor.
- **Consulta personalizada**: Permite consultar datos filtrados por rango de fechas o por mes en curso.
- **Visualización de datos**: Muestra los pagos y anticipos en tablas interactivas.
- **Gráficos informativos**: Genera gráficos dinámicos que resumen la información de anticipos y saldos por semana.
- **Despliegue en la nube**: La aplicación está alojada en Streamlit Cloud para fácil acceso.

## Tecnologías Utilizadas

- **Python**: Lenguaje principal para el desarrollo.
- **Streamlit**: Framework para construir aplicaciones web interactivas.
- **PostgreSQL**: Base de datos utilizada para almacenar y consultar la información.
- **Plotly**: Librería para generar gráficos dinámicos.
- **SQLAlchemy**: ORM para interactuar con la base de datos.

## Requisitos

### Librerías de Python

Las librerías necesarias están especificadas en el archivo `requirements.txt`:

streamlit==1.40.1 pandas==2.0.3 SQLAlchemy==2.0.36 psycopg2-binary==2.9.10 numpy==1.26.0 plotly==5.14.1

css
Copiar código

### Dependencias del Sistema

Las dependencias del sistema están especificadas en el archivo `packages.txt` y deben instalarse en el servidor:

python3-distutils build-essential libpq-dev python3-dev

bash
Copiar código

## Configuración del Proyecto

1. Clona el repositorio:
   ```bash
   git clone https://github.com/MiguelData2030/ConsultaPagosTransportadores.git
   cd ConsultaPagosTransportadores
Instala las dependencias de Python:

bash
Copiar código
pip install -r requirements.txt
Configura tu base de datos PostgreSQL con las siguientes credenciales (modifica según tu entorno):

Usuario: postgres
Contraseña: Luna2030.
Host: localhost
Puerto: 5433
Base de datos: Proyecto_Pagos
Ejecuta la aplicación:

bash
Copiar código
streamlit run Pepsicargo_Pagos.py
Uso de la Aplicación
Inicio de sesión: Introduce tu número de proveedor para acceder a tu información.
Opciones de consulta:
Filtra por rango de fechas para ver anticipos y saldos.
Consulta información del mes en curso con un solo clic.
Visualización de datos:
Explora tablas interactivas con detalles de anticipos y saldos.
Genera gráficos semanales que resumen los totales de anticipos y saldos.
Estructura del Proyecto
bash
Copiar código
ConsultaPagosTransportadores/
├── Pepsicargo_Pagos.py      # Código principal de la aplicación
├── requirements.txt         # Dependencias de Python
├── packages.txt             # Dependencias del sistema
├── README.md                # Documentación del proyecto
└── Untitled-1.ipynb         # Notas o experimentos en Jupyter Notebook
Próximos Pasos
Mejorar la interfaz de usuario con más opciones de personalización.
Añadir notificaciones automáticas para pagos pendientes.
Integrar funciones avanzadas de análisis de datos.
Autor
Proyecto desarrollado por Miguel Ángel Londoño Díaz.
