/*
 * Entradas:
 * 1. Número de termos para calcular pi
 */

import java.util.Scanner;

public class ex02 {

    public static void main(String[] args) {
        System.out.println("Informe o número de termos para calcular pi: ");
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        double pi = Math.pow(calculaPi(n), 1.0/3.0);
        String piFormatted = String.format("%.5f", pi);
        System.out.println("O valor aproximado de pi com " + n + " termos é: " + piFormatted);
        
        in.close();
    }

    public static double calculaPi(int n) {
        double soma = 0.0;
        int denominador = 1;

        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                soma += 1.0 / (double) (denominador * denominador * denominador);
            } else {
                soma -= 1.0 / (double) (denominador * denominador * denominador);
            }
            denominador += 2;
        }
        return soma * 32;
    }
}