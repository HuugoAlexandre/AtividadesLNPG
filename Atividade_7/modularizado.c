#include <stdio.h>

char pegaOperador() {
    char operador;
    printf("Digite a operação (+, -, *, /): ");
	scanf("%c", &operador);

    return operador;
}

float pegaPrimeiroNumero() {
    float num1;
    printf("Digite o primeiro número: ");
    scanf("%f", &num1);
    return num1;
}

float pegaSegundoNumero() {
    float num2;
    printf("Digite o segundo número: ");
    scanf("%f", &num2);
    return num2;
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
    char operador = pegaOperador();
    float num1 = pegaPrimeiroNumero();
    float num2 = pegaSegundoNumero();

    calcula(operador, num1, num2);
	
	return 0;
}
