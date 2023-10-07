/* dado
Montse
26/09/22 */

import java.lang.Math;

class Dado{
	public static void main(String[]args){
		double numA = Math.random();
		// MinMax Scaling
		int a=1, b=6;
		double dado = Math.round (a+(b-a)*numA);
		System.out.println("El valor es: "+(int)dado);

	}
}