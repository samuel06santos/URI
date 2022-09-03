using System;
class Program{
    static void Main(){
        double a,b,c;
        a = Convert.ToDouble(Console.ReadLine());
        b = Convert.ToDouble(Console.ReadLine());
        c = Convert.ToDouble(Console.ReadLine());
        a *= 2; b *= 3; c *= 5;
        Console.WriteLine("MEDIA = {0}",((a+b+c)/10).ToString("F1"));
    }
}
