from Simula import  cria_cenario, posiciona_blocos, mostra_img, encerra
from Simula import  sec_barra, tam_bloco, tam_mola
from decimal import Decimal
import math

def gera_periodos(tf, tp):
    periodos = []
    p = 0
    while p < tf:
        periodos.append(p)
        p += tp
    return periodos

def nova_posição2(x1, x2):
    xa1 = Decimal(x1)
    xa2 = Decimal(x2)
    return xa1, xa2


#
# Programa principal gera o movimento dos blocos, molas e amortecedores
#
tm = Decimal(tam_mola/100)
tb = Decimal(tam_bloco/100)
sb = Decimal(sec_barra/100)

x1 = Decimal('1.50')     # posição inicial
x2 = Decimal('3.0')     # posição final
tf = Decimal('60.0')      # tempo final da simulação
tp = Decimal('0.1')     # passo de mudança do tempo

# Velocidades iniciais 
v1  = Decimal('0')
va1 = Decimal('0')
v2  = Decimal('0')
va2 = Decimal('0')

# Caracteísticas do sistema
k1 = Decimal('10')
k2 = Decimal('15')
k3 = Decimal('12')
b  = Decimal('8')
m1 = Decimal('10')
m2 = Decimal('15')

image = cria_cenario()

periodos = gera_periodos(tf, tp)

for t in periodos:
    img = image.copy()
    
    # Calcula nova posição dos blocos
    xa1, xa2 = nova_posição2(x1, x2)
    
    # Gera quadro da imagem com nova posição dos blocos
    print("%.5f, %.5f " % \
          (x1, x2))
    img = posiciona_blocos(img, int(x1*60), int(x2*60), str(t) + " em " + str(tf))
    
    # Mostra a imagem em movimento
    fim = mostra_img(img)
    
    t = float(t)
    
    #Função que calcula a posição do carro 1
    x1 = Decimal(3)+Decimal(-1.398047538899 * math.cos(1.725554106593 * t) * math.exp(-0.665869315209 * t)-0.543347494885 * math.exp(-0.665869315209 * t) * math.sin(1.725554106593 * t) + 0.012045439804 *
                 math.exp(-0.000797351457 * t) * math.sin(0.936459671869 * t)+2.898047538899 * math.cos(0.936459671869 * t) * math.exp(-0.000797351457 * t))
    
    #Função que calcula a posição do carro 2
    x2 = Decimal(8)+Decimal(-1.176388995674*math.exp(-0.665869315209*t)*math.sin(1.725554106593*t)+2.807102421878*math.exp(-0.000797351457*t)*math.sin(0.936459671869*t)+0.89185485616 *
                 math.cos(1.725554106593*t)*math.exp(-0.665869315209*t)+3.108145143839*math.cos(0.936459671869*t)*math.exp(-0.000797351457*t))

encerra()
    



