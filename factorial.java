import java.util.Scanner;

public class factorial
{
    public static void main(String[] args)
    {
        Scanner entrada = new Scanner(System.in);
        int limite = 0;
        int resultado = 0;

        System.out.print("\n########## Programa para calcular el enesimo numero factorial ##########\n\n");
        System.out.print(" Inserte el enesimo numero factorial: ");

        limite = entrada.nextInt();
        entrada.close();

       resultado = factorial(limite);
       
       System.out.printf("\nEl valor de %d! es %d.\n\n", limite, resultado);
    }    

    public static int factorial(int limite)
    {
        if (limite == 0)
        {
            return 1;
        }

        else
        {
            return limite * factorial(limite - 1);
        }
    }
}
