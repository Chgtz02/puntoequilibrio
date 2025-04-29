import streamlit as st
import pandas as pd

st.set_page_config(page_title="Calculadora de Punto de Equilibrio", layout="centered")
st.title("📊 Calculadora de Punto de Equilibrio")
st.caption("Desarrollado con ❤️ por Christian Gutiérrez")
st.markdown("Esta herramienta te ayudará a entender los números de tu negocio paso a paso. Vamos a calcular tu **punto de equilibrio**, evaluando tus costos y márgenes de utilidad.")

# 1. Costos Fijos Mensuales
st.header("1️⃣ Costos Fijos Mensuales")
st.markdown("**¿Qué son?** Son los gastos que debes cubrir mes a mes sin importar cuánto vendas: renta, servicios, sueldos, etc.")

costos_fijos = []
for i in range(1, 11):
    col1, col2 = st.columns([3, 1])
    concepto = col1.text_input(f"Concepto fijo #{i}", key=f"cf_concepto_{i}")
    cantidad = col2.number_input(f"Cantidad", min_value=0.0, step=10.0, format="%.2f", key=f"cf_cantidad_{i}")
    costos_fijos.append(cantidad)

total_costos_fijos = sum(costos_fijos)
st.success(f"💰 Total de costos fijos: ${total_costos_fijos:.2f}")

# 2. Costos Variables Mensuales
st.header("2️⃣ Costos Variables Mensuales")
st.markdown("**¿Qué son?** Son los costos que cambian dependiendo de cuánto produzcas o vendas. Ej: materia prima, empaques, comisiones.")

costos_variables = []
for i in range(1, 11):
    col1, col2 = st.columns([3, 1])
    concepto = col1.text_input(f"Concepto variable #{i}", key=f"cv_concepto_{i}")
    cantidad = col2.number_input(f"Cantidad", min_value=0.0, step=10.0, format="%.2f", key=f"cv_cantidad_{i}")
    costos_variables.append(cantidad)

total_costos_variables = sum(costos_variables)
st.success(f"📦 Total de costos variables: ${total_costos_variables:.2f}")

# 3. Margen de Utilidad
st.header("3️⃣ Margen de Utilidad")
st.markdown("**¿Qué es?** Es la ganancia que obtienes por cada venta después de restar el costo del producto.")

precios = []
costos = []
for i in range(1, 11):
    col1, col2 = st.columns(2)
    precio = col1.number_input(f"Precio de venta #{i}", min_value=0.0, step=1.0, format="%.2f", key=f"precio_{i}")
    costo = col2.number_input(f"Costo del producto #{i}", min_value=0.0, step=1.0, format="%.2f", key=f"costo_{i}")
    precios.append(precio)
    costos.append(costo)

# Filtrar valores válidos
precios_validos = [p for p in precios if p > 0]
costos_validos = [c for c in costos if c > 0 and costos.index(c) < len(precios) and precios[costos.index(c)] > 0]

margenes = []
for p, c in zip(precios_validos, costos_validos):
    if p > c:
        margen = ((p - c) / p) * 100
        margenes.append(margen)

if margenes:
    margen_promedio = sum(margenes) / len(margenes)
    st.info(f"📈 Margen de utilidad promedio: {margen_promedio:.2f}%")

    if margen_promedio < 20:
        st.error("🔴 Margen bajo. Considera revisar tus precios o costos.")
    elif margen_promedio < 40:
        st.warning("🟡 Margen aceptable. Hay oportunidad de mejora.")
    else:
        st.success("🟢 Buen margen. Tu negocio está sano en rentabilidad.")
else:
    st.warning("Ingresa precios y costos válidos para calcular el margen.")

# 4. Cálculo del Punto de Equilibrio
st.header("4️⃣ Punto de Equilibrio")
st.markdown("📌 **¿Qué es el punto de equilibrio?** Es el nivel mínimo de ventas que necesitas para cubrir todos tus costos. Si vendes menos, pierdes; si vendes más, empiezas a ganar. Saber esto te da claridad para tomar decisiones con rumbo.")

if precios_validos and costos_validos:
    precio_promedio = sum(precios_validos) / len(precios_validos)
    costo_variable_promedio = sum(costos_validos) / len(costos_validos)
    utilidad_unitaria = precio_promedio - costo_variable_promedio

    if utilidad_unitaria > 0:
        punto_equilibrio = total_costos_fijos / utilidad_unitaria
        st.success(f"🔁 Punto de Equilibrio: Necesitas vender **{punto_equilibrio:.0f} unidades promedio** al mes para cubrir tus costos.")
        
        if punto_equilibrio > 100:
            st.error("🔴 Punto de equilibrio alto. Revisa tus márgenes o gastos fijos.")
        elif punto_equilibrio > 50:
            st.warning("🟡 Punto de equilibrio moderado. Hay margen de optimización.")
        else:
            st.success("🟢 Punto de equilibrio saludable. Estás en buen camino.")
    else:
        st.error("Tu utilidad por unidad es cero o negativa. No es posible calcular el punto de equilibrio.")
else:
    st.info("Ingresa al menos un precio y costo válido para calcular el punto de equilibrio.")
