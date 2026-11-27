import streamlit as st
from tema import aplicar_tema

# Configuração da página
st.set_page_config(
    page_title="Nossos Sabores | Gelato Vero",
    page_icon="🍓",
    layout="wide"
)
aplicar_tema()

# --- BARRA LATERAL ---
with st.sidebar:
    st.title("🍨 Gelato Vero")
    st.caption("Sabores batidos diariamente com polpa natural.")
    st.divider()
    st.markdown('<div class="sidebar-aviso">💡 <b>Consumo exclusivo no salão:</b> Nossos gelatos não são enviados por delivery para preservar a textura artesanal.</div>', unsafe_allow_html=True)

# --- BASE DE DADOS DOS SABORES TRADICIONAIS ---
sabores = [
    {
        "nome": "Morango Silvestre",
        "categoria": "Frutas Vermelhas",
        "polpa": "100% Polpa de Morango Fresco",
        "descricao": "Receita clássica da casa, levemente adocicada, com pedacinhos naturais da fruta.",
        "destaque": "Mais Pedido",
        "emoji": "🍓"
    },
    {
        "nome": "Manga Palmer Tradicional",
        "categoria": "Frutas Tropicais",
        "polpa": "100% Polpa de Manga Madura",
        "descricao": "Cremosidade natural da própria manga, sem adição de leite ou conservantes.",
        "destaque": "Zero Lactose",
        "emoji": "🥭"
    },
    {
        "nome": "Maracujá Azedinho",
        "categoria": "Frutas Cítricas",
        "polpa": "Polpa Natural com Sementes",
        "descricao": "Refrescante e intenso, equilibrando o azedinho da fruta com o ponto certo de doçura.",
        "destaque": "Refrescante",
        "emoji": "🟡"
    },
    {
        "nome": "Limão Siciliano",
        "categoria": "Frutas Cítricas",
        "polpa": "Suco e Raspas Naturais",
        "descricao": "Aromático e leve, ideal para limpar o paladar em dias quentes.",
        "destaque": "Zero Lactose",
        "emoji": "🍋"
    },
    {
        "nome": "Coco da Fazenda",
        "categoria": "Clássicos da Casa",
        "polpa": "Polpa e Leite de Coco Natural",
        "descricao": "Textura aveludada feita com coco fresco ralado na hora.",
        "destaque": "Tradição",
        "emoji": "🥥"
    },
    {
        "nome": "Goiaba Vermelha",
        "categoria": "Frutas Tropicais",
        "polpa": "100% Polpa de Goiaba Selecionada",
        "descricao": "Sabor marcante da fruta de pomar, com textura densa e tradicional.",
        "destaque": "Receita Antiga",
        "emoji": "🍈"
    }
]

# --- CABEÇALHO ---
st.title("Nossos Sabores Tradicionais 🍨")
st.write("Explore nossa vitrine feita exclusivamente com **polpas de frutas naturais**.")

# --- FILTROS INTERATIVOS ---
col_filtro1, col_filtro2 = st.columns([1, 2])

with col_filtro1:
    categorias = ["Todas as Categorias", "Frutas Tropicais", "Frutas Cítricas", "Frutas Vermelhas", "Clássicos da Casa"]
    categoria_escolhida = st.selectbox("Filtrar por família de sabor:", categorias)

with col_filtro2:
    busca = st.text_input("Buscar por nome ou fruta (ex: Manga, Coco, Morango):", "")

st.divider()

# --- LÓGICA DE FILTRAGEM ---
sabores_filtrados = []
for s in sabores:
    bate_categoria = (categoria_escolhida == "Todas as Categorias") or (s["categoria"] == categoria_escolhida)
    bate_busca = (busca.lower() in s["nome"].lower()) or (busca.lower() in s["descricao"].lower())
    if bate_categoria and bate_busca:
        sabores_filtrados.append(s)

# --- EXIBIÇÃO EM CARDS ---
if not sabores_filtrados:
    st.markdown('<div class="destaque-box">⚠️ Nenhum sabor encontrado com esse filtro. Tente limpar a busca!</div>', unsafe_allow_html=True)
else:
    cols = st.columns(2)
    for idx, sabor in enumerate(sabores_filtrados):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="sabor-card">
                <h3>{sabor['emoji']} {sabor['nome']}</h3>
                <p><b>🌿 {sabor['polpa']}</b> &nbsp;|&nbsp; <b>✨ {sabor['destaque']}</b></p>
                <p style="margin-top: 10px;">{sabor['descricao']}</p>
            </div>
            """, unsafe_allow_html=True)

st.divider()

# --- INTERAÇÃO EXTRA: COMBINAÇÃO SUGERIDA ---
st.subheader("🥄 Monte sua combinação ideal para pedir no balcão")
escolhas = st.multiselect(
    "Selecione até 3 sabores naturais para visualizar sua taça:",
    [s["nome"] for s in sabores],
    max_selections=3
)

if escolhas:
    st.markdown(f'<div class="destaque-box">✅ Ótima pedida! Sua taça no salão terá: <b>{", ".join(escolhas)}</b>. Peça diretamente ao nosso atendente!</div>', unsafe_allow_html=True)
