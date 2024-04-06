/*  Neste programa, o usuário poderia digitar uma entrada incorreta em alguns lugares
    do programa, como na seleção da opção, adicionar ou vender um produto (como um caracter,
    mesmo o programa esperando um valor inteiro) o que acabaria por quebrar o programa.
    Foram feitas modificações que não deixam o programa quebrar, ao mesmo tempo que
    avisam ao usuário da entrada inválida e pede uma nova entrada. 
 */



import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.Map;
import java.util.Scanner;

public class ControleEstoque {
    private static Map<String, Integer> estoque = new HashMap<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        while (true) {
            exibirMenu();
            int opcao = lerNumeroInteiro("Escolha uma opção:");
            if (opcao == Integer.MIN_VALUE) {
                System.out.println("Entrada inválida para opção.");
                continue;
            }

            switch (opcao) {
                case 1:
                    adicionarProduto();
                    break;
                case 2:
                    venderProduto();
                    break;
                case 3:
                    exibirEstoque();
                    break;
                case 4:
                    System.out.println("Saindo do programa...");
                    return;
                default:
                    System.out.println("Opção inválida!");
            }
        }
    }

    private static void exibirMenu() {
        System.out.println("Escolha uma opção:");
        System.out.println("1 - Adicionar Produto");
        System.out.println("2 - Vender Produto");
        System.out.println("3 - Exibir Estoque");
        System.out.println("4 - Sair");
    }

    private static void adicionarProduto() {
        System.out.println("Digite o nome do produto:");
        String nome = scanner.next();
        int quantidade = lerNumeroInteiro("Digite a quantidade do produto:");
        
        if (quantidade == Integer.MIN_VALUE) {
            System.out.println("Entrada inválida.");
            return;
        }

        if (estoque.containsKey(nome)) {
            quantidade += estoque.get(nome);
        }

        estoque.put(nome, quantidade);
        System.out.println("Produto adicionado com sucesso!");
    }

    private static void venderProduto() {
        System.out.println("Digite o nome do produto:");
        String nome = scanner.next();
        int quantidade = lerNumeroInteiro("Digite a quantidade a ser vendida:");
        
        if (quantidade == Integer.MIN_VALUE) {
            System.out.println("Entrada inválida.");
            return;
        }

        if (estoque.containsKey(nome)) {
            int estoqueAtual = estoque.get(nome);
            if (estoqueAtual >= quantidade) {
                estoque.put(nome, estoqueAtual - quantidade);
                System.out.println("Venda realizada com sucesso!");
            } else {
                System.out.println("Quantidade insuficiente em estoque!");
            }
        } else {
            System.out.println("Produto não encontrado em estoque!");
        }
    }

    private static void exibirEstoque() {
        System.out.println("Estoque atual:");
        for (String produto : estoque.keySet()) {
            int quantidade = estoque.get(produto);
            System.out.println(produto + ": " + quantidade);
        }
    }

    private static int lerNumeroInteiro(String mensagem) {
        int numero;
        try {
            System.out.println(mensagem);
            numero = scanner.nextInt();
        } catch (InputMismatchException e) {
            scanner.nextLine();
            return Integer.MIN_VALUE; // retorna um valor especial para indicar entrada inválida
        }
        return numero;
    }
}
