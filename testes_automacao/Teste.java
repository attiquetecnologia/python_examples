
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


        tempoInicial = System.nanoTime();
        int i = 0;
        while ( i<=1000000000 ){
            i++;
            System.err.println(i);
        }
        tempoFinal = System.nanoTime();
        System.out.print("Tempo execução loop JAVA ");
        System.out.println(tempoFinal-tempoInicial);
    }
}