# Importing the opencv module
import cv2

# Constantes para o cenário
cor_linhas = (255, 0, 0)
cor_bloco1 = (255, 100, 100)
cor_bloco2 = (0, 0, 255)
cor_molas  = (100, 0, 100)
cor_amort  = (0, 100, 100)
solo       = 500   # Coordenada do solo para desenho do cenário
pri_barra  = 100   # Posição da primeira barra da estrutura
sec_barra  = 1100   # Posição da segunda barra da estrutura
alt_barra  = 200   # Altura das barras laterais
larg       = 10    # Largura das estruturas do cenário
larg_fix   = 3     # Largura das linhas da estrutura
tam_bloco  = 100   # Lado do bloco (quadrado)
tam_amort  = 80    # Tamanho do amortecedor
tam_mola   = 150    # Tamanho minimo da mola
num_mola   = 12    # quantidade de itens na mola
#x1i        = 130   # Localização inicial de x1, quando não há tração na mola
#x2i        = 360   # Localização inicial de x2, quando não há tração na mola
# 
# Cria o cenário para os bloquinhos
#
def cria_cenario():
    img = cv2.imread("parque.png")
    cv2.rectangle(img,(pri_barra-larg, solo),(sec_barra+larg, solo+larg),cor_linhas,larg)
    cv2.rectangle(img,(pri_barra-larg, solo), (pri_barra, solo-alt_barra), cor_linhas, larg)
    cv2.rectangle(img,(sec_barra, solo), (sec_barra+larg, solo-alt_barra), cor_linhas, larg)
    passo = int(alt_barra / 10)
    for i in range(10):
        cv2.line(img, (pri_barra-20,solo-i*passo), (pri_barra, (solo-20)-i*passo), cor_linhas, larg_fix) 
    for i in range(10):
        cv2.line(img, (sec_barra+20,solo-i*passo), (sec_barra, (solo-20)-i*passo), cor_linhas, larg_fix) 
    passo = int ((sec_barra-pri_barra) / 20)
    for i in range(20):
        cv2.line(img, ((pri_barra-10)+i*passo, solo+30), ((pri_barra+30)+i*passo, solo), cor_linhas, larg_fix) 
        
    return img

# 
# programa principal
#

def blocos(img, x1, x2):

    cv2.rectangle(img,(x1,solo-20),(tam_bloco+x1,solo-80), cor_bloco1, larg_fix)
    cv2.circle(img, (x1+int(0.20*tam_bloco), solo-10), 8, cor_bloco1, larg_fix)
    cv2.circle(img, (x1+int(0.75*tam_bloco), solo-10), 8, cor_bloco1, larg_fix)
 
    cv2.putText(img=img, text='M1', org=(x1+int(tam_bloco/3), solo-int(tam_bloco/3)), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=cor_bloco1,thickness=1)
    cv2.line(img, (pri_barra, int(solo-tam_bloco-20)), (x1, int(solo-tam_bloco-20)), cor_bloco1, 1) 
    cv2.line(img, (x1, int(solo-tam_bloco-25)), (x1, int(solo-tam_bloco-15)), cor_bloco1, 1) 
    cv2.putText(img=img, text='X1='+str(x1), org=(x1-80, int(solo-tam_bloco-25)), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=cor_bloco1,thickness=1)
    
    cv2.rectangle(img,(x2,solo-20),(tam_bloco+x2,solo-80), cor_bloco2, larg_fix)
    cv2.putText(img=img, text='M2', org=(x2+int(tam_bloco/3), solo-int(tam_bloco/3)), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=cor_bloco2,thickness=1)
    cv2.circle(img, (x2+int(0.20*tam_bloco), solo-10), 8, cor_bloco2, larg_fix)
    cv2.circle(img, (x2+int(0.75*tam_bloco), solo-10), 8, cor_bloco2, larg_fix)
    cv2.line(img, (pri_barra, int(solo-tam_bloco-50)), (x2, int(solo-tam_bloco-50)), cor_bloco2, 1) 
    cv2.line(img, (x2, int(solo-tam_bloco-55)), (x2, int(solo-tam_bloco-45)), cor_bloco2, 1) 
    cv2.putText(img=img, text='X2='+str(x2), org=(x2-80, int(solo-tam_bloco-55)), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=cor_bloco2,thickness=1)
    
    
    return img

