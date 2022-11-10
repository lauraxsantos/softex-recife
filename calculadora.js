var num1 = prompt('Digite um número: ');
var num2 = prompt('Digite o segundo número: ');
var op = prompt('Escolha um operador aritmético(* + / -): ');
var result;

if (op === '/') {
  result = parseInt(num1) / parseInt(num2);
  if(parseInt(num1) % parseInt(num2) !== 0){
    console.log(parseInt(num1) % parseInt(num2))
  }
} else if (op === '+') {
  result = parseInt(num1) + parseInt(num2);
} else if (op === '-') {
  result = parseInt(num1) - parseInt(num2);
} else if (op === '*') {
  result = parseInt(num1) * parseInt(num2);
} else {
  console.log('Você digitou um operador inválido');
}

console.log(result);
