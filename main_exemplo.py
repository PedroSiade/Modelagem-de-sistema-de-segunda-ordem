from Simula import  cria_cenario, posiciona_blocos, mostra_img, encerra

#
# Programa principal gera o movimento dos blocos, molas e amortecedores
#
image = cria_cenario()
Fim = True

pos = 0
inc = 1
while Fim:
    
    img = image.copy()
    
    # Estima a posição dos blocos
    x1 = 160 + pos
    x2 = 400 + int(pos*1.3)

    img = posiciona_blocos(img, x1, x2, "Simulcao - Tecle <Esc> para encerrar")


    # Mostra a imagem em movimento
    Fim = mostra_img(img)
    if pos > 400:
        inc = - 1
    if pos < 140:
        inc = 1
        
    pos += inc

encerra()
    



