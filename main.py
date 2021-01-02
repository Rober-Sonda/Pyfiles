def agregarArticulo(articulo):
  escribir_archivo = open("archivito.txt","a") #"a" es el modo edictar el archivo buscar en la documentacion de python https://docs.python.org/es/3/library/functions.html?highlight=open#open
  escribir_archivo.write("{}\n".format(articulo))
  escribir_archivo.close()

agregarArticulo(input("ingresa el articulo -> "))