import java.util.Scanner;

public class fibonacci
{
    public static void main(String[] args)
    {
        Scanner entrada = new Scanner(System.in);
        int limite = 0;
        int resultado = 0;

        System.out.print("\n########## Programa para calcular el enesimo numero de la secuencia de fibonacci ##########\n\n");
        System.out.print(" Inserte el indicee del numero a calcular: ");

        limite = entrada.nextInt();
        entrada.close();

       resultado = fibonacci(limite);
       
       System.out.printf("\nEl valor del indice %d! es %d.\n\n", limite, resultado);
    }    

    public static int fibonacci(int limite)
    {
        if (limite == 1 || limite == 2)
        {
            return limite;
        }

        else if (limite <= 0)
        {
            return 0;
        }

        else
        {
            return fibonacci(limite - 1) + fibonacci(limite - 2);
        }
    }
}
