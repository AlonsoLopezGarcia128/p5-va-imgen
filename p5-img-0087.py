import cv2
## Leer la imagen con cv2 = computer vision
img = cv2.imread('spiderman1020.jpg')
## Determinar tipo de imagen numpy.ndarray
print(type(img))
## Mostrar pixeles (554, 554, 3)
print(img.shape)

## Mostrando iamgen en ventana, barra de titulo spiderman0087
cv2.imshow('spiderman0087', img)
## Tiempo de espera
cv2.waitKey(0)
## Destruir todas las ventanas 
cv2.destroyAllWindows()


