/*
 * Entradas:
 * 1. Mês e ano (Ex: 01/2021) e IPCA (Ex: 0.25)
 * 
 * Caso esteja satisfeito com as entradas, basta digitar *
 * 
 */

import java.util.Scanner;

public class ex05 {

    public static void main(String[] args) {
        String menorMesAno = "", maiorMesAno = "";
        int totalMeses = 0;
        double menorIpca = Double.MAX_VALUE;
        double maiorIpca = Double.MIN_VALUE;
        double ipca, somaIpca = 0;

        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite o mês e ano (Ex: 01/2021) e IPCA: ");
        while(true){
            String entrada = scanner.nextLine();
            if(entrada.equals("*")){
                break;
            } 

            String[] partes = entrada.split(" ");
            String mesAno = partes[0];
            ipca = Double.parseDouble(partes[1]);

            somaIpca+=ipca;
            totalMeses++;

            if(ipca < menorIpca){
                menorIpca = ipca;
                menorMesAno = mesAno;
            }

            if(ipca > maiorIpca){
                maiorIpca = ipca;
                maiorMesAno = mesAno;
            }

        }
        
        System.out.println("Menor IPCA: " + menorIpca + " no mês/ano " + menorMesAno);
        System.out.println("Maior IPCA: " + maiorIpca + " no mês/ano " + maiorMesAno);
        System.out.println("Média do IPCA: " + somaIpca/totalMeses);

        scanner.close();
        
    }
    
}
