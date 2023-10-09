//6. Escribe un programa que pida dos números y escriba en la pantalla cual es el
//mayor.
/*
num1 = parseInt(prompt("Ingrese un numero: "))
num2 = parseInt(prompt("Ingrese un numero: "))


if (num1>num2) {
    console.log(num1 + " es el numero mas grande")
  
} else if (num1<num2) {
    console.log(num2 + " es el numero mas grande")

}  else {
    console.log("Los numeros son iguales")
    
}

*/


//7. Escribe un programa que pida 3 números y escriba en la pantalla el mayor de
//los tres.
/*
num1 = parseInt(prompt("Ingrese un numero: "))
num2 = parseInt(prompt("Ingrese un numero: "))
num3 = parseInt(prompt("Ingrese un numero: "))

if (num1>num2) {
    if (num1>num3){
        console.log("El numero mas grande es: "+num1)
    }
    else {
        console.log("El numero mas grande es: "+num3)
    }

} else if (num2>num3) {
    console.log("El numero mas grande es: "+num2)
}else {
    console.log("El numero mas grande es: "+num3)

}

*/


//8. Escribe un programa que pida un número y diga si es divisible por 2
/*
num1 = parseInt(prompt("Ingrese un numero: "))

resto = num1%2
if (resto===0) {
    console.log(num1+" SI es divisible por 2")

}else {
    console.log(num1+" NO es divisible por 2")
}

*/


//9. Escribe un programa que pida una frase y escriba cuantas veces aparece la
//letra a
/*
frase = prompt("Ingrese una frase: ")
frase = frase.toLowerCase() //convierte la frase a minuscula
letra = prompt("Ingrese una letra: ")
letra = letra.toLowerCase()
contador = 0
for (let i = 0; i < frase.length; i++) {//recorre la frase
    if (frase[i]===letra) {
        contador++
    }
    
}
console.log("La letra "+letra+" aparece "+contador+" veces en la frase: "+frase)
*/


//10. Escribe un programa que pida una frase y escriba las vocales que aparecen
/*
frase = prompt("Ingrese una frase: ")
frase = frase.toLowerCase() //convierte la frase a minuscula

contador = 0

for (let i = 0; i < frase.length; i++) {
    if(frase[i] ==="a"||frase[i] ==="e"||frase[i] ==="i"||frase[i] ==="o"||frase[i] ==="u") {
        console.log(frase[i])
        contador+=1
    }
    
}


console.log(frase)

*/


//11. Escribe un programa que pida una frase y escriba cuántas de las letras que
//tiene son vocales


frase = prompt("Ingrese una frase: ")
frase = frase.toLowerCase() //convierte la frase a minuscula

contador = 0

for (let i = 0; i < frase.length; i++) {
    if ("aeiou".includes(frase[i]))
    {contador+=1}

}


console.log(frase)
console.log("hay "+contador+" vocales")


