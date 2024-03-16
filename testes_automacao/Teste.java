
public class Teste{
    public static void main(String... args){
        long tempoInicial = System.currentTimeMillis();
        int aux = 0;
        for (int i =0; i<=1000; i++){
            aux += i;
        }
        long tempoFinal = System.currentTimeMillis();
        System.out.print("Tempo execução JAVA ");
        System.out.println(tempoFinal-tempoInicial);
        System.err.println(aux);
    }
}