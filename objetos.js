function Filme(nome, ano, pais){
    this.lista = [nome, ano,  pais];
    this.nome = nome;
    this.ano = ano;
    this.pais = pais;
};

function atributos(objeto){
    for(let el of Object.keys(objeto)){
        console.log(el);
    };
};

function elementos(lista){
    for(let elem of lista){
        console.log(elem);
    };
};
