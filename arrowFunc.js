const func = function(){
    return 5 + 5
}

const func2 = function(op, val1, val2){
    return eval(`${val1} ${op} ${val2}`)
}

const arfunc = (op, val1, val2) => eval(`${val1} ${op} ${val2}`);
