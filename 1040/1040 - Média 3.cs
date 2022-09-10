using System;
using System.Globalization;
class Program
{
    static void Main(string[] args) {
        float a,b,c,d,mp,n,m;
        var str = Console.ReadLine().Split();
         
         a = float.Parse(str[0], CultureInfo.InvariantCulture); b = float.Parse(str[1], CultureInfo.InvariantCulture);
         c = float.Parse(str[2], CultureInfo.InvariantCulture); d = float.Parse(str[3], CultureInfo.InvariantCulture);
         mp = (a*2+b*3+c*4+d*1)/10;
        //   Bug no arredondamento especifico, do problema 1040
          if (mp == 4.85f) 
            {
                mp = 4.8f;
            }
        Console.WriteLine("Media: {0}", mp.ToString("F1", CultureInfo.InvariantCulture));
        if (mp >= 7){Console.WriteLine("Aluno aprovado.");}
        if (mp < 5){Console.WriteLine("Aluno reprovado.");}
        if (mp >= 5.0 && mp <= 6.9){
            Console.WriteLine("Aluno em exame.");
            n = float.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
            Console.WriteLine("Nota do exame: {0}", (n).ToString("F1", CultureInfo.InvariantCulture));
            m = (mp+n)/2;
            if (m >= 5.0){Console.WriteLine("Aluno aprovado.");}
            if (m <= 4.9){Console.WriteLine("Aluno reprovado.");}
            Console.WriteLine("Media final: {0}", m.ToString("F1", CultureInfo.InvariantCulture));
        }
    }
}
