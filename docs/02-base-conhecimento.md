# Base de Conhecimento

> [!TIP]
> **Prompt usado para esta etapa:**
> 
> Organize a base de conhecimento do agente "MD.Edu" usando os 4 arquivos da pasta `data/` (em anexo). Explique pra que serve cada arquivo e monte um exemplo de contexto formatado que será enviado pro LLM. Preencha o template abaixo.
>

## Dados Utilizados

| Arquivo | Formato | Para que serve no MD.Edu? |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores, ou seja, dar continuidade ao atendimento de forma mais eficiente. |
| `perfil_investidor.json` | JSON | Personalizar as explicações sobre as dúvidas e necessidades de aprendizado do cliente. |
| `produtos_financeiros.json` | JSON | Conhecer os produtos disponíveis para que eles possam ser ensinados ao cliente. |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente e usar essas informações de forma didática. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Inves de investimento real, decidi criar um agente para investimento de uma moeda fictícia dentro de Genshin Impact! Porque ganhar mais Mora é sempre bom.

```text
DADOS E PERFIL DO CLIENTE (data/perfil_investidor.json):
{
  "nome": "Lucas Genshin Silva",
  "idade": 6,
  "profissao": "Game Designer",
  "renda_mensal": 5000.00,
  "perfil_investidor": "Moderado",
  "objetivo_principal": "Intercâmbio no Canadá em 2026",
  "patrimonio_total": 45000.00,
  "reserva_emergencia_atual": 12000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

TRANSACOES DO CLIENTE (data/transacoes.csv):
data,descricao,categoria,valor,tipo
2025-10-01,Recompensa do Abismo,receita,600000.00,entrada
2025-10-02,Fortalecimento de Artefato,ascensao,150000.00,saida
2025-10-03,Restaurante Wanmin (Comida),alimentacao,25000.00,saida
2025-10-05,Passe de Batalha (Gnostic),lazer,120000.00,saida
2025-10-07,Ferreiro (Refinamento),armas,89000.00,saida
2025-10-10,Ingredientes com a Sara,alimentacao,12000.00,saida
2025-10-15,Ascensão de Personagem (Lvl 80),progresso,250000.00,saida
2025-10-15,Melhorando 50 Armas 1 Estrelas que não vai usar(Lvl 70),progresso,800000.00,saida

HISTORICO DE ATENDIMENTO DO CLIENTE (data/historico_atendimento.csv):
data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim
2025-10-15,chat,Cartão Internacional,Dúvida sobre taxas de IOF para viagem,sim
2025-10-22,chat,Criptoativos,Pediu explicação sobre ETF de Bitcoin,sim
2025-11-01,email,Seguro Viagem,Solicitou cotação para cobertura na América do Norte,sim
2025-11-05,chat,Reserva,Verificou quanto falta para a meta de intercâmbio,sim
2025-11-10,telefone,Aumento de limite,Solicitação aprovada para gastos na viagem,sim

PRODUTOS DISPONIVEIS PARA ENSINO (data/produtos_financeiros.json):
[
  {
    "nome": "Comissões Diárias",
    "categoria": "renda_fixa_teyvat",
    "risco": "zero",
    "rentabilidade": "Mora Garantida + Gemas",
    "esforço_minimo": "10 min",
    "indicado_para": "Todo viajante que quer o básico garantido"
  },
  {
    "nome": "Linha Ley (Flor da Riqueza)",
    "categoria": "investimento_resina",
    "risco": "baixo",
    "rentabilidade": "60.000 Mora por 20 Resinas",
    "esforço_minimo": "Gasto de Resina",
    "indicado_para": "Quem precisa de liquidez imediata para subir personagens"
  },
  {
    "nome": "Contratos de Recompensa (Bounties)",
    "categoria": "reputacao",
    "risco": "medio",
    "rentabilidade": "Alta (Mora + XP Reputação)",
    "esforço_minimo": "Caça a monstros elite",
    "indicado_para": "Viajantes que já possuem um time sólido"
  },
  {
    "nome": "Espiral do Abismo",
    "categoria": "alto_risco",
    "risco": "alto",
    "rentabilidade": "Massiva (Mora, Gemas e Artefatos)",
    "esforço_minimo": "Combate de elite",
    "indicado_para": "Veteranos buscando maximizar patrimônio"
  }
]
```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

O exemplo de contexto montado abaixo, se baiseia nos dados originais da base de conhecimento, mas os sintetiza deixando apenas as informações mais relevantes, otimizando assim o consumo de tokens. Entretanto, vale lembrar que mais importante do que economizar tokens, é ter todas as informações relevantes disponíveis em seu contexto.

```
DADOS DO CLIENTE:
- Nome: João Silva
- Perfil: Moderado
- Objetivo: Levar a Skirk para Lvl 90
- Reserva atual: Mora 100.000 (meta: Mora 150.000)

RESUMO DE GASTOS:
- Compras do dia a dia dentro do jogo: Mora 1.380
- Alimentação no restaurante da Xiangling: Mora 570
- Saúde (comprando comidas que curam): Mora 188
- Lazer (comprando itens aleatorios dentro do jogo): Mora 55,90
- Total de saídas: Mora 2.488,90

PRODUTOS DISPONÍVEIS PARA EXPLICAR:
- Ley Lines (risco alto)
- Abismo (risco alto)
- Teatro (risco médio)
- Comissões Diárias (risco baixo)
- Códigos (risco zero)
```
