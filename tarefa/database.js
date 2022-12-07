const seq = require("sequelize");

const seque = new seq("arquivo", "root", "senha", {
    host: 'localhost',
    dialect: 'mysql'
});

seque.authenticate()
.then(function(){
    console.log("Conexão realizada")
}).catch(function(){
    console.log("ERRO, falha na conexão")
});