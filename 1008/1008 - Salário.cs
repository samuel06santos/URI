using System;
using System.Globalization;
class Program
{
    static void Main() {
        int id = int.Parse(Console.ReadLine());
        int hours = int.Parse(Console.ReadLine());
        double hourValue = double.Parse(Console.ReadLine(), CultureInfo.CreateSpecificCulture("en-US"));
        string salary = (hours * hourValue).ToString("F2", CultureInfo.CreateSpecificCulture("en-US"));
        Console.WriteLine("NUMBER = {0}\nSALARY = U$ {1}", id, salary);
    }
}
