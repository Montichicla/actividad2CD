/* sucesiones
Montse 
26/09/22 */

import java.lang.Math;

class Sucesiones{
	public static void main(String[]args){
		double xn;
		for (int n=-1; n<=4; n++){
			xn = 1/Math.pow(2,n)-1;
			System.out.print(" "+xn+" ");
		}
		System.out.print("\n");	
		int n=0;
		double sn;
		int limite = 10; // quiero n terminos de la sucesion
		while(n<limite){
			sn = Math.pow(2,n)+4*Math.pow(3,n);
			System.out.println(" "+sn+" ");
			n++;
		}
	}
}