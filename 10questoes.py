var nome = "nathan";              // string
let idade = 30;                  // number
const aprovado = true;           // boolean
let endereco;                    // undefined
let telefone = null;             // null

console.log(nome);
console.log(idade);
console.log(aprovado);
console.log(endereco);
console.log(telefone);

let numero1 = 10;
let numero2 = 3;

console.log("Soma:", numero1 + numero2);
console.log("Subtração:", numero1 - numero2);
console.log("Multiplicação:", numero1 * numero2);
console.log("Divisão:", numero1 / numero2);
console.log("Resto:", numero1 % numero2);


let numero1 = 10;
let numero2 = 5;

if (numero1 > numero2) {
    console.log("O primeiro número é maior.");
} else if (numero1 < numero2) {
    console.log("O segundo número é maior.");
} else {
    console.log("Os números são iguais.");
}

let idade = 70;

if (idade < 18) {
    console.log("A pessoa é menor de idade.");
} else if (idade <= 65) {
    console.log("A pessoa é maior de idade.");
} else {
    console.log("A pessoa é idosa.");
}

let idade = 20;

let resultado = idade >= 18 ? "É maior de idade." : "É menor de idade.";

console.log(resultado);

for (let i = 1; i <= 10; i++) {
    console.log(i);
}


let numero = 1;

while (numero <= 5) {
    console.log(numero);
    numero++;
}

let numero2 = 1;

do {
    console.log(numero2);
    numero2++;
} while (numero2 <= 5);


function saudacao(nome) {
    return "Olá, " + nome + "! Seja bem-vindo(a)!";
}

console.log(saudacao("Josie"));

const calcularArea = function(base, altura) {
    return (base * altura) / 2;
};

console.log(calcularArea(10, 5));

let frutas = ["maçã", "banana", "laranja", "uva", "manga"];

console.log(frutas);

// push() - adiciona uma fruta
frutas.push("abacaxi");
console.log(frutas);

// pop() - remove a última fruta
frutas.pop();
console.log(frutas);

// slice() - seleciona parte do array
let algumasFrutas = frutas.slice(1, 3);
console.log(algumasFrutas);

// join() - transforma o array em texto
console.log(frutas.join(", "));