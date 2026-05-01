## 💰 MD.Edu - Tesoureiro de Teyvat (Educador de Mora)
Um agente de IA Generativa inspirado em Genshin Impact que ensina viajantes a gerirem suas Moras e recursos dentro do jogo de forma didática e divertida.

## 🌟 Por que um agente de Genshin Impact?
Para este desafio de projeto da DIO, optei por criar um agente fictício voltado ao universo de Genshin Impact em vez de um assistente financeiro real.

### Os motivos principais são:

1. **Segurança e Privacidade:** Ao lidar com dados de um jogo, eliminamos qualquer risco de exposição de dados bancários reais durante os testes de estudo.

2. **Criatividade e Engajamento:** Aplicar conceitos de IA (como RAG e System Prompts) em um cenário de entretenimento demonstra a versatilidade da tecnologia.

3. **Foco Educativo:** O objetivo é testar o conhecimento técnico sobre integração de IA e Python, usando a economia do jogo (Mora, Resina, Itens) como uma metáfora perfeita para finanças reais.

## 💡 O Que o MD.Edu Faz?
O MD.Edu é o seu consultor do Banco do Norte em Liyue. Ele analisa seu "extrato de Teyvat" e te ajuda a não ficar pobre antes do próximo banner.

- **✅ Analisa Gastos:** Identifica se você está gastando muita Mora com comida ou ascensões desnecessárias.

- **✅ Sugere Farms:** Explica como funcionam as Linhas Ley, Comissões e o Abismo.

- **✅ Linguagem Imersiva:** Responde com gírias e referências ao jogo (Lore-friendly).

- **❌ Não dá dicas de combate:** O foco dele é estritamente financeiro/recursos.

- **❌ Não recomenda gastos reais:** Ele lida apenas com a moeda fictícia do jogo (Mora).

## 🏗️ Arquitetura do Projeto
Nesta versão, utilizamos a nuvem para processamento, garantindo leveza e rapidez sem necessidade de downloads pesados.
'''
Snippet de código
flowchart TD
    A[Viajante/Usuário] --> B[Streamlit - Interface]
    B --> C[Google Gemini 2.0 Flash - IA]
    C --> D[Base de Dados CSV/JSON - Teyvat]
    D --> C
    C --> E[Resposta do MD.Edu]
'''
**Stack Tecnológica:**

- **Linguagem:** Python

- **Interface:** Streamlit

- **Cérebro (LLM):** Google Gemini 2.0 Flash (via API)

- **Dados:** Pandas para manipulação de CSV/JSON mockados

## 📁 Estrutura de Arquivos
'''
├── data/                          # Base de conhecimento de Teyvat
│   ├── perfil_investidor.json     # Perfil do Viajante e Objetivos
│   ├── transacoes.csv             # Histórico de gastos (Artefatos, Comida, etc)
│   ├── historico_atendimento.csv  # Conversas passadas
│   └── produtos_financeiros.json  # Métodos de Farm (Linhas Ley, etc)
│
├── src/
│   └── app.py                     # Código principal da aplicação
└── README.md                      # Você está aqui!
'''
## 🚀 Como Executar
**1. Obter uma API Key do Gemini**
O projeto utiliza a API do Google. Você pode gerar uma chave gratuita no Google AI Studio.

**2. Instalar Dependências**
'''
Bash
pip install streamlit pandas google-generativeai
'''
**3. Rodar a Aplicação**
'''
Bash
streamlit run src/app.py
'''
## 📝 Exemplo de Interação
**Usuário:** "Edu, gastei 500k de Mora hoje, estou mal?"

**MD.Edu:** "Pelas barbas de Barbatos, Viajante! Vi aqui no seu extrato que você torrou tudo em fortalecimento de artefatos azuis... Isso é um contrato terrível com a sua carteira! Que tal focarmos nas Comissões Diárias amanhã para recuperar esse prejuízo? Contratos devem ser cumpridos!"

## 👨‍💻 Desenvolvido por
Matthew - Gemini (README e como copiloto de código).
Projeto desenvolvido para a trilha de IA da DIO.
