using System;
class Program
{
    static void Main()
    {
        int hi, mi, hf, mf, th, tm;
        string[] values = Console.ReadLine().Split();
        hi = int.Parse(values[0]); mi = int.Parse(values[1]); hf =  int.Parse(values[2]); mf = int.Parse(values[3]);
        th = hf - hi;
        tm = mf - mi;
        
        if (tm < 0)
        {
            tm += 60;
            th -= 1;
        }
        if (tm == 0 && th <= 0)
        {
            th += 24;
        }
        if (th < 0)
        {
            th += 24;
        }
        Console.WriteLine($"O JOGO DUROU {th} HORA(S) E {tm} MINUTO(S)");
    }
}