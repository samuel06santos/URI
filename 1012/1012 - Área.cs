using System;
using System.Globalization;
class Program
{
    static void Main()
    {
        double a, b, c, pi;
        pi = 3.14159;
        string[] values = Console.ReadLine().Split();
        a = double.Parse(values[0]); b = double.Parse(values[1]); c = double.Parse(values[2]);
        
        string triangle = ((a*c)/2.0).ToString("F3", CultureInfo.InvariantCulture);
        string circle = (pi*(c*c)).ToString("F3", CultureInfo.InvariantCulture);
        string trapeze = ((a+b)*c/2.0).ToString("F3", CultureInfo.InvariantCulture);
        string square = (b*b).ToString("F3", CultureInfo.InvariantCulture);
        string rectangle = (a*b).ToString("F3", CultureInfo.InvariantCulture);

        Console.WriteLine($"TRIANGULO: {triangle}\nCIRCULO: {circle}\nTRAPEZIO: {trapeze}\nQUADRADO: {square}\nRETANGULO: {rectangle}");
    }
}