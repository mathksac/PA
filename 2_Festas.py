import streamlit as st
from datetime import date, timedelta
from tema import aplicar_tema

# Configuração da página
st.set_page_config(
    page_title="Festas na Sorveteria | Gelato Vero",
    page_icon="🎂",
    layout="wide"
)
aplicar_tema()

# --- BARRA LATERAL ---
with st.sidebar:
    st.title("🍨 Gelato Vero")
    st.caption("Celebre momentos especiais com gelatos naturais.")
    st.divider()
    st.markdown('<div class="sidebar-aviso">🎉 <b>Eventos Exclusivos:</b> Nossas festas acontecem exclusivamente no salão da sorveteria com pacotes fechados.</div>', unsafe_allow_html=True)

# --- DADOS DOS PACOTES FECHADOS ---
pacotes = {
    "Festa Essencial (Até 20 convidados)": {
        "preco": 1200.00,
        "duracao": "2h30 de salão reservado",
        "sabores_qtd": 3,
        "incluso": [
            "Buffet livre de 3 sabores tradicionais de polpa natural",
            "Casquinhas crocantes e copinhos biodegradáveis",
            "1 atendente exclusivo servindo no balcão",
            "Mesa principal decorada em estilo artesanal"
        ]
    },
    "Festa Tradição (Até 40 convidados)": {
        "preco": 2200.00,
        "duracao": "3h30 de salão reservado",
        "sabores_qtd": 4,
        "incluso": [
            "Buffet livre de 4 sabores tradicionais de polpa natural",
            "Casquinhas, cascões artesanais e copinhos",
            "Caldas naturais de frutas da estação",
            "2 atendentes exclusivos + área reservada para parabéns"
        ]
    },
    "Festa Vero Completa (Até 60 convidados)": {
        "preco": 3100.00,
        "duracao": "4h de salão fechado exclusivamente para o evento",
        "sabores_qtd": 6,
        "incluso": [
            "Salão 100% fechado para sua família e amigos",
            "Buffet livre de 6 sabores tradicionais de polpa natural",
            "Estação completa com cascões, caldas naturais e frutas picadas",
            "Equipe completa de atendimento + lembrancinha artesanal"
        ]
    }
}

sabores_disponiveis = [
    "Morango Silvestre",
    "Manga Palmer Tradicional",
    "Maracujá Azedinho",
    "Limão Siciliano",
    "Coco da Fazenda",
    "Goiaba Vermelha"
]

# --- CABEÇALHO ---
st.title("Faça sua Festa na Gelato Vero 🎂🍨")
st.write("Oferecemos **pacotes fechados** com estrutura completa e nossos autênticos sorvetes de polpa natural.")

st.subheader("1. Conheça Nossos Pacotes Fechados")

# Exibição dos 3 pacotes em colunas
cols = st.columns(3)
for idx, (nome_pacote, info) in enumerate(pacotes.items()):
    with cols[idx]:
        itens_html = "".join([f"<li>{item}</li>" for item in info["incluso"]])
        st.markdown(f"""
        <div class="pacote-card">
            <h4>{nome_pacote}</h4>
            <div class="preco-destaque">R$ {info['preco']:,.2f}</div>
            <p><b>⏱️ Duração:</b> {info['duracao']}</p>
            <p><b>🍨 Sabores inclusos:</b> Escolha até {info['sabores_qtd']} sabores</p>
            <hr>
            <ul>{itens_html}</ul>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# --- SIMULADOR E PRÉ-RESERVA INTERATIVA ---
st.subheader("2. Monte sua Solicitação de Reserva")

col_form1, col_form2 = st.columns(2)

with col_form1:
    pacote_escolhido = st.selectbox("Escolha o pacote fechado:", list(pacotes.keys()))
    dados_pacote = pacotes[pacote_escolhido]

    data_minima = date.today() + timedelta(days=7)
    data_festa = st.date_input(
        "Data desejada para o evento (mínimo 7 dias de antecedência):",
        value=data_minima,
        min_value=data_minima
    )

    turno = st.radio("Turno preferido:", ["Tarde (14h às 18h)", "Noite (18h30 às 22h30)"], horizontal=True)

with col_form2:
    limite_sabores = dados_pacote["sabores_qtd"]
    sabores_festa = st.multiselect(
        f"Selecione até {limite_sabores} sabores tradicionais para servir na festa:",
        sabores_disponiveis,
        max_selections=limite_sabores
    )

    nome_cliente = st.text_input("Seu nome completo:")
    telefone_cliente = st.text_input("Seu WhatsApp para confirmação:")

# --- RESUMO E CONFIRMAÇÃO ---
if st.button("📋 Gerar Resumo da Pré-Reserva", type="primary"):
    if not nome_cliente or not telefone_cliente:
        st.markdown('<div class="destaque-box">❌ <b>Atenção:</b> Por favor, preencha seu nome e WhatsApp para gerar a solicitação.</div>', unsafe_allow_html=True)
    elif len(sabores_festa) == 0:
        st.markdown('<div class="destaque-box">⚠️ <b>Atenção:</b> Selecione pelo menos 1 sabor tradicional para o cardápio da sua festa.</div>', unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="destaque-box">
            <h4>✅ Solicitação de pré-reserva gerada com sucesso!</h4>
            <p><b>🧾 Resumo do Pedido de Reserva — Gelato Vero</b></p>
            <ul>
                <li><b>Responsável:</b> {nome_cliente} ({telefone_cliente})</li>
                <li><b>Pacote Selecionado:</b> {pacote_escolhido}</li>
                <li><b>Data e Turno:</b> {data_festa.strftime('%d/%m/%Y')} — {turno}</li>
                <li><b>Sabores Escolhidos ({len(sabores_festa)}/{limite_sabores}):</b> {', '.join(sabores_festa)}</li>
                <li><b>Investimento Total (Pacote Fechado):</b> R$ {dados_pacote['preco']:,.2f}</li>
            </ul>
            <p><i>Nossa equipe entrará em contato via WhatsApp em até 24h para confirmar a disponibilidade da agenda.</i></p>
        </div>
        """, unsafe_allow_html=True)
