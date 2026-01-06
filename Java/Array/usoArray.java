import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		String[]  Paises = new String [5];

		System.out.println("Introduce nombres de Paises.\n");

		for (int i = 0; i < Paises.length; i++) {

			Paises[i] = input.nextLine();

		}

        System.out.println("Tu lista de Paises.\n");

		for (String paises : Paises) System.out.println(paises);


	}
}
