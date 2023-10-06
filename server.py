import xmlrpc.server
import math

# Função para calcular o IMC e retornar a classificação
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 24.9:
        classificacao = "Peso normal"
    elif imc < 29.9:
        classificacao = "Sobrepeso"
    elif imc < 34.9:
        classificacao = "Obesidade grau I"
    elif imc < 39.9:
        classificacao = "Obesidade grau II"
    else:
        classificacao = "Obesidade grau III"
    
    return f"IMC: {imc:.2f}, Classificação: {classificacao}"

# Função para calcular uma equação do segundo grau
def calcular_equacao_segundo_grau(a, b, c):
    if a == 0:
        return "A variável 'a' não pode ser zero"
    
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"Soluções: x1 = {x1}, x2 = {x2}"
    elif discriminante == 0:
        x1 = -b / (2*a)
        return f"Solução única: x = {x1}"
    else:
        return "Não há solução real"

# Função para verificar se uma palavra é um palíndromo
def verificar_palindromo(palavra):
    palavra = palavra.lower()
    if palavra == palavra[::-1]:
        return f"{palavra} é um palíndromo"
    else:
        return f"{palavra} não é um palíndromo"

# Criar o servidor RPC
with xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000)) as server:
    server.register_function(calcular_imc, "calcular_imc")
    server.register_function(calcular_equacao_segundo_grau, "calcular_equacao_segundo_grau")
    server.register_function(verificar_palindromo, "verificar_palindromo")
    
    print("Servidor RPC em execução na porta 8000...")
    server.serve_forever()
