from random import randint
from pygame import mixer
import time

mixer.init()

numeroaleatorio = randint(0,5)
print('\033[1;93m-='*30)
print('\033[1;36mVou pensar em um número entre 0 e 5, tente advinhar haha')
numerodigitado = int(input('Digite o número inteiro que você acha que pensei entre 0 e 5 :\033[m'))
input('\033[1;33mAperte enter e veja se você acertou o número que eu pensei\033[m ...')


if numeroaleatorio == numerodigitado:
    print('\033[1;32mPARABÉNS VOCÊ ME SUPEROU!\033[m')
    mixer.music.load('acertou.mp3')
    mixer.music.set_volume(2)
    mixer.music.play()
    time.sleep(2)
else:
    print('\033[1;31mHAHA, VOCÊ FOI DERROTADO SEU MERO MORTAL\033[m!')
    mixer.music.load('errou.mp3')
    mixer.music.set_volume(2)
    mixer.music.play()
    time.sleep(2)
print('\033[1;93m-='*30)

