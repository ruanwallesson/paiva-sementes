import matplotlib.pyplot as plt
import cv2

#recebe a imagem
img = cv2.imread('9.jpg')

img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(45,45))
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
img = cv2.GaussianBlur(closing, (55, 55), 0)
_,threshold = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

#corta a imagem
threshold = threshold[1000:1980, 1200:2900]

largura = 0
for i in range(len(threshold[0])):
    soma = 0
    for j in range(len(threshold)):
        if threshold[j][i] == 0:
            soma += 1
    if largura < soma:
        largura = soma

altura = 0 
for i in threshold:
    soma = 0
    for j in i:
        if j == 0:
            soma += 1
    if soma > altura:
        altura = soma
        
#mostra como a imagem esta
plt.imshow(threshold)

#salva a imagemm
cv2.imwrite('Salvo.png', threshold)
print('diametro %.2f' %(largura/37.398373983739837398373983739837))
print('largura %.2f' %(altura/35.827435119649477586788001348163))
