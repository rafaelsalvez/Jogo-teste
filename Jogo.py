from time import sleep

print('Bem vindo(a ao Jogo!!')
sleep(1)
nome = input('Digite seu nome.')
Boasvindas = print(f'Bem vindo ao jogo {nome}, espero que se divirta.')
sleep(0.5)
while True:
    escolha1 = int(input('Você acorda em um quarto escuro, sem lembranças de como chegou ali, tudo que consegue ver é uma lanterna em uma mesa a sua frente e uma porta. O que você escolhe fazer? 1-Pegar a lanterna e explorar o quarto. 2-Sair pela porta. Escolha: '))
        
    if escolha1 == 1:
            escolha2 = int(input('Você começa a explorar o quarto e encontra uma passagem em um canto do quarto grande o suficiente para você passsar, se esgueira por la e acaba dando em uma sala de visitas, aparentemente você não estava sozinho(a) lá. 1-Vasculhar a sala. 2-tentar sair pela porta de entrada. Escolha: '))
            
            if escolha2 == 1:
                escolha3 = int(input('Você consegue ver um corredor do outro lado dessa sala e uma porta que da acesso a uma cozinha escura onde você vê um painel com as chaves da casa e do carro, nessse momento começa a ouvir passsos vindo em sua direção. 1-Seguir pelo corredor. 2-Ir a cozinha e pegar as chaves. 3 Se esconder. Escolha: '))
                
                if escolha3== 1:
                    print('Do outro lado do corredor, um homem com uma besta atira em seu peito...')       
                    sleep(1)
                    print('Você morreu...')
                if escolha3 == 2:
                    escolha4 = int(input('Você pega as chaves e corre em diração a porta, enquanto abre vocçê ouve passos pesados correndo em sua direção, quando passa pela porta, fecha ela rapidamente e corre em direção ao carro, entra e tenta liga-lo, nessse momento o homem arromba a porta e vai em sua direção com uma adaga na mão, você consegue ligar o carro e tem que tomar uma importante decisão agora. 1-Passar por cima do sequestrador. 2-Dar marcha ré e sair daquele lugar.'))

                    if escolha4 == 1:
                        print('Você acelera a toda velocidade em direção ao homem e passa por cima dele com tudo, nesse momento percebe que ele tenta se arrastar para fora, dá a ré e vai pra cima novamente, acabando finalmente com isso...')
                        sleep(1)
                        print(f'Parabéns por concluir o jogo {nome} e previnir que mais pessoas sofram com isso..')
                        print(f'Obrigado por jogar!! :)')
                    if escolha4 == 2:
                        print('Você acelera e sai desesperadamente daquele lugar, sem olhar para trás, dando umfim a esse pesadelo...')
                        sleep(1)
                        print(f'Parabéns por concluir o jogo {nome}!!')
                        print('Obrigado por jogar!! :)')
                if escolha3 == 3:
                    print('Você se esconde atrás de uma prateleira enquanto vê um homem enorme passando pela sala, quando você nota que ele ja te viu, agora é tarde para correr...')
                    sleep(1)  
                    print('Você morreu...')

            
            if escolha2 == 2:
                print('Ao tentar abrir a porta um alarme soa e você sente algo atravessando seu peito, um homem atrás de você com uma adaga...')
                sleep(1)
                print('Você morreu...')
                
    
        
    elif escolha1 == 2:
        print('Assim que abre a porta, vê um homem com uma faca e no mesmo instante te ataca...')
        sleep(1)
        print('Você morreu...') 
        break  
    else:
        print('Número inválido')
print('Tente novamente! :)')        
                          