/*
Crear una función que lea notas hasta que ingrese -1 y devuelve el
promedio de las notas leídas. ( aunque no se suele leer valores en una
función)
Una función que se llame siguiente, que reciba como
parámetro un valor entero, y devuelva el siguiente del número
ingresado como parámetro
*/


function leer() {
    nota = prompt("Ingrese una nota")
    cont = 0
    while(nota!="-1") {
        nota = prompt("Ingrese una nota")
        cont = cont+1


    }
return(`se leyeron ${cont} notas`)
}

function siguiente(n1) {
return (n1+1)
    
}

