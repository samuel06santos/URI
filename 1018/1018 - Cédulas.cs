using System;
class Program
{
    static void Main()
    {
        int v = int.Parse(Console.ReadLine());
        int[] array = {100, 50, 20, 10, 5, 2, 1};

        Console.WriteLine(v);
        for (int i=0; i<array.Length; i++)
        {
            Console.WriteLine($"{ (v/array[i]) } nota(s) de R$ { array[i] },00");
            v %= array[i];
        }
    }
}