print("----Hola!! Mi nombre es BotRoG, me gustaria saber un poco mas de ti.----")
nomb = input("¿Cual es tu nombre? ")
print(f"Hoo, mucho gusto {nomb}!! ")
my_name = input("¿Quieres saber el significado de mi nombre? Si/No ")
if my_name in ["Si","si","SI"]:
    print("El significado es Ro de Rosales y G de Guerrero. ")
else:
    print("No te preocupes vamos a continuar con la siguente pregunta.")

color = input("¿Cual es tu color favorito? ")
if color in ["Azul","azul"]:
    print("Wow el color azul es hermoso, como un dia soleado con el cielo azul")
elif color in ["Rojo","rojo"]:
    print("Wow el color rojo es hermoso, como el color icónico de Ferrari")
elif color in ["verde","Verde"]:
    print("Wow el color verde es hermoso, me recuerda a un paisaje colorido resaltando el color verde de los arboles")
else:
    print(f"Wow el color {color} es hermoso. ")

edad = input(F"{nomb}, ¿Cual es tu edad? ")
edadint = int(edad)
print(F"Wow entonses naciste en el {2024-edadint}")

ppt = input("¿Te gustaria jugar al piedra papel o tijera? ")
if ppt in ["Si","SI","si"]:
    print("Perfecto comencemos...")
    res = input("Elige piedra, papel o tijera ")
    if res in ["Piedra","piedra","PIEDRA"]:
      print("BotRoG eligio Papel, !!!GANASTE¡¡¡")
    elif res in ["Papel","papel","PAPEL"]:
      print("BotRoG tambien eligio Pepel, EMPATE")
    elif res in ["Tijera","tijera","TIJERA"]:
      print("BotRoG eligio Papel, !!!GANASTE¡¡¡")
    else: print("Eligue una opcion corecta.")
else:
    print("No te preocupes podemos seguir conversando.")

pre_f1 = input("¿Te gusta la formula 1? ")
if pre_f1 in ["Si","SI","si"]:
   wc = input(f"{nomb}, ¿Quien crees que se campeon de F1 en 2024?")
   print(f"{wc}, Wow yo siento que Max Verstapen sera nuevamente campeon")

print(f"Me despido {nomb}, espera proximas actualizaciones")
print("----BotRoG v1.0 2024----")
