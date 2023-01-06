using System;
using System.Globalization;
class Program
{
    static void Main() {
        string nome = Console.ReadLine();
        double salary = double.Parse(Console.ReadLine(), CultureInfo.CreateSpecificCulture("en-US"));
        double amount = double.Parse(Console.ReadLine(), CultureInfo.CreateSpecificCulture("en-US"));
        string result = (salary + (amount*0.15)).ToString("F2", CultureInfo.CreateSpecificCulture("en-US"));
        Console.WriteLine("TOTAL = R$ " + result);
    }
}
