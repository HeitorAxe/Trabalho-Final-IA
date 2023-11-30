import cv2
import os
from sklearn.cluster import KMeans
import json
import numpy as np

# Função para aplicar o algoritmo k-médias e reconstruir a imagem
def aplicar_kmeans_e_reconstruir(imagem, k):
    #Redimensiona a imagem para um vetor de pixels
    pixels = imagem.reshape((-1, 3))
    #Aplica k-médias
    kmeans = KMeans(n_clusters=k,n_init='auto')
    #treinamento do modelo
    kmeans.fit(pixels)
    #Rótulos atribuídos a cada pixel
    rotulos = kmeans.labels_
    #Centroides
    centroides = kmeans.cluster_centers_
    #Reconstrói a imagem usando os centroides
    imagem_reconstruida = centroides[rotulos].reshape(imagem.shape)

    return imagem_reconstruida, centroides

def getInfoOfFile(path: str) -> {"resolution": tuple, "size": str, "colors-quantity": int}:
    image = cv2.imread(path)
    resolution = (image.shape[1], image.shape[0])  # (w, h)
    size_kb = os.path.getsize(path) / 1024  # Size in KB
    unique_colors = len(np.unique(image.reshape((-1, 3)), axis=0))
    return {'resolution': resolution, 'size': f"{size_kb:.2f} KB", 'colors-quantity': unique_colors}


kValues = [2, 5, 10, 15, 20, 25, 30]


pasta_originais = "originais/"

# busca imagens na pasta
imagens = sorted(os.listdir(pasta_originais))

dadosImagem = []

for imagem in imagens:
    imagemOriginal = cv2.imread(pasta_originais+imagem)

    info_original = getInfoOfFile(pasta_originais+imagem)

    # Loop sobre cada valor de k
    for k in kValues:
        # Aplica k-médias e reconstrói a imagem
        imagem_reconstruida, centroides = aplicar_kmeans_e_reconstruir(imagemOriginal, k)
        # Cria o diretório se não existir | retirar .jpg do nome da pasta
        pasta_k = f'k-means/{imagem[0:-4]}/k{k}'
        if not os.path.exists(pasta_k):
            os.makedirs(pasta_k)
        # Obtém o nome da imagem sem o caminho
        nome_imagem_sem_caminho = os.path.basename(imagem)

        # Salva a imagem na pasta correspondente ao valor de k
        caminho_imagem_reconstruida = os.path.join(pasta_k, f'k{k}_reconstruida_{nome_imagem_sem_caminho}')
        cv2.imwrite(caminho_imagem_reconstruida, imagem_reconstruida)

        info_reconstruida = getInfoOfFile(caminho_imagem_reconstruida)
        name_json = f'{pasta_k}/dados_{imagem[0:-4]}.json'
        #salva Json
        with open(r''+name_json, 'w') as json_file:
            json.dump({
                            "imagem": imagem[0:-4],
                            "k":k,
                            "original":info_original,
                            "nova":info_reconstruida
            }, json_file, indent=4)

