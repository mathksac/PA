import streamlit as st
import pandas as pd
from tema import aplicar_tema

# Configuração da página
st.set_page_config(
    page_title="Gestão & Lucro | Gelato Vero",
    page_icon="📊",
    layout="wide"
)
aplicar_tema()

# --- BARRA LATERAL ---
with st.sidebar:
    st.title("🍨 Gelato Vero")
    st.caption("Área Administrativa e Controle de Margem.")
    st.divider()
    st.markdown('<div class="sidebar-aviso">🔒 <b>Meta Financeira:</b> Todo pacote ou produto deve manter margem de lucro mínima de <b>30%</b>.</div>', unsafe_allow_html=True)

st.title("Painel de Gestão & Margem de Lucro 📊")

# --- CONTROLE DE ACESSO POR SENHA ---
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.markdown('<div class="destaque-box">🔐 Esta área é restrita à administração da <b>Gelato Vero</b>. Digite a senha para acessar.</div>', unsafe_allow_html=True)
    senha = st.text_input("Senha de acesso:", type="password", placeholder="Dica: gelato30")
    if st.button("Entrar no Painel", type="primary"):
        if senha == "gelato30":
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.markdown('<div class="destaque-box">❌ <b>Senha incorreta.</b> Tente novamente.</div>', unsafe_allow_html=True)
    st.stop()

# Botão para sair do painel
if st.sidebar.button("🚪 Sair da Área Restrita"):
    st.session_state.autenticado = False
    st.rerun()

# --- SEÇÃO 1: AUDITORIA DOS PACOTES FECHADOS ATUAIS ---
st.subheader("1. Auditoria de Rentabilidade — Pacotes de Festa")
st.write("Acompanhamento automático da margem líquida sobre os preços praticados na página de Festas:")

dados_pacotes = [
    {"Pacote": "Festa Essencial (20 pessoas)", "Preço Venda (R$)": 1200.00, "Custo Polpas/Insumos (R$)": 420.00, "Custo Equipe/Espaço (R$)": 320.00},
    {"Pacote": "Festa Tradição (40 pessoas)", "Preço Venda (R$)": 2200.00, "Custo Polpas/Insumos (R$)": 780.00, "Custo Equipe/Espaço (R$)": 550.00},
    {"Pacote": "Festa Vero Completa (60 pessoas)", "Preço Venda (R$)": 3100.00, "Custo Polpas/Insumos (R$)": 1100.00, "Custo Equipe/Espaço (R$)": 780.00},
]

df = pd.DataFrame(dados_pacotes)
df["Custo Total (R$)"] = df["Custo Polpas/Insumos (R$)"] + df["Custo Equipe/Espaço (R$)"]
df["Lucro Líquido (R$)"] = df["Preço Venda (R$)"] - df["Custo Total (R$)"]
df["Margem (%)"] = (df["Lucro Líquido (R$)"] / df["Preço Venda (R$)"]) * 100
df["Status Meta (30%)"] = df["Margem (%)"].apply(lambda m: "✅ Meta Batida" if m >= 30 else "🚨 Abaixo de 30%")

st.dataframe(
    df.style.format({
        "Preço Venda (R$)": "R$ {:.2f}",
        "Custo Polpas/Insumos (R$)": "R$ {:.2f}",
        "Custo Equipe/Espaço (R$)": "R$ {:.2f}",
        "Custo Total (R$)": "R$ {:.2f}",
        "Lucro Líquido (R$)": "R$ {:.2f}",
        "Margem (%)": "{:.1f}%"
    }),
    use_container_width=True,
    hide_index=True
)

st.divider()

# --- SEÇÃO 2: SIMULADOR INTERATIVO DE PREÇO E MARGEM MÍNIMA ---
st.subheader("2. Simulador Interativo de Custos e Precificação (Trava de 30%)")
st.write("Ajuste os custos de polpas naturais, equipe e preço cobrado para testar novos pacotes ou reajustes:")

col_sim1, col_sim2 = st.columns(2)

with col_sim1:
    nome_simulacao = st.text_input("Nome do Pacote ou Item:", value="Novo Pacote Festa 30 Pessoas")
    custo_polpas = st.number_input("Custo com Polpas Naturais e Insumos (R$):", min_value=0.0, value=600.0, step=20.0)
    custo_fixo = st.number_input("Custo com Equipe, Energia e Salão (R$):", min_value=0.0, value=450.0, step=20.0)
    preco_pretendido = st.number_input("Preço de Venda Pretendido (R$):", min_value=1.0, value=1450.0, step=50.0)

# Cálculos financeiros em tempo real
custo_total = custo_polpas + custo_fixo
lucro_real = preco_pretendido - custo_total
margem_real = (lucro_real / preco_pretendido) * 100
# Preço mínimo para garantir exatamente 30% de margem sobre a venda: Custo / (1 - 0.30)
preco_minimo_30 = custo_total / 0.70

with col_sim2:
    st.markdown(f"#### Resultado da Simulação: *{nome_simulacao}*")
    m1, m2, m3 = st.columns(3)
    m1.metric("Custo Total", f"R$ {custo_total:,.2f}")
    m2.metric("Lucro Líquido", f"R$ {lucro_real:,.2f}")
    m3.metric("Margem Atual", f"{margem_real:.1f}%", delta=f"{margem_real - 30:.1f}% vs meta")

    st.write("")
    if margem_real >= 30.0:
        st.markdown(f"""
        <div class="destaque-box">
            <h4>✅ Aprovado!</h4>
            <p>Este valor garante <b>{margem_real:.1f}% de lucro</b>, superando a meta mínima de 30%.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        diferenca = preco_minimo_30 - preco_pretendido
        st.markdown(f"""
        <div class="destaque-box">
            <h4>🚨 Atenção: Margem abaixo de 30%!</h4>
            <p>Para atingir exatamente <b>30% de lucro</b> sobre este custo de R$ {custo_total:,.2f}, 
            o preço mínimo de venda deve ser <b>R$ {preco_minimo_30:,.2f}</b> (aumente pelo menos R$ {diferenca:,.2f}).</p>
        </div>
        """, unsafe_allow_html=True)
