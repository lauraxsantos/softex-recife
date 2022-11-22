const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Nota 1: ", function(n1){
    rl.question("Nota 2: ", function(n2){
        var tot = 21 - (parseInt(n1) + parseInt(n2))
        if (tot > 10) {
            console.log("Você necessita de mais de 10 pontos para atingir 7")
        } else{
            console.log(`Você precisa de ${tot} para atingir nota suficiente`)
        }
        rl.close()
    });
});