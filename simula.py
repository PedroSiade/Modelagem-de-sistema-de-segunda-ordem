from main import cria_cenario, posiciona_blocos, mostra_img, encerra
from main import sec_barra, tam_bloco, tam_mola
from decimal import Decimal
from numpy import exp, cos, sin


def gera_periodos(tf, tp):
    periodos = []
    p = 0
    while p < tf:
        periodos.append(p)
        p += tp
    return periodos

def posicao(tempo):
    t=tempo
    x1=Decimal(-1.398047538899*cos(1.725554106593*t)*exp(-0.665869315209*t)-0.543347494885*exp(-0.665869315209*t)*sin(1.725554106593*t)+0.012045439804*exp(-0.000797351457*t)*sin(0.936459671869*t)+2.898047538899*cos(0.936459671869*t)*exp(-0.000797351457*t))
    x2=Decimal(-1.176388995674*exp(-0.665869315209*t)*sin(1.725554106593*t)+2.807102421878*exp(-0.000797351457*t)*sin(0.936459671869*t)+0.89185485616*cos(1.725554106593*t)*exp(-0.665869315209*t)+3.108145143839*cos(0.936459671869*t)*exp^(-0.000797351457*t))
    return x1,x2


tf=Decimal(80.0)
tp=Decimal(0.1)

periodos = gera_periodos(tf, tp)

for t in periodos:
    x1,x2=posicao(t);

    print("%.5f, %.5f " % \
          (x1, x2))
    img = posiciona_blocos(img, int(x1 * 100), int(x2 * 100), str(t) + " em " + str(tf))

    # Mostra a imagem em movimento
    fim = mostra_img(img)

encerra()
