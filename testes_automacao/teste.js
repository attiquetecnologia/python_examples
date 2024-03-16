console.log("Teste execução");
inicio = Date.now();
// console.time("meu time");
aux = 0;
for (var i=0; i<=1000; i++) {
    aux += i;
}
fim = Date.now();
// console.timeEnd("fim tempo");
console.log("Tempo total JS", fim-inicio)