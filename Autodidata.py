nome = input('Qual é o seu nome? ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite a sua altura em centímetros: '))  # exemplo: 1.65
peso = float(input('Digite o seu peso em kg: '))  # exemplo: 50.7
imc = peso / (altura ** 2)
ano_atual = 2021
nascimento = ano_atual - idade

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso} kg')
print(f'{nome} nasceu em {nascimento}')
print()
print(f'O IMC de {nome} é {imc:.2f}')

if imc < 18.5:
    print('Faixa de peso: Abaixo do peso.')
elif 18.5 <= imc <= 24.9:
    print('Faixa de peso: Normal')
elif 24.9 <= imc <= 30:
    print('Faixa de peso: Sobrepeso')
elif imc > 30:
    print('Faixa de peso: Obesidade')
