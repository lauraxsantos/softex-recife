class Banco{
    constructor(conta, saldo, tipoDeConta, Agencia) { 
        this.conta = conta; 
        this.saldo = saldo;
        this.tipoDeConta = tipoDeConta;
        this.Agencia = Agencia;
    }
    
    buscarSaldo(){
        return this.saldo;
    }

    deposito(valor){
        this.saldo += valor 
    }

    saque(valor){
        this.saldo -= valor
    }

    numeroDaConta(){
        return this.conta
    }



}
