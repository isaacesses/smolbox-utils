from utils import validar_rfc, formatear_moneda, numero_a_letras, no_grande_a_letras
import streamlit as st

st.title("Smolbox Utils")
st.text("Caja de herramientas indispensables para realizar trabajo financiero en alguna empresa.")


rfc, formato, noALetras = st.tabs(["Validar RFC", "Formatear Moneda", "Convertir número a letras"])

# Validar estructura de un RFC
with rfc:
    st.header("Validar RFC")
    st.write("Esta validación solo revisa el formato estructural; no confirma que el RFC exista ante el SAT.")

    with st.form(key="rfc"):
        rfc_ingresado = st.text_input(label="RFC", placeholder="Ingrese un RFC", max_chars=13)
        submit_button = st.form_submit_button(label="Validar")

    if submit_button:
        if validar_rfc(rfc_ingresado):
            st.success(f"¡El RFC ingresado es valido!")
        else:
            st.error("El RFC ingresado no es valido.")


# Darle formato a monto ingresado
with formato:
    st.header("Formatear Moneda")
    st.write("Le agrega formato a números con o sin decimales.")

    with st.form(key="formato"):
        monto = st.text_input(label="Monto", placeholder="1234.56")
        submit_button = st.form_submit_button(label="Convertir")

        if submit_button:
            monto_convertido = formatear_moneda(monto)
            if monto_convertido == None:
                st.error("Número inválido. Recuerda poner el número decimal sin commas y sin formato.")
            else:
                st.success(monto_convertido)


# Convertir numero a letras
with noALetras:
    st.header("Convertir número a letras")
    st.write("Convierte números enteros con y sin decimal a formato de letra en pesos MXN.")

    with st.form(key="noALetras"):
        monto = st.text_input(label="Monto", placeholder="1234.56")
        submit_button = st.form_submit_button("Convertir")

    if submit_button:
        error_message = "Número inválido. El número ingresado debe ser decimal, positivo, sin commas y sin formato."
        try:
            monto = float(monto)
            if monto <= 100:
                en_letras = numero_a_letras(monto)
                if en_letras == None:
                    st.error(error_message)
                else:
                    st.success(en_letras)
            else:
                en_letras = no_grande_a_letras(monto)
                if en_letras == None:
                    st.error(error_message)
                else:
                    st.success(en_letras)
        except:
            st.error(error_message)


with st.bottom:
    st.write("Hecho por: Isaac Esses")