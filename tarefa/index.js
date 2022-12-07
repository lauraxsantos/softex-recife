const exp = require('express');
const conexion = exp();

const database = require("./database");

conexion.get("/", async (req, res) => {
    res.send("Conexão com o banco de dados")
});


conexion.listen(1010, () => {
    console.log("http://localhost:1010");
})