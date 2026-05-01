import json
import pandas as pd
import streamlit as st
import google.generativeai as genai

# ============ CONFIGURAÇÃO DO GEMINI ============
# Lembre-se de usar sua chave real aqui
GOOGLE_API_KEY = "SUA_CHAVE_AQUI" 
genai.configure(api_key=GOOGLE_API_KEY)

# Ótima escolha! O gemini-2.0-flash é super rápido e inteligente.
model = genai.GenerativeModel('gemini-2.0-flash')

# Configuração da página do Streamlit
st.set_page_config(page_title="MD.Edu - Tesoureiro de Teyvat", page_icon="💰")

# ============ CARREGAR DADOS ============
@st.cache_data
def carregar_dados():
    perfil = json.load(open('./data/perfil_investidor.json', encoding='utf-8'))
    transacoes = pd.read_csv('./data/transacoes.csv')
    historico = pd.read_csv('./data/historico_atendimento.csv')
    produtos = json.load(open('./data/produtos_financeiros.json', encoding='utf-8'))
    return perfil, transacoes, historico, produtos

perfil, transacoes, historico, produtos = carregar_dados()

# ============ MONTAR CONTEXTO DE TEYVAT ============
contexto = f"""
VIAJANTE: {perfil['nome']}, perfil {perfil['perfil_investidor']}
OBJETIVO NO JOGO: {perfil['objetivo_principal']}
RESERVA DE MORA: {perfil['patrimonio_total']} | INVESTIDO EM ITENS: {perfil['reserva_emergencia_atual']}

EXTRATO RECENTE DE GASTOS EM TEYVAT:
{transacoes.to_string(index=False)}

DIÁRIOS DE ATENDIMENTO ANTERIORES:
{historico.to_string(index=False)}

OPÇÕES DE "INVESTIMENTO" (FARM):
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ============ SYSTEM PROMPT (A PERSONALIDADE) ============
SYSTEM_PROMPT = """Você é o MD.Edu, o Tesoureiro de Teyvat e especialista em Mora.
Sua missão é ajudar viajantes a não ficarem pobres no Genshin Impact.

PERSONALIDADE:
- Você é engraçado, informal e usa gírias de Genshin (Resina, Artefatos, Arcontes, Paimon);
- Você é focado em economia de recursos do jogo.

REGRAS RÍGIDAS:
1. NUNCA dê dicas de finanças da vida real (dinheiro real, bancos reais, ações);
2. Se perguntarem sobre combate ou builds de dano, diga que seu negócio é apenas Mora e recursos;
3. Use os dados do 'EXTRATO RECENTE' para dar broncas ou elogios personalizados;
4. Se o viajante estiver gastando muito com "Comida" ou "Ascensão de Armas inúteis", avise-o;
5. Responda em no máximo 3 parágrafos curtos.
6. Sempre termine com uma frase de efeito como "Que o Arconte do Ouro te proteja!" ou "Contratos devem ser cumpridos!".
"""

# ============ FUNÇÃO PARA CHAMAR O GEMINI (A QUE FALTAVA!) ============
def perguntar_ao_edu(pergunta_usuario):
    try:
        # Unimos o System Prompt, o Contexto dos arquivos e a pergunta do usuário
        prompt_completo = f"{SYSTEM_PROMPT}\n\nCONTEXTO DO VIAJANTE:\n{contexto}\n\nPERGUNTA: {pergunta_usuario}"
        
        response = model.generate_content(prompt_completo)
        return response.text
    except Exception as e:
        return f"Pelas barbas de Barbatos! Ocorreu um erro na comunicação com Celestia: {e}"

# ============ INTERFACE UI/UX (STREAMLIT) ============
st.title("💰 MD.Edu: Tesoureiro de Teyvat")
st.markdown(f"**Bem-vindo, {perfil['nome']}!** Vamos organizar essas Moras para você não passar sufoco no próximo banner.")

# Exibição do Histórico de Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do Usuário
if prompt := st.chat_input("Pergunte sobre seus gastos ou como ganhar mais Mora..."):
    # Mostra mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Resposta do MD.Edu usando o Gemini
    with st.chat_message("assistant"):
        with st.spinner("Consultando os registros do Banco do Norte..."):
            resposta = perguntar_ao_edu(prompt)
            st.markdown(resposta)
            st.session_state.messages.append({"role": "assistant", "content": resposta})