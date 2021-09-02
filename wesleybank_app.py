import time
import cowsay
print('\033[1;35m  WESLEYBANK\033[m')
opção = int(input('\033[1;30mOlá, digite o número de qual serviço você precisa :\033[m\n\033[1;32m1 PARA EMPRÉSTISMOS\033[m\n\033[1;31m2 PARA CANCELAR A CONTA\033[m\n\033[1;30mDigite o número :\033[m'))

if opção == 1 :
    print('\033[1;32mVOCÊ ESTÁ NA ABA DE EMPRÉSTIMOS\033[m')
    time.sleep(2)
    nome = str(input('\033[1;30mOlá, tudo bem qual o seu nome :\033[m')).capitalize()
    salario = float(input('\033[1;30mDigite o quanto você recebe de salário :\033[m'))
    print('\033[1;30mÉ um prazer falar com você \033[m \033[1;36m{}\033[m'.format(nome))
    emprestimo = float(input('\033[1;30mDigite o valor do empréstimo que deseja :\033[m'))
    tempo = int(input('\033[1;30mDigite o tempo em \033[m\033[1;31manos\033[m \033[1;30mque deseja pagar esse empréstimos :\033[m'))
    contameses = tempo*12
    contaparcela = emprestimo/contameses
    if contaparcela <= 0.3*salario:
        print('\033[1;32mANALISANDO AS CONDIÇÕES ...\033[m')
        time.sleep(2)
        print('\033[1;32mO SEU EMPRÉSTIMO FOI APROVADO\033[m')
        print('\033[1;31mVocê terá de pagar {} parcelas mensais, no valor de R${:.2f}'.format(contameses,contaparcela))
    else:
        print('\033[1;32mANALISANDO AS CONDIÇÕES ...\033[m')
        time.sleep(2)
        print('\033[1;31mSEU EMPRÉSTIMO FOI NEGADO\033[m')
        print('\033[1;31mO valor das parcelas mensais excedeu os 30% de seu salário')
elif opção == 2:
    print('\033[1;31mVOCÊ ESTÁ NA ABA DE CANCELAMENTO\033[m')
    time.sleep(2)
    nome = str(input('\033[1;30mDigite seu nome :\033[m'))
    input('\033[1;30mNos dê seu feedback :\033[m')
    print('\033[1;32mMuito obrigado {} pelo seu feedback, foi muito bom ter você conosco.\033[m'.format(nome))
    print('\033[1;31mSUA CONTA FOI CANCELADA')
else:
    print('\033[1;31m*\033[m'*35)
    print('\033[1;31mVOCÊ DIGITOU UM NÚMERO DESCONHECIDO\033[m')
    print('\033[1;31m*\033[m'*35)
print('\033[1;35mTENHA UM ÓTIMO DIA, WESLEYBANK AGRADECE ! \033[m')
cowsay.trex("\033[1;31mBY : WESLEY")