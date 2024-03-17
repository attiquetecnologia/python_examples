console.log("Teste execução");

// console.time("meu time");
function incremento(): number{
    var aux: number = 0;
    for (var i=0; i<=1000000000; i++) {
        aux += i;
    }
    return aux;
}

function loop (){
    var aux: number = 0;
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
// >>> default: 865.757ms

inicio = console.time();
loop();
fim = console.timeEnd();
// console.timeEnd("fim tempo");
console.log("Tempo total loop JS =>");
// >>> default: 657.211ms

// CONCLUSÃO
//  Comparando os resultados com python é possível ver que as técnicas de otimização
// fizeram o script .py ficar ligeiramente mais rápido, diferença de 1ms, entretanto
// e também que o node é sim realmente mais rápido do que python, porém ao rodar o
// script diretamente no browser a diferença de desempenho em favor do python é brutal.