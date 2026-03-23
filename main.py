import random
import json

# lista de usuários fictícios
usuarios = [
    {"id": 1, "nome": "João", "saldo": 1500.75, "limite": 3000},
    {"id": 2, "nome": "Maria", "saldo": 200.00, "limite": 2000},
    {"id": 3, "nome": "Carlos", "saldo": 50.00, "limite": 500},
    {"id": 4, "nome": "Ana", "saldo": 3200.90, "limite": 5000},
]

# mensagens base (simulando IA)
mensagens_base = [
    "Temos uma oportunidade especial para você!",
    "Que tal aproveitar uma condição exclusiva?",
    "Preparamos uma oferta personalizada!",
    "Você foi selecionado para um benefício especial!"
]


def gerar_mensagem(usuario):
    base = random.choice(mensagens_base)

    if usuario["saldo"] < 100:
        return (
            f"Olá {usuario['nome']}, {base} "
            f"Sabemos que seu saldo está baixo. "
            f"Que tal um crédito de até R${usuario['limite']}?"
        )

    elif usuario["saldo"] < 1000:
        return (
            f"Olá {usuario['nome']}, {base} "
            f"Você pode aumentar seu limite para até R${usuario['limite'] * 1.5:.2f}!"
        )

    else:
        return (
            f"Olá {usuario['nome']}, {base} "
            f"Invista seu saldo de R${usuario['saldo']:.2f} "
            f"e faça seu dinheiro render mais!"
        )


def executar_pipeline():
    print("🚀 Iniciando geração de mensagens...\n")

    resultados = []

    for usuario in usuarios:
        mensagem = gerar_mensagem(usuario)

        resultado = {
            "id": usuario["id"],
            "nome": usuario["nome"],
            "mensagem": mensagem
        }

        resultados.append(resultado)

        print(f"📩 Mensagem para {usuario['nome']}:")
        print(mensagem)
        print("-" * 50)

    # salva saída em JSON (simulando etapa LOAD)
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(resultados, f, indent=4, ensure_ascii=False)

    print("\n✅ Processo finalizado! Arquivo 'output.json' gerado.")


if __name__ == "__main__":
    executar_pipeline()
