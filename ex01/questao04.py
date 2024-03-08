def descobrir_interruptores_lampadas():
    
    interruptores = [False, False, False]

    ligar_interruptor(0, interruptores)

    for i in range(len(interruptores)):
        if estado_lampada(i):
            print(f"O interruptor {i + 1} controla a lâmpada {i + 1}")
        else:
            print(f"O interruptor {i + 1} não controla a lâmpada {i + 1}")

def ligar_interruptor(num_interruptor, interruptores):
    interruptores[num_interruptor] = not interruptores[num_interruptor]

def estado_lampada(num_lampada):

    return num_lampada % 2 == 1

descobrir_interruptores_lampadas()
