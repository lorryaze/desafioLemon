var scanf = require('scanf');
 
console.log('Insira aqui o consumo de energia dado em KWH: ');

var consumo = scanf('%f');
const tarifaSI = 0.5572

console.log('Consumo: %f, type: %s', consumo, typeof consumo); 
console.log('Tarifa Sem Imposto:', tarifaSI, typeof tarifaSI); 
