'''     >>>>> DESAFIO CASA <<<<<
            >> Cauã Campos <<         '''

#========== Início do código ==========#

from time import sleep 
import sys

from time import sleep 
import sys

class Crs:

    branco = '\033[0m'	
    vermelho = '\033[1;31m'
    verde =	'\033[1;32m	'
    amarelo	= '\033[1;33m'	
    azul = '\033[1;34m'	                
    magenta = '\033[1;35m'	
    ciano = '\033[1;36m'	
    cinzaclaro = '\033[1;37m'	
    cinzaescuro = '\033[1;90m'	
    vermelhoclaro = '\033[1;91m'	
    verdeclaro	= '\033[1;92m'	
    amareloclaro = '\033[1;93m'	
    azulclaro = '\033[1;94m'
    magentaclaro = '\033[1;95m'	
    cianoclaro = '\033[1;96m'

print(f'{Crs.ciano}Olá, você chegou do trabalho após um dia exaustivo, parece bastante cansado.{Crs.branco}')

while True:

    print(f'''{Crs.azul}
=============================================={Crs.ciano}
[1] Ir para o quarto. (suíte)
[2] Ir para a cozinha.
[3] Ir para a sala.
[4] Sair de casa.
{Crs.branco}''')

    esc = int(input(f'{Crs.ciano}Selecione o que quer fazer:{Crs.branco} '))
    sleep(2)
    print('')
    print(f'{Crs.azul}=============================================={Crs.branco}')
    print('')

    #============================= 1 ==============================#

    if esc == 1:
        print(f'{Crs.ciano}Você entrou no quarto.{Crs.branco}')

        while True:
            print(f'''{Crs.azul}
=============================================={Crs.ciano}
[1] Tomar banho.
[2] Trocar de roupa.
[3] Dormir. 
[4] Sair do quarto.{Crs.branco}
        ''')

            quarto = int(input(f'{Crs.ciano}Selecione o que quer fazer:{Crs.branco} '))
            sleep(2)
            print('')
            print(f'{Crs.azul}=============================================={Crs.branco}')
            print('')

            if quarto == 1:
                print(f'{Crs.ciano}Você tomou banho.{Crs.branco}')
            elif quarto == 2:
                print(f'{Crs.ciano}Você trocou de roupa.{Crs.branco}')
            elif quarto == 3:
                print(f'{Crs.ciano}Você está dormindo...{Crs.branco}')
                sleep(5)
                print(f'{Crs.ciano}Proonto, acordou novo em folha.{Crs.branco}')
            elif quarto == 4:
                print(f'{Crs.ciano}Você saiu do quarto.{Crs.branco}')
                break

    #============================= 2 ==============================#
    
    if esc == 2:
        print(f'{Crs.ciano}Você entrou na cozinha.{Crs.branco}')

        while True:
            print(f'''{Crs.azul}
=============================================={Crs.ciano}
[1] Fazer almoço.
[2] Tomar um café e fazer um lanche.
[3] Tomar água. 
[4] Sair da cozinha.{Crs.azul}{Crs.branco}
        ''')

            cozinha = int(input(f'{Crs.ciano}Selecione o que quer fazer:{Crs.branco} '))
            sleep(2)
            print('')
            print(f'{Crs.azul}=============================================={Crs.branco}')
            print('')

            if cozinha == 1:
                print(f'{Crs.ciano}Você fez um almoço delicioso.{Crs.branco}')
            elif cozinha == 2:
                print(f'{Crs.ciano}Você fez um lanche e tomou um café.{Crs.branco}')
            elif cozinha == 3:
                print(f'{Crs.ciano}Você se hidratou.{Crs.branco}')
            elif cozinha == 4:
                print(f'{Crs.ciano}Você saiu do cozinha.{Crs.branco}')
                break
    
    #============================= 3 ==============================#

    if esc == 3:
        print(f'{Crs.ciano}Você entrou na sala.{Crs.branco}')

        while True:
            print(f'''{Crs.azul}
=============================================={Crs.ciano}
[1] Assistir série.
[2] Deitar no sofá e mexer no celular.
[3] Deitar no sofá e descansar. 
[4] Sair da sala.{Crs.branco}
        ''')

            sala = int(input(f'{Crs.ciano}Selecione o que quer fazer:{Crs.branco} '))
            sleep(2)
            print('')
            print(f'{Crs.azul}=============================================={Crs.branco}')
            print('')

            if sala == 1:
                print(f'{Crs.ciano}Você sentou no sofá e terminou de assistir sua série.{Crs.branco}')
            elif sala == 2:
                print(f'{Crs.ciano}Você deitou no sofá e está mexendo no celular.{Crs.branco}')
            elif sala == 3:
                print(f'{Crs.ciano}Você deitou no sofá e está descansando.{Crs.branco}')
                sleep(3)
                print(f'{Crs.ciano}Woow, que cochilo bom hein!?{Crs.branco}')   
            elif sala == 4:
                print(f'{Crs.ciano}Você saiu do sala.{Crs.branco}')
                break
    
    #============================= 4 ==============================#

    if esc == 4:
        print(f'{Crs.ciano}Você saiu de casa.{Crs.branco}')
        sys.exit()