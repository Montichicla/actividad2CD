public class Fibonacci1 {
	public static void main(String[] args) {
		int i=0;
		int a=0;
		int b=1;
		int c=0;
		System.out.println("Este algoritmo nos permitira representar la sucesion de Fibonacci."); 
		for (i=0; i<20; i++) {
			if (i<19) {
				System.out.print(a+", ");
				c=a+b;
				a=b;
				b=c;
			}else {
				System.out.print(a+".");
			}
		}
	}
	
}