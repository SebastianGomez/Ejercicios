/*
1) Realizá un programa que permita al usuario ingresar su nombre. La computadora debe emitir una
salida con un mensaje de bienvenida que incluya el nombre ingresado.

nombre = prompt("Ingrese su nombre: ")
alert("Hola " + nombre)

2) Realizá un programa que permita al usuario ingresar un número entero. La computadora debe
informar el número opuesto1 y el número inverso2 del ingresado.


numero = parseInt(prompt("Ingrese un numero: "))
console.log("El opuesto es: " + (numero*-1))
console.log("El inverso es: " + (1/numero))

3) Realizá un programa que permita al usuario ingresar 3 notas pertenecientes a tres trimestres
distintos para cierto alumno. La computadora debe mostrar la nota promedio.


nota1 = parseInt(prompt("Ingrese una nota: "))
nota2 = parseInt(prompt("Ingrese una nota: "))
nota3 = parseInt(prompt("Ingrese una nota: "))

console.log((nota1+nota2+nota3)/3)

4) Realizá un programa que permita al usuario ingresar el valor salarial de una hora de trabajo y la
cantidad de horas trabajadas por día. La computadora debe mostrar el valor del salario semanal,
asumiendo que trabaja todos los días hábiles y media jornada los sábados.



valorHora = parseInt(prompt("Ingrese el valor de la hora: "))
cantidadHoras = parseInt(prompt("Ingrese las horas trabajadas: "))

Semana = 5*valorHora*cantidadHoras+(valorHora*cantidadHoras/2)

console.log(Semana)


5) Realizá un programa que permita al usuario ingresar valores del mismo tipo para las variables a
y b. Una vez cargadas, la computadora debe mostrar ambas variables por pantalla, intercambiar
entre sí sus valores (que lo cargado en a quede en b, y viceversa), y volver a mostrarlas.


variable1 = prompt("Ingrese variable1: ")
variable2 = prompt("Ingrese variable2: ")

console.log("La variable 1 es: "+variable1)
console.log("La variable 2 es: "+variable2)

variable3 = variable1
variable1 = variable2
variable2 = variable3

console.log("La variable 1 es: "+variable1)
console.log("La variable 2 es: "+variable2)


6) Realizá un programa que permita al usuario ingresar el valor unitario de cierto artículo y la
cantidad de artículos vendidos por un vendedor, del cual se sabe que gana un sueldo fijo de $14000
más el 16% del monto total vendido. Con tales datos, la computadora debe calcular el sueldo
mensual del vendedor y mostrarlo.




valorArticulo = parseInt(prompt("Ingrese el valor del articulo: "))
cantArticulos = parseInt(prompt("Ingrese la cantidad de articulos: "))
sueldoFijo = 14000
comision = valorArticulo*cantArticulos*16/100
sueldoTotal = sueldoFijo+comision

console.log("El sueldo total es: "+sueldoTotal)

*/
