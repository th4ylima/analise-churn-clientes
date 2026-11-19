# Análise de Churn de Clientes

Projeto de análise exploratória de dados em Python para entender o cancelamento (churn) de clientes de um serviço por assinatura, com exportação da base tratada para visualização no Power BI.

> Os dados são **fictícios** e foram criados apenas para fins de estudo. Os resultados não representam nenhuma empresa real.

## Objetivo

Responder, com estatística descritiva, perguntas básicas de negócio:

- Qual é a taxa geral de churn?
- Quem cancela costuma ser mais jovem?
- O tipo de contrato (mensal, trimestral ou anual) influencia o cancelamento?

## Tecnologias

- **Python**
- **Pandas** — criação do DataFrame, agrupamentos e tabelas cruzadas
- **Power BI** — visualização da base tratada

## Base de dados

Base simulada com **15 clientes**, criada diretamente no código (`analise.py`), com as colunas:

| Coluna | Descrição |
|---|---|
| `id_cliente` | Identificador do cliente |
| `idade` | Idade do cliente |
| `tipo_contrato` | Mensal, Trimestral ou Anual |
| `mensalidade` | Valor da mensalidade |
| `meses_contrato` | Duração do contrato em meses |
| `cancelou` | 1 = cancelou, 0 = ativo |

## Principais resultados

| Indicador | Resultado |
|---|---|
| Taxa geral de churn | **40%** (6 de 15 clientes) |
| Idade média dos clientes ativos | 36,4 anos |
| Idade média dos clientes que cancelaram | 37,3 anos |

**Cancelamentos por tipo de contrato**

| Tipo de contrato | Ativos | Cancelaram |
|---|---|---|
| Mensal | 2 | 6 |
| Trimestral | 3 | 0 |
| Anual | 4 | 0 |

## Insights

- **O tipo de contrato é o fator que mais se destaca:** todos os cancelamentos vieram de contratos mensais (6 de 8 clientes mensais cancelaram), e nenhum cliente trimestral ou anual cancelou.
- **A idade quase não diferencia os grupos:** a hipótese de que quem cancela é mais jovem **não se confirmou** nesta base. A diferença entre as médias é de menos de 1 ano.
- **Sugestão de negócio:** incentivar a migração de clientes mensais para planos trimestrais ou anuais, por exemplo com desconto.

## Limitações

- A base tem apenas 15 registros, então os resultados servem como exercício e não permitem conclusões estatísticas sólidas.
- Os dados são simulados.
- Não há variáveis como motivo do cancelamento, canal de aquisição ou uso do serviço, que enriqueceriam a análise.

## Dashboard

![Dashboard](dashboard.png)

<!-- Confirme se o dashboard foi feito no Power BI e ajuste esta seção se necessário. -->

## Como executar

```bash
git clone https://github.com/th4ylima/analise-churn-clientes.git
cd analise-churn-clientes
pip install pandas
python analise.py
```

O script imprime os indicadores no terminal e gera o arquivo `dados_clientes_limpos.csv`, usado para montar o dashboard no Power BI.

## Próximos passos

- Repetir a análise com uma base real e maior.
- Calcular o churn por faixa de idade e por valor de mensalidade.
- Adicionar gráficos em Python (Matplotlib ou Plotly).
- Testar um modelo simples de previsão de churn.

## Autoria

**Thayna Lima Rezende**
[LinkedIn](https://linkedin.com/in/thaynalimarezende) · [GitHub](https://github.com/th4ylima)
