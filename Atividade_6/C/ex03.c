#include <stdio.h>

int main() {
    int n, quant;
    double bonus = 0.0, valorTotal = 0.0, valorArrecadado = 0.0;
    double valorJogo = 19.9;

    printf("Informe a quantidade de jogos vendidos: ");
    scanf("%d", &n);

    quant = n;
    
    while (n >=15) {
        bonus = bonus + 0.08 * (valorJogo * quant);
        n -= 15;
    }

    valorArrecadado = valorJogo * quant;
    valorTotal = (valorJogo * quant * 0.5) + bonus;
    printf("O valor total arrecado: %.2lf\n", valorArrecadado);
    printf("Valor ganho como bonus: %.2lf\n", bonus);
    printf("Valor total a ser pago para Catarina: %.2lf\n", valorTotal);
    
    return 0;
}
