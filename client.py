import xmlrpc.client

# Criar um proxy para o servidor RPC
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Exemplo de chamada para calcular o IMC
resultado_imc = proxy.calcular_imc(70, 1.75)
print(resultado_imc)

# Exemplo de chamada para calcular uma equação do segundo grau
resultado_equacao = proxy.calcular_equacao_segundo_grau(1, -3, 2)
print(resultado_equacao)

# Exemplo de chamada para verificar se uma palavra é um palíndromo
resultado_palindromo = proxy.verificar_palindromo("socorram-me, subi no ônibus em marrocos")
print(resultado_palindromo)
