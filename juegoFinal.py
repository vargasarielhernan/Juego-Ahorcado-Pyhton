import random

#DEFINICION VARIABLES
peliculas= ["batman", "titanic", "mision imposible", "el ilusionista", "el padrino", "casablanca"]
vidas = ["❤️","❤️","❤️","❤️","❤️","❤️","❤️"]
indicePeliculas = 0
letra = ""
cantidadGuiones = ""
guionesVacios = list()
peliculaElegida = list()
encontro=0

#PROGRAMA
print("*"*80)
print("*"*10 , " "*17 , "EL JUEGO DEL AHORCADO!", " "*17 ,"*"*10 )
print("*"*10 , " "*25, "Reglas:", " "*24, "*"*10 )
print("*"*10 , "Intente adivinar la palabra ingresando una letra o palabra", "*"*10 )
print("*"*10 , " "*5, "Si ingresa una letra y falla, pierde una vida.", " "*5, "*"*10 )
print("*"*10 , " "*5, "Si ingresa una palabra y falla, pierde 3 vidas.", " "*4, "*"*10 )
print("*"*80, "\n")
print("Cantidad de vidas: ", vidas)
indicePeliculas = random.randint(0, len(peliculas)-1)
print(peliculas[indicePeliculas])
#print(list(peliculas[indicePeliculas]))
peliculaElegida = list(peliculas[indicePeliculas])
#print(peliculas[indicePeliculas][3])
cantidadGuiones = ("_"*(len(peliculas[indicePeliculas])))
guionesVacios = list(cantidadGuiones)
for i in range(len(peliculaElegida)):
      if " " == peliculaElegida[i]:
        guionesVacios[i] = " "
#print(guionesVacios)
ultimosGuiones = "".join(guionesVacios)
print("Película: ", ultimosGuiones)
 #funcion que busca si encuentra cohincidencias entre numero si hacen match devuelve true sino false
def search(list, peliculaElegida):
      for i in range(len(list)):
        for x in range(len(peliculaElegida)):
          if list[i] == peliculaElegida[x]:
             return True
      return False
while len(vidas) <= 7 and len(vidas) > 0:
 if ultimosGuiones != peliculas[indicePeliculas]:  
  letra = input("Ingrese una letra o palabra: ").lower()
  letraUsuario = list(letra)
    
  if len(letraUsuario) > 1:
    #si la funcion no encuentra cohincidencias remueve 3 vidas
    if not search(letraUsuario, peliculaElegida):
      if len(vidas)<3:
        vidas=0
      # if len(vidas) == 0:
        print("Perdiste!!! 🤣")
      else:
        vidas.remove(vidas[len(vidas) - 1])
        vidas.remove(vidas[len(vidas) - 1])
        vidas.remove(vidas[len(vidas) - 1])
      print("Cantidad vidas elif: ", vidas)
      # si el user se queda sin vidas termina el juego
      

    for i in range(len(peliculaElegida)):
      letraOriginal=letraUsuario
      if (len(letraUsuario)<len(peliculaElegida)):
        letraUsuario.append("_")
    for u in range(len(peliculaElegida)):
       
        for c in range(len(peliculaElegida)):
          """ aca se realiza un for dentro de otro for para que cuando el user ponga una letra recorra toda la peliculaElegida 
          en caso de encontrar cohincidencia con la letra la iguala 
          
           """
          
          if letraUsuario[u] == peliculaElegida[c]:
            guionesVacios[c] = letraUsuario[u]

    

  else: 
   
    #si la funcion da true ingresa aca 
    if search(letraUsuario, peliculaElegida):
    
      for i in range(len(peliculaElegida)):
        # recorre la letra ingresada x los indices de la pelicula si encuentra match lo reemplaza
        if letraUsuario[0] == peliculaElegida[i]:
         print("Entro aca2", ultimosGuiones == peliculas[indicePeliculas])
         guionesVacios[i] = letraUsuario[0]
         encontro=1
         letraUsuario.append("_")     
    #si la funcion no encuentra cohincidencias remueve una vida
    elif not search(letraUsuario, peliculaElegida):
      vidas.remove(vidas[len(vidas) - 1])
      print("Cantidad vidas elif: ", vidas)
      # si el user se queda sin vidas termina el juego
      if len(vidas) == 0:
          print("Perdiste!!! 🤣")
      
  ultimosGuiones = "".join(guionesVacios)
  if ultimosGuiones == peliculas[indicePeliculas]:
        print("ADIVINASTE!!!")
        print("La pelicula era " + peliculas[indicePeliculas])
  print("Adivinaste las siguientes letras: ", ultimosGuiones)