def draw_mola(img, pos, leng):
    esp = int(leng / (num_mola))
    for i in range(0, num_mola, 2):
        cv2.line(img, (pos+i*esp, int(solo-tam_bloco/3-10)), (pos+(i+1)*esp, int(solo-tam_bloco/3+10)), cor_molas, 2) 
        cv2.line(img, (pos+(i+1)*esp, int(solo-tam_bloco/3+10)), (pos+(i+2)*esp, int(solo-tam_bloco/3-10)), cor_molas, 2)
    if (i+2)*esp < leng:
        cv2.line(img, (pos+(i+2)*esp, int(solo-tam_bloco/3-10)), (pos+leng, int(solo-tam_bloco/3-10)), cor_molas, 2)
        
    return img

def draw_amortecedor(img, x1, x2):
    
    pos_i = x1 + tam_bloco 
    pos_f = x2

    leng = x2 - x1 - tam_bloco
   
    # barras fixa do amostecedor
    cv2.line(img, (pos_i, int(solo-tam_bloco+30)), (pos_i+int(leng/2.5), int(solo-tam_bloco+30)), cor_amort, 2) 
    cv2.line(img, (pos_f, int(solo-tam_bloco+30)), (pos_f-int(leng/2.5), int(solo-tam_bloco+30)), cor_amort, 2) 

    # cilindro do amostecedor
    cv2.line(img, (pos_f-int(leng/2.5), int(solo-tam_bloco+40)), (pos_f-int(leng/2.5)-tam_amort, int(solo-tam_bloco+40)), cor_amort, 2) 
    cv2.line(img, (pos_f-int(leng/2.5), int(solo-tam_bloco+20)), (pos_f-int(leng/2.5)-tam_amort, int(solo-tam_bloco+20)), cor_amort, 2) 
 
    # Ponta aberta do amortecedor   
    cv2.line(img, (pos_f-int(leng/2.5)-tam_amort, int(solo-tam_bloco+40)), (pos_f-int(leng/2.5)-tam_amort, int(solo-tam_bloco+35)), cor_amort, 2) 
    cv2.line(img, (pos_f-int(leng/2.5)-tam_amort, int(solo-tam_bloco+20)), (pos_f-int(leng/2.5)-tam_amort, int(solo-tam_bloco+25)), cor_amort, 2)
    cv2.line(img, (pos_i+int(leng/2.5), int(solo-tam_bloco+35)), (pos_i+int(leng/2.5), int(solo-tam_bloco+25)), cor_amort, 2) 
    
    # Ponta fechada do amortecedor
    cv2.line(img, (pos_f-int(leng/2.5), int(solo-tam_bloco+40)), (pos_f-int(leng/2.5), int(solo-tam_bloco+20)),  cor_amort, 2) 

    return img
    
def molas(img, x1, x2):
    m1 = x1 - pri_barra
    img = draw_mola(img, pri_barra, m1)
    
    m2 = x2 - (x1 + tam_bloco)
    img = draw_mola(img, x1 + tam_bloco, m2)
    
    m3 = sec_barra - (x2 + tam_bloco)
    img = draw_mola(img, x2 + tam_bloco, m3)
    return img

def limites(x1, x2):
    
    #verifica os limites de x1
    if x1 < pri_barra + tam_mola:
        x1 = pri_barra + tam_mola
    if x1 > sec_barra - 2*tam_bloco - 2*tam_mola:
        x1 = sec_barra - 2*tam_bloco - 2*tam_mola

    #verifica os limites de x2   
    if x2 > sec_barra - tam_bloco - tam_mola:
        x2 = sec_barra - tam_bloco - tam_mola

    if x2 < pri_barra + tam_bloco + 2*tam_mola:
        x2 = pri_barra + tam_bloco + 2*tam_mola
        
    return x1, x2

def posiciona_blocos(img, x1, x2, txt):
    x1, x2 = limites(x1, x2)
    img = blocos(img, x1, x2)
    img = molas(img, x1, x2)
    img = draw_amortecedor(img, x1, x2)
    cv2.putText(img=img, text=txt, org=(30, 30), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 0, 0),thickness=1)
    return img


def mostra_img(img):
    cv2.imshow("Simulador de movimento de Blocos", img) 
    if cv2.waitKey(10) & 0xFF == 27:#ord('q'):
        cv2.destroyAllWindows()
        return False
    else:
        return True
    
def encerra():
    cv2.destroyAllWindows()
    