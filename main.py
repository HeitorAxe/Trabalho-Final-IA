import cv2
import numpy as np
from sklearn.cluster import KMeans


# Função para aplicar o algoritmo k-médias e reconstruir a imagem
def aplicar_kmeans_e_reconstruir(imagem, k):
    #Redimensiona a imagem para um vetor de pixels
    pixels = imagem.reshape((-1, 3))
    #Aplica k-médias
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(pixels)
    #Rótulos atribuídos a cada pixel
    rotulos = kmeans.labels_
    #Centroides
    centroides = kmeans.cluster_centers_
    #Reconstrói a imagem usando os centroides
    imagem_reconstruida = centroides[rotulos].reshape(imagem.shape)

    return imagem_reconstruida, centroides


kValues = [2, 3, 4, 5, 6, 7, 8]

imagens = ["imagem1.jpg"]

for imagem in imagens:
    imagemOriginal = cv2.imread(imagem)

    # Loop sobre cada valor de k
    for k in kValues:
        # Aplica k-médias e reconstrói a imagem
        imagem_reconstruida, centroides = aplicar_kmeans_e_reconstruir(imagemOriginal, k)
        # Salva a imagem 
        cv2.imwrite(f'reconstruida_{imagem}_k{k}.jpg', imagem_reconstruida)
