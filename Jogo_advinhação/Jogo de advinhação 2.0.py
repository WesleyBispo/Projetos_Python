from random import randint
from time import sleep
from pygame import mixer

mixer.init()
cont = 0
typednumber = ""
computernumber = randint(0,10)
while typednumber != computernumber:
    cont += 1
    print('\033[1;36m-='*42)
    print('\033[1;93mEu vou pensar em um número entre 0 e 10 e quero ver se você é capaz de acertar HAHA')
    typednumber = int(input('\033[1;34mTente advinhar o número que pensei : '))
    input('\033[1;30mAperte ENTER e veja se você acertou ...')
    if typednumber == computernumber:
        print('\033[1;32mNÃO ACREDITO, VOCÊ ME VENCEU!')
        print('VOCÊ PRECISOU DE {} TENTATIVAS PARA ACERTAR'.format(cont))
        print('\033[1;36m-='*42)
        mixer.music.load('acertou.mp3')
        mixer.music.set_volume(3)
        mixer.music.play()
        sleep(2)
    else :
        print('\033[1;31mVOCÊ ERROU, EU JÁ ESPERAVA.')
        print('TENTE MAIS UMA VEZ MERO MORTAL')
        mixer.music.load('errou.mp3')
        mixer.music.set_volume(3)
        mixer.music.play()
        sleep(2)




