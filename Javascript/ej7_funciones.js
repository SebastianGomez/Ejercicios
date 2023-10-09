/*

Una función que se denomine imprimirValores que dado un número
por parámetro, imprima cual es el valor siguiente, el doble y el
cuadrado. Usando las funciones definidas en los puntos 5) , 6) y 7) :
siguiente, el doble y el cuadrado

*/

function cuadrado(n) {
    return(n**2)    
}

function doble(num) {
    return(num*2)
}

function siguiente(n1) {
    return (n1+1)
        
}
    


function imprimirValores(n) {
    console.log(cuadrado(n))
    console.log(doble(n))
    console.log(siguiente(n))
    
}