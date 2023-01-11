using System;
using System.Globalization;
class Program
{
    static void Main()
    {
        int km = int.Parse(Console.ReadLine());
        double l = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
        string result = (km/l).ToString("F3", CultureInfo.InvariantCulture);
        Console.WriteLine($"{result} km/l");
    }
}