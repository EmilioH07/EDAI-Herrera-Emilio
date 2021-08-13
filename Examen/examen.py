import os
os.system("cls")

print("\n\t\t\t\tBienvenido a mi examen de EDAI\n")
a=open("covid.csv","r")
contenido=a.readlines()

x=0
i=0
j=0
for i in range (0,len(contenido)):
	indicador=contenido[i].split(',')
	
	if float(indicador[1])>=0.8:
		print("Esta persona si tiene Covid")
		print("Edad: "+indicador[0]+"\t Indicador: "+indicador[1])
		x=x+int(indicador[0])
		j=j+1
		
	elif float(indicador[1])<0.8:
		print("Esta persona no tiene Covid")
		print("Edad: "+indicador[0]+"\t Indicador: "+indicador[1])
		
	i=i+1

prom=x/j

print("Total de personas con Covid-19: "+str(j))

if j==0:
	print("El semáforo es verde, no se confíe siga con sus medidas de protección.")
elif j>=1 and j<=30:
	print("El semáforo es amarillo, mantenga todas las medidas de precaución.")
elif j>=31 and j<=70:
	print("El semáforo es naranja, salga solo para lo escencial.")
elif j>=71 and j<=100:
	print("El semáforo es rojo, manten la cuarentena.")


print("\nEl promedio de edad de personas con  Covid-19 es: "+str(prom))