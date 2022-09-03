using System;
class Program{
    static void Main(){
        double a,b;
        a = Convert.ToDouble(Console.ReadLine());
        b = Convert.ToDouble(Console.ReadLine());
        a *= 3.5; b *= 7.5;
        Console.WriteLine($"MEDIA = {((a+b)/11).ToString("F5")}");
    }
}
