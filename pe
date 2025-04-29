import streamlit as st
import pandas as pd
from io import StringIO

st.set_page_config(page_title="Calculadora de Punto de Equilibrio", layout="centered")

st.title("📊 Calculadora de Punto de Equilibrio")
st.markdown("Esta herramienta te ayuda a calcular cuántas ventas necesitas para cubrir tus gastos mensuales y no perder dinero.")

st.header("1️⃣ Costos Fijos")
st.markdown("**¿Qué son?** Gastos que tienes cada mes sin importar cuánto vendas. Ej: renta, luz, sueldos, etc.")
costos_fijos = st.number_input("Ingresa la suma total de tus costos fijos mensuales (MXN):", min_value=0.0, format="%.2f")

st.header("2️⃣ Costos Variables")
st.markdown("**¿Qué son?** Gastos que cambian según lo que produces o vendes. Ej: materia prima, empaques, comisiones.")

producto_unico = st.radio("¿Vendes un solo producto o varios?", ("Un solo producto", "Varios productos"))

if producto_unico == "Un solo producto":
    precio_venta = st.number_input("Precio de venta por unidad (MXN):", min_value=0.01, format="%.2f")
    costo_unitario = st.number_input("Costo por unidad del producto (MXN):", min_value=0.0, max_value=precio_venta, format="%.2f")
    
    if precio_venta > 0 and costo_unitario >= 0:
        margen_utilidad = ((precio_venta - costo_unitario) / precio_venta) * 100
        utilidad_unitaria = precio_venta - costo_unitario
        
        st.markdown(f"🧮 **Margen de utilidad:** {margen_utilidad:.2f}%")
        st.markdown(f"💰 **Utilidad por unidad vendida:** ${utilidad_unitaria:.2f}")
        
        if utilidad_unitaria > 0:
            punto_equilibrio = costos_fijos / utilidad_unitaria
            st.success(f"🔁 Necesitas vender **{punto_equilibrio:.0f} unidades** al mes para alcanzar tu punto de equilibrio.")
        else:
            st.error("Tu utilidad es cero o negativa. Revisa tus precios o costos.")
        
else:
    st.markdown("Ingresa los datos de tus productos abajo:")
    st.markdown("**Ejemplo:** Producto A, Precio 100, Costo 60")
    data_input = st.text_area("Pega tus datos en este formato:\nNombre,Precio,Costo", height=150)

    if data_input:
        try:
            df = pd.read_csv(StringIO(data_input), names=["Nombre", "Precio", "Costo"])
            df["Precio"] = df["Precio"].astype(float)
            df["Costo"] = df["Costo"].astype(float)
            df["Utilidad"] = df["Precio"] - df["Costo"]
            df["Margen %"] = ((df["Utilidad"]) / df["Precio"]) * 100

            precio_promedio = df["Precio"].mean()
            costo_promedio = df["Costo"].mean()
            utilidad_promedio = precio_promedio - costo_promedio
            margen_promedio = (utilidad_promedio / precio_promedio) * 100 if precio_promedio > 0 else 0

            st.dataframe(df)

            st.markdown(f"📊 **Precio promedio:** ${precio_promedio:.2f}")
            st.markdown(f"📉 **Costo promedio:** ${costo_promedio:.2f}")
            st.markdown(f"🧮 **Margen de utilidad promedio:** {margen_promedio:.2f}%")
            st.markdown(f"💰 **Utilidad promedio por venta:** ${utilidad_promedio:.2f}")

            if utilidad_promedio > 0:
                punto_equilibrio = costos_fijos / utilidad_promedio
                st.success(f"🔁 Necesitas vender **{punto_equilibrio:.0f} unidades promedio** al mes para alcanzar tu punto de equilibrio.")
            else:
                st.error("La utilidad promedio es cero o negativa. Revisa tus precios o costos.")
        except Exception as e:
            st.error("Error al procesar los datos. Asegúrate de que estén en el formato correcto.")
