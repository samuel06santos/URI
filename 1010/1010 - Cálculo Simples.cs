using System;
using System.Globalization;
class Program
{
    static void Main()
   {
        (int u1, double v1) = GetValues();
        (int u2, double v2) = GetValues();

        string result = ((u1*v1)+(u2*v2)).ToString("F2", CultureInfo.InvariantCulture);

        Console.WriteLine($"VALOR A PAGAR: R$ {result}");
   }
    private static (int unity, double value) GetValues()
   {
        string[] values = Console.ReadLine().Split();
        
        int unity = int.Parse(values[1]);
        double value = double.Parse(values[2], CultureInfo.InvariantCulture);
        return (unity, value);
   }
}