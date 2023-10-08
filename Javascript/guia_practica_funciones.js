/*
Definí las siguientes funciones, asegurándote su correcto funcionamiento con algunos tests.
1) esPar, que devuelva si un número entero dado como parámetro es par o no.
*/


function esPar(n) {
    if (n%2==0){
        return(console.log("el numero es par"))
    }
    else {
        return(console.log("el numero es impar"))

    }
    
}
/*
2) obtenerResto, que devuelva el resto del cociente entre dos números enteros dados como parámetros 
(sin usar el operador %).
*/

function obtenerResto(n1,n2) {
   n3=parseInt((n1/n2))
   resto=n1-(n3*n2)
   return(resto)


}

/*3) imprimirSimbolo, que imprima por consola n veces un caracter en la misma línea.
Tanto n como el caracter se reciben como parámetro.
*/
/*
caracter = prompt("Ingrese un caracter: ")
n = parseInt(prompt("Ingrese un numero: "))
*/


function imprimirSimbolo(n,caracter) {
    resultado = caracter.repeat(n)
    console.log(resultado) 
        
   
}