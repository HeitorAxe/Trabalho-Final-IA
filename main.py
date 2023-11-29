import cv2
import os
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

pasta_originais = "originais/"
imagens = ["imagem2.jpg"]

for imagem in imagens:
    imagemOriginal = cv2.imread(pasta_originais+imagem)
    print(imagemOriginal)
    # Loop sobre cada valor de k
    for k in kValues:
        # Aplica k-médias e reconstrói a imagem
        imagem_reconstruida, centroides = aplicar_kmeans_e_reconstruir(imagemOriginal, k)
        # Cria o diretório se não existir
        pasta_k = f'k-means/k_{k}'
        if not os.path.exists(pasta_k):
            os.makedirs(pasta_k)

        # Obtém o nome da imagem sem o caminho
        nome_imagem_sem_caminho = os.path.basename(imagem)

        # Salva a imagem na pasta correspondente ao valor de k
        caminho_imagem_reconstruida = os.path.join(pasta_k, f'reconstruida_{nome_imagem_sem_caminho}_k{k}.jpg')
        cv2.imwrite(caminho_imagem_reconstruida, imagem_reconstruida)
