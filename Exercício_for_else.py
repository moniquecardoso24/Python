"FOR , ELSE"

variavel = ['Nina', 'Sandra', 'João']  # colocar aspas senão dá erro

for valor in variavel:
    if valor.startswith('N'):   # startswith é para checar se começa com a letra informada
        print(f'Começa com N', valor)
    else:
        print(f'Não começa com N', valor)
        break
        continue


comeca_com_s = False
for valor in variavel:
    if valor.lower().startswith('s'):  #LOWER - Pode digitar letra minúscula ou maiúscula. Se não tiver o lower, só pode digitar letra maíscula. O python diferencia maiúsc. de minúsc.
        comeca_com_s = True

if comeca_com_s:
    print(f'Exite uma palavra que começa com S.')
else:
    print(f'Não existe uma palavra que começa com S.')


'Geralmente os programadores usam o continue e não o else'

for valor in variavel:
    if valor.lower().startswith('j'):
        continue
    print(valor)



