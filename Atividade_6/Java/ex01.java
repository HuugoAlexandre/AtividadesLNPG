/*
 * Entradas:
 * 1. Quantidade de passageiros
 * 2. RG (ou "nao possui")
 * 3. Passagem (ou "nao possui")
 * 4. Data de nascimento que consta no RG se necessário
 * 5. Data de nascimento que consta na passagem se necessário
 * 6. Assento se necessário
 */

import java.util.Scanner;

public class ex01 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Digite a quantidade de passageiros: ");
        int qtdPassageiros = in.nextInt();
        in.nextLine(); // Consumindo a nova linha pendente

        for (int i = 0; i < qtdPassageiros; i++) {
            System.out.println("Passageiro " + (i+1) + ", tem RG? (rg ou nao possui): ");
            String rg = in.nextLine();
            if (rg.equals("nao possui")) {
                System.out.println("A saída é nessa direção.");
                continue;       
            }

            System.out.println("Tem passagem? (passagem ou nao possui): ");
            String passagem = in.nextLine();
            if (passagem.equals("nao possui")) {
                System.out.println("A recepção é nessa direção.");
                continue;       
            }

            System.out.println("Digite a data de nascimento que consta no RG: ");
            String dataNascimentoRG = in.nextLine();
            System.out.println("Digite a data de nascimento que consta na passagem: ");
            String dataNascimentoPassagem = in.nextLine();
            if (!dataNascimentoRG.equals(dataNascimentoPassagem)) {
                System.out.println("190");
                continue;
            } 
            System.out.println("Informe seu assento: ");
            String assento = in.nextLine();
            System.out.println("O seu assento é o " + assento + ", tenha um ótimo dia.");
        }

        in.close();
    }
}
