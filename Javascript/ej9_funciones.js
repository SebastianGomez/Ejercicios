/*
Una función que dado un número de mes y me devuelva la cantidad de
días de ese mes (suponiendo que no es un año bisiesto).
*/

function mes(n) {
    if (n ==1||n==3||n==5||n==7||n==8||n==10||n==12){
        console.log("31 dias")
    }
    else if (n==2) {
        console.log("28 dias")
    }
    else {
        console.log("30 dias")
    }
}
