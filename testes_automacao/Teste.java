
public class Teste{
    public static void main(String... args){
        long tempoInicial = System.nanoTime();
        int aux = 0;
        for (int i =0; i<=1000; i++){
            aux += i;
        }
        long tempoFinal = System.nanoTime();
        System.out.print("Tempo execução incremento JAVA ");
        System.out.println(tempoFinal-tempoInicial);
        // >>> Tempo execução incremento JAVA 7746 ns


        tempoInicial = System.nanoTime();
        int i = 0;
        while ( i<=1000000000 ){
            i++;
        }
        tempoFinal = System.nanoTime();
        System.out.print("Tempo execução loop JAVA ");
        System.out.println(tempoFinal-tempoInicial);
        // >>> Tempo execução loop JAVA 245155406 ns

        /* CONCLUSÃO
         *  O que se conclui é que java é brutalemente mais veloz devido ao seu JIT
         * a JVM trabalha com just in time por isso os resultados em nano segundo
         * algo como 10^-9, ou seja, 6 zeros de diferença.
         */
    }
}