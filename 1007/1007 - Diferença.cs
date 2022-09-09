using System;

class Program
{
    static void Main() {
        int a = Convert.ToInt16(Console.ReadLine());
        int b = Convert.ToInt16(Console.ReadLine());
        int c = Convert.ToInt16(Console.ReadLine());
        int d = Convert.ToInt16(Console.ReadLine());
        
        Console.WriteLine("DIFERENCA = {0}", (a*b)-(c*d));
    }
}
