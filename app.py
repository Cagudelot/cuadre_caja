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


st.write("")
st.write("")
st.subheader("Creado con mucho amor para la negrita ♥",text_alignment="center")                