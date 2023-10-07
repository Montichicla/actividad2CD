import java.util.Scanner;
public class fac{
    public static void main(String[] args){
        Scanner a = new Scanner(System.in);
        int N = 0;
        int R = 0;

        System.out.print("Dado un numero n, imprima el n-esimo factorial. Dime el numero del que quieres saber su factorial: ");
        N = a.nextInt();
        a.close();

       R = factorial(N);
       
       System.out.printf("\nEl valor de %d! es %d.\n\n", N, R);
    }    

    public static int factorial(int N)
    {
        if (N == 0)
        {
            return 1;
        }

        else
        {
            return N * factorial(N - 1);
        }
    }
}