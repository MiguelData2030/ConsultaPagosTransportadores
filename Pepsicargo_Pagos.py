import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Consulta de Pagos para Conductores", layout="wide")
st.title("Consulta de Pagos para Conductores")

# Variables de sesión
if "proveedor" not in st.session_state:
    st.session_state["proveedor"] = None

# Conexión a la base de datos
usuario = 'postgres'
contraseña = 'Luna2030.'
host = 'localhost'
puerto = '5433'
db = 'Proyecto_Pagos'

engine = create_engine(f'postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{db}')

# Formulario de ingreso
if st.session_state["proveedor"] is None:
    with st.form(key="login_form"):
        numero_proveedor = st.text_input("Ingrese su número de proveedor:", type="password")
        login_button = st.form_submit_button("Ingresar")

        if login_button:
            if numero_proveedor == "":
                st.error("Por favor, ingrese un número de proveedor.")
            else:
                query_validar = f'SELECT * FROM usuarios WHERE "Acreedor" = \'{numero_proveedor}\''
                try:
                    df_usuario = pd.read_sql(query_validar, engine)
                    if df_usuario.empty:
                        st.error("Número de proveedor no encontrado. Intente nuevamente.")
                    else:
                        st.session_state["proveedor"] = numero_proveedor
                        st.session_state["nombre_proveedor"] = df_usuario.iloc[0]['Nombre del Proveedor']
                        st.success(f"¡Bienvenido {st.session_state['nombre_proveedor']}!")
                except Exception as e:
                    st.error(f"Error al conectar con la base de datos: {e}")

