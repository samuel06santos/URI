using System;
using System.Globalization;
class Program
{
    static void Main()
    {
        int h, vel;
        h = int.Parse(Console.ReadLine());
        vel = int.Parse(Console.ReadLine());
        string result = ((vel*h)/12.0).ToString("F3", CultureInfo.InvariantCulture);
        Console.WriteLine(result);
    }
}