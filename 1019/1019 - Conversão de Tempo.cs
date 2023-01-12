using System;
using System.Globalization;
class Program
{
    static void Main()
    {
        int sec, h, h2, m, m2, s; 
        sec = int.Parse(Console.ReadLine());
        h = sec/3600; h2 = sec % 3600;
        m = h2/60; m2 = h2 % 60;
        s = m2 % 60;
        Console.WriteLine($"{h}:{m}:{s}");
    }
}