totaldasidades = 0
mulheresmenor20 = 0
totalmulheres = 0
maisvelho = 0
nomehomem = str
for pessoa in range (1,5):
    print('\033[1;34m-=' * 15)
    print('\033[1;93mDADOS {}° PESSOA'.format(pessoa))
    nome = str(input('\033[1;30mDIGITE O NOME :')).strip().title()
    sexo = str(input('DIGITE O GÊNERO :')).upper().strip()
    idade = int(input('DIGITE A IDADE :'))
    totaldasidades += idade
    if "FEMININO" in sexo :
        totalmulheres += 1
        if idade < 20 :
            mulheresmenor20 += 1
    if "MASCULINO" in sexo :
        if pessoa == 1 :
            maisvelho = idade
            nomehomem = nome
        else:
            if idade > maisvelho:
                maisvelho = idade
                nomehomem = nome

print('\033[1;34m-='*15)
if totalmulheres > 1 :
    print('\033[1;36mDe um total de \033[1;93m{} \033[1;36mmulheres \033[1;93m{} \033[1;36mtem menos de 20 anos'.format(totalmulheres,mulheresmenor20))
elif totalmulheres == 1 :
    print('\033[1;36mDe \033[1;93m1 \033[1;36mmulher \033[1;93m1 \033[1;36mtem menos de 20 anos')
else:
    print('\033[1;36mTemos o total de \033[1;93m0 \033[1;36mmulheres')
print('\033[1;32mA média de idade dos \033[1;93m4 \033[1;32mcadastrados é igual a \033[1;93m{:.1f}'.format(totaldasidades/4))
print('\033[1;31mO \033[1;93m{} \033[1;31mé o homem mais velho cadastrado com \033[1;93m{} \033[1;31manos de idade'.format(nomehomem,maisvelho))

