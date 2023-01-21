using System;

class Program
{
    static void Main()
    {
        int age = int.Parse(Console.ReadLine());
        Console.WriteLine($"{age/365} ano(s)");
        age %= 365;
        Console.WriteLine($"{age/30} mes(s)");
        age %= 30;
        Console.WriteLine($"{age} dia(s)");
    }
}