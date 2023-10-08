/*1) Realizá un programa que muestre todos los números enteros del 1 al 100, y luego, los mismos
números, pero en orden inverso.



for (let i = 1; i <= 100; i++) {
    console.log(i)
   
}
for (let i = 100; i >=1 ; i--) {
    console.log(i)
}

2) Realizá un programa que permita al usuario ingresar dos números enteros num1 y num2, donde el
primero siempre deberá ser menor o igual al segundo. La computadora debe mostrar la secuencia
de números existentes entre ambos:
    A) Incluyéndolos;
    B) Excluyéndolos.


num1 = parseInt(prompt("Ingrese un numero: "))
num2 = parseInt(prompt("Ingrese un numero menor al anterior: "))

while (num1>num2) {
    num2=parseInt(prompt("ERROR. Ingrese un numero mayor al primero: "))
 
}
for (let i = num1; i <=num2; i++) {   //sin incluir  let i = num1+1; i <num2; i++)
    console.log(i)
    
3) Realizá un programa que permita al usuario ingresar un número entero n entre 1 y 10. La
computadora debe mostrar la tabla de multiplicar de n.}


num1 = parseInt(prompt("Ingrese un numero entre 1 y 10: "))

while (num1<1||num1>10) {
    num1 = parseInt(prompt("ERROR. Ingrese un numero entre 1 y 10: "))
}


for (let i = 0; i <=10 ; i++) {
    console.log(`${num1}*${i} = ${num1*i}`)
    
    
}

4) Realizá un programa que permita al usuario ingresar un número natural n. La computadora debe
mostrar los primeros n múltiplos de 3 excepto aquellos que sean a la vez múltiplos de 5.



num1 = parseInt(prompt("Ingrese un numero natural: "))

while (num1<0) {
    num1 = parseInt(prompt("Error. Ingrese un numero natural: "))
}

for (let i = 0; i < num1; i++) {
    if (i%5!=0){
        num = 3*i
        console.log(num)    
    }
   
}

*/

