# Jogo da Forca

from Palavras import palavras_dificeis, palavras_faceis, palavras_medias
import random


def selecionar_palavra(dificuldade):
    banco = {
        "facil": palavras_faceis,
        "medio": palavras_medias,
        "dificil": palavras_dificeis
    }

    if dificuldade not in banco:
        raise ValueError("Dificuldade inválida.")

    return random.choice(banco[dificuldade]).lower()


def jogar_forca():
    print("=== JOGO DA FORCA ===")

    # escolher dificuldade
    dificuldade = input("Escolha a dificuldade (facil/medio/dificil): ").lower()
    palavra = selecionar_palavra(dificuldade)

    letras_descobertas = ["_"] * len(palavra)
    letras_usadas = set()
    tentativas = 6

    while tentativas > 0 and "_" in letras_descobertas:
        print("\nPalavra:", " ".join(letras_descobertas))
        print("Tentativas restantes:", tentativas)
        print("Letras usadas:", " ".join(sorted(letras_usadas)))

        chute = input("Digite uma letra: ").lower().strip()

        # validações
        if len(chute) != 1 or not chute.isalpha():
            print("Digite apenas UMA letra válida.")
            continue

        if chute in letras_usadas:
            print("Você já tentou essa letra.")
            continue

        letras_usadas.add(chute)

        # verifica acerto
        if chute in palavra:
            print("✅ Acertou!")
            for i, letra in enumerate(palavra):
                if letra == chute:
                    letras_descobertas[i] = letra
        else:
            print("❌ Errou!")
            tentativas -= 1

    # resultado final
    if "_" not in letras_descobertas:
        print("\n🎉 Parabéns! Você venceu!")
    else:
        print("\n💀 Você perdeu!")
        print("A palavra era:", palavra)


# ▶️ iniciar jogo
if __name__ == "__main__":
    jogar_forca()