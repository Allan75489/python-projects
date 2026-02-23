# Calculadora Cientifica

import math

# Função para soma
def soma(a, b):
    return a + b

# função para subtração
def subtracao(a, b):
    return a - b

# função de multiplicação
def multiplicacao(a, b):
    return a * b

# função de divisão
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Não é possível dividir por zero."

# funções científicas (em graus)
def seno(a):
    return math.sin(math.radians(a))

def cosseno(a):
    return math.cos(math.radians(a))

def tangente(a):
    return math.tan(math.radians(a))

def logaritmo(a):
    if a > 0:
        return math.log(a)
    else:
        return "Erro: o logaritmo só é definido para números positivos."

# Função para armazenar dados pessoais
def armazenar_dados():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    grau_academico = input("Qual o seu nível atual de estudo?: ")
    return nome, idade, grau_academico

# Função principal da calculadora
def calculadora():
    nome, idade, grau_academico = armazenar_dados()
    print(f"\nNome: {nome}, Idade: {idade}, Grau Acadêmico: {grau_academico}")

    while True:
        print("\nSelecione a operação desejada:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Seno")
        print("6. Cosseno")
        print("7. Tangente")
        print("8. Logaritmo (base e)")
        print("Digite 'sair' para encerrar")

        escolha = input("Opção: ").lower()

        if escolha == "sair":
            print("Encerrando calculadora...")
            break

        # Operações com dois números
        if escolha in ["1", "2", "3", "4"]:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))

            if escolha == "1":
                print("Resultado:", soma(a, b))
            elif escolha == "2":
                print("Resultado:", subtracao(a, b))
            elif escolha == "3":
                print("Resultado:", multiplicacao(a, b))
            elif escolha == "4":
                print("Resultado:", divisao(a, b))

        # Operações com um número
        elif escolha in ["5", "6", "7", "8"]:
            a = float(input("Digite o valor: "))

            if escolha == "5":
                print("Resultado:", seno(a))
            elif escolha == "6":
                print("Resultado:", cosseno(a))
            elif escolha == "7":
                print("Resultado:", tangente(a))
            elif escolha == "8":
                print("Resultado:", logaritmo(a))

        else:
            print("Opção inválida!")

# Executar
calculadora()