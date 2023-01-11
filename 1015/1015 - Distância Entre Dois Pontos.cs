using System;
using System.Globalization;
class Program
{
    static void Main()
    {
        double x1, x2, y1, y2;
        string[] values1 = Console.ReadLine().Split();
        string[] values2 = Console.ReadLine().Split();
        x1 = double.Parse(values1[0]); y1 = double.Parse(values1[1]);
        x2 = double.Parse(values2[0]); y2 = double.Parse(values2[1]);

        string d = ( Math.Pow( ( Math.Pow(x2-x1, 2) + Math.Pow(y2-y1, 2) ), 0.5) )
            .ToString("F4", CultureInfo.InvariantCulture);
        Console.WriteLine(d);
    }
}