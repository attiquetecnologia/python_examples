console.log("Teste execução");

// console.time("meu time");
function incremento(){
    var aux = 0;
    for (var i=0; i<=1000; i++) {
        aux += i;
    }
    return aux;
}

function loop(){
    var aux = 0;
    while (aux <= 1000000000 ) {
        aux++;
    }
    console.log(aux);
}

inicio = console.time();
incremento()
fim = console.timeEnd();
// console.timeEnd("fim tempo");
console.log("Tempo total incremento JS =>");

inicio = console.time();
loop();
fim = console.timeEnd();
// console.timeEnd("fim tempo");
console.log("Tempo total loop JS =>");