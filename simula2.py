from main import cria_cenario, posiciona_blocos, mostra_img, encerra
from decimal import Decimal
import math
import cv2

tf = Decimal(80)
tp = Decimal(0.1)


def gera_periodos():
    periodos = []
    p = Decimal(0)
    while p < tf:
        periodos.append(p)
        p += tp
    return periodos


def posicao(tempo):
    t = float (tempo)
    a = -1.398047538899 * math.cos(1.725554106593 * t) * math.exp(-0.665869315209 * t)
    b = -0.543347494885 * math.exp(-0.665869315209 * t) * math.sin(1.725554106593 * t)
    c = 0.012045439804 * math.exp(-0.000797351457 * t) * math.sin(0.936459671869 * t)
    d = 2.898047538899 * math.cos(0.936459671869 * t) * math.exp(-0.000797351457 * t)
    x1 = Decimal(a + b + c + d)
    e=-1.176388995674*math.exp(-0.665869315209*t)*math.sin(1.725554106593*t)
    f=2.807102421878*math.exp(-0.000797351457*t)*math.sin(0.936459671869*t)
    g=0.89185485616*math.cos(1.725554106593*t)*math.exp(-0.665869315209*t)
    h=3.108145143839*math.cos(0.936459671869*t)*math.exp(-0.000797351457*t)
    x2=e+f+g+h
    return x1,x2


period = gera_periodos()

for t1 in period:
    image = cria_cenario()
    from PIL import Image

    im1 = cv2.imread(r"C:\Users\pedro\PycharmProjects\pythonProject\Fundo.jpg")
    img = im1.copy()

    xa1, xa2 = posicao(t1)
    print("%.5f, %.5f " % \
          (xa1, xa2))
    img = posiciona_blocos(img, int(xa1 * 100), int(xa2 * 100), str(t1) + " em " + str(tf))

    # Mostra a imagem em movimento
    fim = mostra_img(img)
encerra()
