import streamlit as st

# CSS para alinear las columnas
st.markdown("""
<style>
    /* Hace la app más ancha */
    .stMainBlockContainer {
        max-width: 100%;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    /* Estilo para number_input */
    .stNumberInput input {
        font-size: 18px;
        text-align: center;
    }
    /* Hace que el markdown tenga la misma altura que el input */
    .stMarkdown {
        min-height: 42px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .stMarkdown h3 {
        text-align: center;
        font-size: 18px;
        margin: 0;
        padding: 0;
    }
</style>
""", unsafe_allow_html=True)


st.title("CUADRE CIERRE DE CAJA",text_alignment="center")

col1s, col2s = st.columns(2, gap="large")

with col1s:

    with st.container(border=True):
        st.subheader("Conteo de Efectivo",text_alignment="center")
        
        #creo dos columnas
        col1, col2, col3 = st.columns(3)

        with col1:
                st.markdown("### $50")
                st.markdown("### $100") 
                st.markdown("### $200") 
                st.markdown("### $500") 
                st.markdown("### $1.000") 
                st.markdown("### $2.000") 
                st.markdown("### $5.000") 
                st.markdown("### $10.000") 
                st.markdown("### $20.000") 
                st.markdown("### $50.000") 
                st.markdown("### $100.000") 


        with col2:
            
            val50 = st.number_input("$50", min_value=0, step=1, label_visibility="collapsed")
            val100 = st.number_input("$100", min_value=0, step=1, label_visibility="collapsed")
            val200 = st.number_input("$200", min_value=0, step=1, label_visibility="collapsed")
            val500 = st.number_input("$500", min_value=0, step=1, label_visibility="collapsed")
            val1000 = st.number_input("$1.000", min_value=0, step=1, label_visibility="collapsed")
            val2000 = st.number_input("$2.000", min_value=0, step=1, label_visibility="collapsed")
            val5000 = st.number_input("$5.000", min_value=0, step=1, label_visibility="collapsed")
            val10000 = st.number_input("$10.000", min_value=0, step=1, label_visibility="collapsed")
            val20000 = st.number_input("$20.000", min_value=0, step=1, label_visibility="collapsed")
            val50000 = st.number_input("$50.000", min_value=0, step=1, label_visibility="collapsed")
            val100000 = st.number_input("$100.000", min_value=0, step=1, label_visibility="collapsed")
            

    
        with col3:
            st.markdown(f"### ${val50*50:,.0f}".replace(",", "."),text_alignment="center")
            st.markdown(f"### ${val100*100:,.0f}".replace(",", "."),text_alignment="center")
            st.markdown(f"### ${val200*200:,.0f}".replace(",", "."),text_alignment="center")   
            st.markdown(f"### ${val500*500:,.0f}".replace(",", "."),text_alignment="center")   
            st.markdown(f"### ${val1000*1000:,.0f}".replace(",", "."),text_alignment="center")   
            st.markdown(f"### ${val2000*2000:,.0f}".replace(",", "."),text_alignment="center")   
            st.markdown(f"### ${val5000*5000:,.0f}".replace(",", "."),text_alignment="center")   
            st.markdown(f"### ${val10000*10000:,.0f}".replace(",", "."),text_alignment="center")   
            st.markdown(f"### ${val20000*20000:,.0f}".replace(",", "."),text_alignment="center")   
            st.markdown(f"### ${val50000*50000:,.0f}".replace(",", "."),text_alignment="center") 
            st.markdown(f"### ${val100000*100000:,.0f}".replace(",", "."),text_alignment="center")   

        # Calcular el total
        total = (val50*50 + val100*100 + val200*200 + val500*500 + val1000*1000 + 
                val2000*2000 + val5000*5000 + val10000*10000 + val20000*20000 + 
                val50000*50000 + val100000*100000)
        st.divider()
        st.subheader(f"TOTAL ${total:,.0f}".replace(",", "."), text_alignment="center")


