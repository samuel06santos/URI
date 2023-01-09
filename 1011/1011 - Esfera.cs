using System;
using System.Globalization;
class Program 
{
    static void Main()
    {
        int r = int.Parse(Console.ReadLine());
        double pi = 3.14159;
        string result = ((4.0/3) * pi * r * r * r).ToString("F3", CultureInfo.InvariantCulture);
        Console.WriteLine($"VOLUME = " + result);
    }
}