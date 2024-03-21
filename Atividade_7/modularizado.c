#include <stdio.h>

char pegaOperador() {	
    	char operador;
	scanf("%c", &operador);
    	return operador;
}

float pegaNumero() {
    	float num;
    	scanf("%f", &num);
    	return num;
}

float soma(float num1, float num2) {
	return num1 + num2;
}

float subtracao(float num1, float num2){
	return num1 - num2;
}

float multiplicacao(float num1, float num2) {
	return num1 * num2;
}

float divisao(float num1, float num2) {
	return num1 / num2;
}

void mostraResultado(float resultado) {
	printf("Resultado: %.2f\n", resultado);
}

void calcula(char operador, float num1, float num2) {
	
    	float resultado;
	switch (operador) {
		case '+':
			resultado = soma(num1, num2);
			mostraResultado(resultado);
			break;
		case '-':
			resultado = subtracao(num1, num2);
			mostraResultado(resultado);
			break;
		case '*':
			resultado = multiplicacao(num1, num2);
			mostraResultado(resultado);
			break;
		case '/':
			if (num2 != 0) {
				resultado = divisao(num1, num2);
				mostraResultado(resultado);
			} else {
				printf("Erro! Divisão por zero.\n");
			}
			break;
		default:
			printf("Operador inválido.\n");
	}
}

int main() {
	printf("Digite a operação (+, -, *, /): ");
	char operador = pegaOperador();
	printf("Digite o primeiro número: ");
    	float num1 = pegaNumero();
	printf("Digite o segundo número: ");
    	float num2 = pegaNumero();

    	calcula(operador, num1, num2);
	
	return 0;
}
