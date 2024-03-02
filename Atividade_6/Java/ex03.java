import java.util.Scanner;

public class ex03 {
    public static void main(String[] args) {
        System.out.println("Informe a quantidade de brinquedos vendidos: ");
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        final double precoBrinquedo = 19.9; 
        final double totalVendas = n * precoBrinquedo;

        int bonusQuant = n / 15;
        double valorBonus = bonusQuant * (totalVendas*0.08);
        double salario = (totalVendas/2) + valorBonus;

        System.out.println("Valor arrecadado com as vendas: R$" + totalVendas);
        System.out.println("Valor arrecadado com bônus: " + valorBonus);
        System.out.println("Salário total: " + salario);

        in.close();
    }
}
