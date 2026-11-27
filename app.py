import streamlit as st
from tema import aplicar_tema

# Configuração geral da página (sempre deve ser o primeiro comando Streamlit)
st.set_page_config(
    page_title="Gelato Vero | Tradição em Polpas Naturais",
    page_icon="🍨",
    layout="wide",
    initial_sidebar_state="expanded"
)
aplicar_tema()

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.title("🍨 Gelato Vero")
    st.caption("Tradição artesanal feita com 100% polpa de fruta natural.")
    st.divider()
    st.markdown('<div class="sidebar-aviso">👈 Use o menu acima para navegar entre nossos sabores, reservar sua festa ou acessar a gestão.</div>', unsafe_allow_html=True)
    st.markdown("**📍 Onde estamos:**\nRua das Frutas Naturais, 120 - Centro")
    st.markdown("**🕒 Horário:**\nTerça a Domingo, das 12h às 22h")

# --- CONTEÚDO DA PÁGINA INICIAL ---
st.title("Bem-vindo à Gelato Vero 🍓🥭🍋")
st.subheader("O verdadeiro sabor da fruta, batido com tradição e servido no nosso espaço.")

# Banner de boas-vindas
st.markdown("""
<div class="destaque-box">
    <h4>✨ Nossa Essência</h4>
    <p>Na <b>Gelato Vero</b>, não usamos essências artificiais nem corantes. Cada receita nasce da 
    <b>polpa natural selecionada</b>, respeitando o tempo e o sabor verdadeiro de cada estação. 
    Nosso salão foi pensado para reunir famílias, amigos e celebrar momentos inesquecíveis.</p>
</div>
""", unsafe_allow_html=True)

# Pilares da sorveteria em 3 colunas
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🌿 100% Polpa Natural")
    st.write("Trabalhamos exclusivamente com polpas de frutas frescas e receitas tradicionais passadas de geração em geração.")

with col2:
    st.markdown("### 🏡 Experiência no Local")
    st.write("Não fazemos delivery porque acreditamos que o gelato perfeito deve ser apreciado fresco, na hora, em nosso salão.")

with col3:
    st.markdown("### 🎉 Sua Festa Aqui")
    st.write("Reserve nossa sorveteria com pacotes fechados exclusivos e encante seus convidados com sabores naturais.")

st.divider()

# Chamada interativa para ação (Navegação rápida)
st.markdown("### O que você gostaria de fazer agora?")
btn_col1, btn_col2 = st.columns(2)

with btn_col1:
    if st.button("🍦 Conhecer Nossos Sabores", use_container_width=True):
        st.switch_page("pages/1_Nossos_Sabores.py")

with btn_col2:
    if st.button("🎂 Simular Festa na Sorveteria", use_container_width=True, type="primary"):
        st.switch_page("pages/2_Festas.py")
