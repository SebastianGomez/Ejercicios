/*1) Realizá un programa que permita al usuario ingresar un número entero. La computadora debe
indicar si se trata de un número par o impar.


num = parseInt(prompt("Ingrese un número: "))

resto = num%2

if (resto ===0) {
    console.log(num+" es par")

}else {
    console.log(num+" es impar")
}



2) Realizá un programa que permita al usuario ingresar la cantidad de inscriptos a una conferencia
y la cantidad de asientos disponibles el auditorio. La computadora debe indicar si alcanzan los
asientos, en caso contrario, indicar cuántos faltan para que todos los inscriptos puedan sentarse.



inscriptos = parseInt(prompt("Número de inscriptos: "))
numero_asientos = parseInt(prompt("Número de asientos: "))

total= numero_asientos-inscriptos

if (total>0) {
    console.log("El numero de asientos alcanza")

}else {
    console.log("faltan "+(-1*total+" asientos"))

}

5) Realizá un programa que permita al usuario ingresar su edad (entre 1 y 120 años) y su género
('F' para mujeres, 'M' para hombres). La computadora debe indicar si la persona está en edad de
jubilarse. En caso de haber ingresado valores erróneos (edad fuera de rango o género inválido),
informar tal situación.


edad = parseInt(prompt("Ingrese una edad entre 1 y 120: "))
sexo = prompt("Ingrese M o F: ")

if ((sexo!=="M") && (sexo!=="F")) {  //pregunar
    console.log("El genero es incorrecto: ")
    }
else if (edad<1 || edad>120){
    console.log("La edad es incorrecta: ")
}
else {
    if (sexo==="M"){
        if (edad >65){
            console.log("Esta en edad de jubilarse ")
        }
        else{
            console.log("No esta en edad de jubilarse: ")
        }
    }
    else {
        if(edad>60){
            console.log("Esta en edad de jubilarse ")
        }
        else {
            console.log("No esta en edad de jubilarse: ")
        }
    }
}

*/