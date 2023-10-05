#Listas Practicas 1
itic3=["Fernanda Pantoja Castillo","Zuleyma de jesus manzano","Vanessa Chaves","Jesus Garcia","Aylin Martinez"]
Carreras_Itpa=["Logistica","Mecatronica","Industrial","Tics","Gestion Empresarial"]
Edades=[18,19,19,19,19,20,32,19,19,19,20,19]
#Imprimir lista
print(Carreras_Itpa)
print(itic3)
print(Edades)

#Imprimir el 3 campo de listas
print(Carreras_Itpa[2])
print(itic3[2])
print(Edades[3])

#Agregar elementos al final de la lista
itic3.append("Zuleyma")
print(itic3)

#Agregar otra lista
itic3.extend(["Aylin", "Jesus"])
print(itic3)

#Agregar elementos en la posicion 5
itic3.insert([8,"Carlos"])
print(itic3)

#Borrar un elemento determinado
del Edades [3]
print(Edades)

#Ver el tamaño de nuestras listas
print(len[Edades])
print(len[itic3])
print(len[Carreras_Itpa])

#Eliminar un elemento en espacio
Edades.remove(32)
print(Edades)
print("----------------------------")

#ordenar elementos
print(Edades)
Edades.sort()
print(Edades)