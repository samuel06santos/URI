using System;
class Program
{
    static void Main(string[] args) {
        int a,b,c,maior,maior2;
        var abc = Console.ReadLine().Split();
        a = Convert.ToInt16(abc[0]);
        b = Convert.ToInt16(abc[1]);
        c = Convert.ToInt16(abc[2]);
        maior = (a + b + Math.Abs(a - b))/2;
        maior2 = (maior + c + Math.Abs(maior - c))/2;
        Console.WriteLine("{0} eh o maior", maior2.ToString("F0"));
    }
}