# Opciones de consulta
if st.session_state["proveedor"]:
    # Proveedor en sesión
    st.sidebar.markdown(f"**Proveedor en sesión:** {st.session_state['proveedor']}")

    # Selección de año
    st.sidebar.title("Año de consulta")
    anio_consulta = st.sidebar.number_input("Seleccione el año:", min_value=2020, max_value=2030, value=2024, step=1)

    # Rango de fechas
    st.sidebar.title("Rango de Fechas")
    fecha_inicio = st.sidebar.date_input("Fecha inicio", pd.Timestamp(f"{anio_consulta}-01-01"))
    fecha_fin = st.sidebar.date_input("Fecha fin", pd.Timestamp(f"{anio_consulta}-12-31"))

    if fecha_inicio > fecha_fin:
        st.sidebar.error("La fecha de inicio no puede ser mayor que la fecha de fin.")

    if st.sidebar.button("Consultar por rango de fechas"):
        try:
            # Consulta de anticipos
            query_anticipos = f"""
            SELECT "Acreedor", "Nombre del Proveedor", "MANIFIESTO", "Fecha_Manifiesto", "ANTICIPO"
            FROM anticipos
            WHERE "Acreedor" = '{st.session_state['proveedor']}'
            AND "Fecha_Manifiesto" BETWEEN '{fecha_inicio}' AND '{fecha_fin}'
            """
            df_anticipos = pd.read_sql(query_anticipos, engine)

            # Formatear datos
            df_anticipos["Acreedor"] = df_anticipos["Acreedor"].astype(str).str.replace(",", "")
            df_anticipos["MANIFIESTO"] = df_anticipos["MANIFIESTO"].astype(str).str.replace(",", "")
            df_anticipos["ANTICIPO"] = df_anticipos["ANTICIPO"].astype(int)
            df_anticipos["Fecha_Manifiesto"] = pd.to_datetime(df_anticipos["Fecha_Manifiesto"]).dt.date
            df_anticipos["Semana"] = pd.to_datetime(df_anticipos["Fecha_Manifiesto"]).dt.isocalendar().week

            # Mostrar tabla de anticipos
            st.subheader("Anticipos del Rango Seleccionado")
            st.dataframe(df_anticipos)

            # Generar gráfico
            fig_anticipos = px.bar(
                df_anticipos.groupby("Semana")["ANTICIPO"].sum().reset_index(),
                x="Semana",
                y="ANTICIPO",
                title="Total de Anticipos por Semana (Rango Seleccionado)",
                labels={"Semana": "Semana", "ANTICIPO": "Total Anticipos (COP)"},
                color_discrete_sequence=["#4CAF50"]
            )
            fig_anticipos.update_traces(texttemplate="%{y}", textposition="outside")
            st.plotly_chart(fig_anticipos)

            # Consulta de saldos
            query_saldos = f"""
            SELECT "pago", "Acreedor", "Nombre 1", "MANIFIESTO", "VALOR_SALDO"
            FROM saldos
            WHERE "Acreedor" = '{st.session_state['proveedor']}'
            AND "pago" BETWEEN '{fecha_inicio}' AND '{fecha_fin}'
            """
            df_saldos = pd.read_sql(query_saldos, engine)

            # Formatear datos
            df_saldos["Acreedor"] = df_saldos["Acreedor"].astype(str).str.replace(",", "")
            df_saldos["VALOR_SALDO"] = df_saldos["VALOR_SALDO"].astype(int)
            df_saldos["pago"] = pd.to_datetime(df_saldos["pago"]).dt.date
            df_saldos["Semana"] = pd.to_datetime(df_saldos["pago"]).dt.isocalendar().week

            # Mostrar tabla de saldos
            st.subheader("Saldos del Rango Seleccionado")
            st.dataframe(df_saldos)

            # Generar gráfico de saldos
            fig_saldos = px.line(
                df_saldos.groupby("Semana")["VALOR_SALDO"].sum().reset_index(),
                x="Semana",
                y="VALOR_SALDO",
                title="Total de Saldos por Semana (Rango Seleccionado)",
                labels={"Semana": "Semana", "VALOR_SALDO": "Total Saldos (COP)"},
                color_discrete_sequence=["#FF5733"]
            )
            st.plotly_chart(fig_saldos)

        except Exception as e:
            st.error(f"Error al realizar la consulta: {e}")

    # Botón para mes en curso
    if st.sidebar.button("Mes en curso"):
        try:
            # Consulta anticipos mes en curso
            query_anticipos_mes = f"""
            SELECT "Acreedor", "Nombre del Proveedor", "MANIFIESTO", "Fecha_Manifiesto", "ANTICIPO"
            FROM anticipos
            WHERE "Acreedor" = '{st.session_state['proveedor']}'
            AND EXTRACT(MONTH FROM "Fecha_Manifiesto") = EXTRACT(MONTH FROM CURRENT_DATE)
            AND EXTRACT(YEAR FROM "Fecha_Manifiesto") = EXTRACT(YEAR FROM CURRENT_DATE)
            """
            df_mes = pd.read_sql(query_anticipos_mes, engine)

            # Formatear datos
            df_mes["Acreedor"] = df_mes["Acreedor"].astype(str).str.replace(",", "")
            df_mes["MANIFIESTO"] = df_mes["MANIFIESTO"].astype(str).str.replace(",", "")
            df_mes["ANTICIPO"] = df_mes["ANTICIPO"].astype(int)
            df_mes["Fecha_Manifiesto"] = pd.to_datetime(df_mes["Fecha_Manifiesto"]).dt.date

            # Mostrar tabla y gráfico
            st.subheader("Anticipos del Mes en Curso")
            st.dataframe(df_mes)

        except Exception as e:
            st.error(f"Error al realizar la consulta: {e}")

if st.sidebar.button("Cerrar Sesión"):
    try:
        # Limpia la sesión
        st.session_state.clear()  # Limpia todas las variables de sesión
        st.toast("Sesión cerrada correctamente.")  # Mostrar notificación

        # Reinicia los parámetros de la aplicación y recarga
        st.experimental_set_query_params()
        st.experimental_rerun()
    except Exception as e:
        # Si ocurre un error, lo ignoramos y continuamos
        pass









