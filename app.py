import streamlit as st

st.set_page_config(page_title="Calculadora Inmo PRO", page_icon="📈")

st.title("📈 Calculadora de Rentabilidad")
st.subheader("Agencia Emprende Digital con IA+45")

precio_uf = st.number_input("Precio Propiedad (UF)", value=2500.0)
arriendo_uf = st.number_input("Arriendo Mensual (UF)", value=12.0)
gastos_uf = st.number_input("Gastos Mensuales (UF)", value=1.5)

if st.button("CALCULAR AHORA"):
    utilidad_neta = (arriendo_uf - gastos_uf) * 12
    cap_rate = (utilidad_neta / precio_uf) * 100
    st.divider()
    st.metric("CAP RATE ANUAL", f"{cap_rate:.2f} %")
    st.balloons()

st.info("Validado en Chile - Agencia Emprende Digital con IA+45")
