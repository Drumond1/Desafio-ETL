# 🚀 Santander Dev Week 2023 - ETL com Python

Projeto desenvolvido como desafio da DIO (Digital Innovation One), com o objetivo de simular um pipeline de ETL utilizando Python e conceitos de IA generativa.

---

## 🧠 Objetivo

Gerar mensagens personalizadas para usuários fictícios com base em seus dados financeiros, simulando uma estratégia de marketing bancário.

---

## ⚙️ Tecnologias utilizadas

- Python 3
- Biblioteca padrão (random, json)

---

## 🔄 Etapas do ETL

### 📥 Extract
Os dados dos usuários são definidos diretamente no código como uma lista de dicionários.

### 🔄 Transform
Uma função (`gerar_mensagem`) cria mensagens personalizadas com base em:
- saldo
- limite disponível

### 📤 Load
Os resultados são salvos em um arquivo `output.json`.

---

## 📊 Exemplo de saída

```json
{
  "id": 1,
  "nome": "João",
  "mensagem": "Olá João, temos uma oportunidade especial para você! Invista seu saldo de R$1500.75 e faça seu dinheiro render mais!"
}
