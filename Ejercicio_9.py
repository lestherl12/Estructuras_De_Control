using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EstructuraRepetitivaDoWhile4
{
    class Program
    {
        static void Main(string[] args)
        {
            int suma,valor;
            string linea;
            suma=0;
            do {
                Console.Write("Ingrese un valor:");
                linea = Console.ReadLine();
                valor=int.Parse(linea);
                if (valor!=9999) 
                {
                    suma=suma+valor;
                }
            }while (valor!=9999);
            Console.Write("El valor acumulado es ");
            Console.WriteLine(suma);
            if (suma==0) 
            {
                Console.WriteLine("El valor acumulado es cero.");
            }
            else 
            {
                if (suma>0) 
                {
                    Console.WriteLine("El valor acumulado es positivo.");
                } 
                else 
                {
                    Console.WriteLine("El valor acumulado es negativo");
                }
            }
            Console.ReadKey();
        }
    }
}
