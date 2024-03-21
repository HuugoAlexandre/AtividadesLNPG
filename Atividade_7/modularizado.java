import java.util.Scanner;

public class modularizado {

    	static double saldo = 1000.00;

	public static void constaSaldoAtual(){
		System.out.println("Seu saldo atual é: R$" + saldo);
	}

	public static void mostrarOpcoes() {
		System.out.println("Escolha uma opção:");
	    	System.out.println("1 - Saque");
	    	System.out.println("2 - Depósito");
	    	System.out.println("3 - Consultar Saldo");
	}

	public static void depositar(double valor) {
		saldo += valor;
	}

	public static boolean verificaSaldo(double valor) {
		return valor > saldo;
	}

	public static void main(String[] args) {	
	    	Scanner scanner = new Scanner(System.in);
	    	int opcao;
	    	double valor;
	
	    	System.out.println("Bem vindo ao Caixa Eletrônico");
		constaSaldoAtual();
	    	mostrarOpcoes();
	
		opcao = scanner.nextInt();
	
	    	if (opcao == 1) {
	        	System.out.println("Digite o valor do saque:");
	        	valor = scanner.nextDouble();
				
	        	if (verificaSaldo(valor)) {
				
	            		System.out.println("Saldo insuficiente.");
	        	} else {
		            	saldo -= valor;
		            	System.out.println("Saque de R$" + valor + " realizado.");
	        	}
	    	} else if (opcao == 2) {
	        	System.out.println("Digite o valor do depósito:");
	        	valor = scanner.nextDouble();
			depositar(valor);
			System.out.println("Depósito de R$" + valor + " realizado.");
	        	
	    	} else if (opcao == 3) {
	        	constaSaldoAtual();
	    	} else {
	        	System.out.println("Opção inválida.");
	    	}
	
	    	scanner.close();
    }
}

