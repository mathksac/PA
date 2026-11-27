import os
import base64
import streamlit as st

PASTA_ATUAL = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_ATUAL, "imagens")

TEMAS = {
    "🍦 Creme (Baunilha)": {
        "fundo": "#FFFDF9",
        "card": "#F7EFE5",
        "sidebar": "#F3E5D8",
        "texto": "#3B2313",
        "destaque": "#D97736",
        "preco": "#2E6F40",
        "botao_texto": "#FFFFFF",
        "banner": os.path.join(PASTA_IMAGENS, "banner_creme.png")
    },
    "🍫 Chocolate": {
        "fundo": "#241410",
        "card": "#3B231C",
        "sidebar": "#1A0E0B",
        "texto": "#FFF5EE",
        "destaque": "#E07A38",
        "preco": "#F4C06A",
        "botao_texto": "#FFFFFF",
        "banner": os.path.join(PASTA_IMAGENS, "banner_chocolate.png")
    },
    "🌿 Pistache": {
        "fundo": "#F3F8F2",
        "card": "#E2EFE0",
        "sidebar": "#D3E6D0",
        "texto": "#1E3A24",
        "destaque": "#4C8C4A",
        "preco": "#2E6F40",
        "botao_texto": "#FFFFFF",
        "banner": os.path.join(PASTA_IMAGENS, "banner_pistache.png")
    },
    "🍓 Morango": {
        "fundo": "#FFF5F7",
        "card": "#FFE3E8",
        "sidebar": "#FAD1DA",
        "texto": "#4A1525",
        "destaque": "#D84367",
        "preco": "#9E1B3B",
        "botao_texto": "#FFFFFF",
        "banner": os.path.join(PASTA_IMAGENS, "banner_morango.png")
    }
}

def _carregar_imagem_base64(caminho):
    with open(caminho, "rb") as f:
        return base64.b64encode(f.read()).decode()

def aplicar_tema():
    if "tema_sabor" not in st.session_state:
        st.session_state.tema_sabor = "🍦 Creme (Baunilha)"

    with st.sidebar:
        st.markdown("### 🎨 Sabor do Visual")
        escolha = st.selectbox(
            "Escolha a paleta do site:",
            list(TEMAS.keys()),
            index=list(TEMAS.keys()).index(st.session_state.tema_sabor),
            key="seletor_tema_global"
        )
        st.session_state.tema_sabor = escolha
        st.divider()

    t = TEMAS[st.session_state.tema_sabor]

    st.markdown(f"""
        <style>
        /* Fundo principal sem faixas brancas */
        html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {{
            background-color: {t['fundo']} !important;
            color: {t['texto']} !important;
        }}

        /* Barra superior transparente */
        header[data-testid="stHeader"] {{
            background: transparent !important;
        }}

        /* Espaçamento do topo */
        .block-container {{
            padding-top: 1.5rem !important;
            padding-bottom: 2rem !important;
        }}

        /* Barra lateral */
        section[data-testid="stSidebar"] {{
            background-color: {t['sidebar']} !important;
        }}

        /* Títulos e textos gerais */
        h1, h2, h3, h4, p, li, label, .stMarkdown, span {{
            color: {t['texto']} !important;
        }}

        /* Cards e avisos personalizados */
        .destaque-box, .sabor-card, .pacote-card, .sidebar-aviso {{
            background-color: {t['card']} !important;
            color: {t['texto']} !important;
            padding: 18px;
            border-radius: 12px;
            border-left: 5px solid {t['destaque']} !important;
            border-top: 5px solid {t['destaque']} !important;
            margin-bottom: 15px;
        }}
        .destaque-box *, .sabor-card *, .pacote-card *, .sidebar-aviso * {{
            color: {t['texto']} !important;
        }}

        /* Inputs, Selectboxes e listas suspensas */
        div[data-baseweb="select"] > div,
        div[data-baseweb="base-input"],
        input {{
            background-color: {t['card']} !important;
            color: {t['texto']} !important;
            border-color: {t['destaque']} !important;
        }}
        ul[data-baseweb="menu"], ul[data-baseweb="menu"] li {{
            background-color: {t['card']} !important;
            color: {t['texto']} !important;
        }}

        /* Preço em destaque */
        .preco-destaque {{
            font-size: 1.6em;
            font-weight: bold;
            color: {t['preco']} !important;
            margin: 10px 0;
        }}

        /* Botões */
        .stButton > button {{
            background-color: {t['destaque']} !important;
            color: {t['botao_texto']} !important;
            border: none !important;
        }}
        .stButton > button p {{
            color: {t['botao_texto']} !important;
        }}
        </style>
    """, unsafe_allow_html=True)

    # Renderiza a imagem diretamente via HTML em 100% da largura e 1 polegada (95px) de altura
    if os.path.exists(t["banner"]):
        img_b64 = _carregar_imagem_base64(t["banner"])
        st.markdown(
            f"""
            <img src="data:image/png;base64,{img_b64}"
                 style="width: 100%; height: 120px; object-fit: cover; object-position: top center; border-radius: 12px; display: block; margin-bottom: 15px;">
            """,
            unsafe_allow_html=True
        )