with col2s:

    with st.container(border=True):
        st.subheader("Cuadre de caja",text_alignment="center")

        col2_1,col2_2,col2_3 = st.columns(3)

        with col2_1:
             st.markdown("### TOTAL VENTAS")
             st.markdown("### BASE")
        with col2_2:
             total_ventas = st.number_input("total ventas", min_value=0, step=1, label_visibility="collapsed")
             base = st.number_input("base", min_value=0, step=1, label_visibility="collapsed")
        with col2_3:
             st.markdown(f"### ${total_ventas:,.0f}".replace(",", "."),text_alignment="center")
             st.markdown(f"### ${base:,.0f}".replace(",", "."),text_alignment="center")       

        st.divider()
        st.subheader(f"DIFERENCIA EFECTIVO VS VENTAS) ${total - total_ventas:,.0f}".replace(",", "."),text_alignment="center")  
        st.subheader(f"TOTAL (VENTA - BASE) ${total_ventas - base:,.0f}".replace(",", "."),text_alignment="center")

    # Sugerido para la base
    with st.container(border=True):
        st.subheader("💰 Sugerido para BASE", text_alignment="center")
        
        # Denominaciones pequeñas (monedas y billetes pequeños) - se usan TODAS primero
        denom_pequenas = [
            (50, val50, "$50"),
            (100, val100, "$100"),
            (200, val200, "$200"),
            (500, val500, "$500"),
            (1000, val1000, "$1.000"),
            (2000, val2000, "$2.000"),
        ]
        
        # Denominaciones grandes (billetes) - se usan para completar
        denom_grandes = [
            (5000, val5000, "$5.000"),
            (10000, val10000, "$10.000"),
            (20000, val20000, "$20.000"),
            (50000, val50000, "$50.000"),
            (100000, val100000, "$100.000"),
        ]
        
        # Calcular sugerido
        restante = base
        sugerido = {}
        
        if base > 0:
            # Paso 1: Usar TODAS las denominaciones pequeñas disponibles (hasta el límite de la base)
            total_pequenas = 0
            for valor, disponible, nombre in denom_pequenas:
                if disponible > 0:
                    usar = min(disponible, restante // valor)
                    if usar > 0:
                        sugerido[nombre] = int(usar)
                        total_pequenas += usar * valor
                        restante -= usar * valor
            
            # Paso 2: Completar con billetes grandes (de mayor a menor para usar menos billetes)
            for valor, disponible, nombre in reversed(denom_grandes):
                if restante <= 0:
                    break
                necesarios = restante // valor
                usar = min(necesarios, disponible)
                if usar > 0:
                    sugerido[nombre] = int(usar)
                    restante -= usar * valor
            
            # Paso 3: Si aún falta, intentar con combinaciones de billetes grandes
            if restante > 0:
                # Buscar si podemos usar un billete grande y devolver con pequeños
                for valor_g, disponible_g, nombre_g in reversed(denom_grandes):
                    if disponible_g > 0 and valor_g > restante:
                        diferencia = valor_g - restante
                        # Verificar si podemos "devolver" la diferencia con lo que ya no usamos
                        puede_devolver = True
                        temp_devolver = diferencia
                        for valor_p, disponible_p, nombre_p in reversed(denom_pequenas):
                            max_devolver = disponible_p - sugerido.get(nombre_p, 0)
                            if max_devolver > 0:
                                usar_dev = min(max_devolver, temp_devolver // valor_p)
                                temp_devolver -= usar_dev * valor_p
                        
                        if temp_devolver == 0:
                            # Podemos usar este billete grande
                            sugerido[nombre_g] = sugerido.get(nombre_g, 0) + 1
                            restante = 0
                            break
        
        # Mostrar sugerido
        if base > 0:
            col_s1, col_s2, col_s3 = st.columns(3)
            
            with col_s1:
                st.markdown("**Denominación**")
            with col_s2:
                st.markdown("**Cantidad**")
            with col_s3:
                st.markdown("**Total**")
            
            # Ordenar por valor de denominación
            orden_denom = ["$50", "$100", "$200", "$500", "$1.000", "$2.000", "$5.000", "$10.000", "$20.000", "$50.000", "$100.000"]
            
            total_sugerido = 0
            for nombre in orden_denom:
                if nombre in sugerido:
                    cantidad = sugerido[nombre]
                    valor_num = int(nombre.replace("$", "").replace(".", ""))
                    subtotal = cantidad * valor_num
                    total_sugerido += subtotal
                    
                    with col_s1:
                        st.markdown(f"{nombre}")
                    with col_s2:
                        st.markdown(f"{cantidad}")
                    with col_s3:
                        st.markdown(f"${subtotal:,.0f}".replace(",", "."))
            
            st.divider()
            st.markdown(f"**Total sugerido: ${total_sugerido:,.0f}**".replace(",", "."))
            
            if restante > 0:
                st.warning(f"⚠️ Faltan ${restante:,.0f} para completar la base (no hay suficiente efectivo disponible)".replace(",", "."))
            else:
                st.success("✅ Base completa")
        else:
            st.info("Ingresa el valor de la BASE para ver el sugerido")      


st.write("")
st.write("")
st.subheader("Creado con mucho amor para la negrita ♥",text_alignment="center")                