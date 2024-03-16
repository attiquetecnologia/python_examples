using System;
public class Teste
{
    public static void Main()
    {
        Stopwatch stopWatch = new Stopwatch();
        stopWatch.Start();
        int aux = 0;
        for (int i = 0; i<=1000; i++){
            aux += i;
        }
        stopwatch.Stop();
        Console.WriteLine("Tempo CS ", stopWatch.Elapsed);
    }
}