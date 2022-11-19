"""
DESAFIO
1. Criar variáveis para nome(str), idade(int), altura (float) e peso (float) de uma pessoa
2. Criar variável com o ano atual (int)
3. Obter o ano de nascimento de uma pessoa (baseado na idade e no ano atual)
4. Obter o IMC de uma pessoa com 2 casas decimais ( peso e altura da pessoa)
5. Exibir um texto com todos os valores na tela usando F-Strings ( com as chaves)
"""

nome = 'Monique'  # str
idade = 23  # int
altura = 1.58  # float
e_maior = idade > 18  # bool
peso = 41.6  # float
imc = peso / (altura ** 2)  # porque () tem maior precedência
ano_atual = 2021  # int
nascimento = ano_atual - idade


print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso} kg')
print(f'O IMC de Monique é {imc:.2f}')  # duas casas decimais, usa-se :.2f depois da variável
print(f'{nome} nasceu em {nascimento}')


forma_automatizada = "FORMA AUTOMATIZADA"
print(forma_automatizada)
#forma que eu fiz sem o f e automatizada
print('{n} tem {i} anos, {a} de altura e pesa {p} kg'. format(n=nome, i=idade, a=altura, p=peso))
