/*
Una función que se denomine imprimirElDobleDelSiguiente que dado
un número por parámetro, imprima cual es el valor siguiente al el doble.
Usando las funciones definidas en los puntos 5) , 6) : siguiente, el
doble
*/
function doble(n) {
    return(n*2)
}


function siguiente(n) {
    return (n+1)
        
    }

function imprimirElDobleDelSiguiente(n) {
    return(siguiente(doble(n)))
    
}