const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Nota 1 ? ', function (n1) {
  rl.question('Nota 2? ', function (n2) {
    rl.question('Nota 3 ?', function(n3){
      var tot = (parseInt(n1)+ parseInt(n2) + parseInt(n3))/3
      if (tot >= 7) {
        console.log("Aprovado!")       
      }else{
        console.log("Reprovado!")
      }
      rl.close();
    });
  });
});

// rl.on('close', function () {
//   console.log('\nBYE BYE !!!');
//   process.exit(0);
// });

