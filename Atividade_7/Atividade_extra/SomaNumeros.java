import java.util.Scanner;

public class SomaNumeros {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite um número inteiro positivo: ");
        int n = scanner.nextInt();
        int soma = somaRecursiva(n);
        System.out.println("A soma dos números de 1 a " + n + " é: " + soma);
        scanner.close();
    }

    public static int somaRecursiva(int n) {
        if (n == 1) {
            return 1;
        } else {
            return n + somaRecursiva(n - 1);
        }
    }
}
