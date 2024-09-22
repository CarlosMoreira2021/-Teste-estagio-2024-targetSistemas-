import time
import random

# Simulando as lâmpadas
lâmpadas = {
    'I1': False,
    'I2': False,
    'I3': False
}

# Randomicamente, ligamos as lâmpadas a interruptores
lâmpada_correspondente = random.choice(list(lâmpadas.keys()))
lâmpadas[lâmpada_correspondente] = True

def verificar_lâmpadas():
    print("Verificando as lâmpadas...")
    for interruptor, estado in lâmpadas.items():
        print(f"{interruptor}: {'Acesa' if estado else 'Apagada'}")

def simular_interrupções():
    print("Ligando o I1...")
    lâmpadas[lâmpada_correspondente] = True  # Lâmpada correspondente a I1
    time.sleep(10)  # Esperar 10 segundos
    print("Desligando o I1 e ligando o I2...")
    lâmpadas[lâmpada_correspondente] = False  # Desligar lâmpada correspondente a I1
    lâmpadas['I2'] = True  # Ligar lâmpada correspondente a I2

# Simulação
simular_interrupções()
verificar_lâmpadas()

# Exibindo qual lâmpada corresponde a qual interruptor
print("\nResultado:")
print(f"Lâmpada ligada a I1: {'Apagada' if lâmpadas[lâmpada_correspondente] else 'Acesa'}")
print(f"Lâmpada ligada a I2: {'Acesa' if lâmpadas['I2'] else 'Apagada'}")
print(f"Lâmpada ligada a I3: {'Apagada' if lâmpadas[lâmpada_correspondente] else 'Acesa' if not lâmpadas['I2'] else 'Apagada'}")
