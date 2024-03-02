#include <stdio.h>
#include <math.h>

double calcular_pi(int n) {
    double soma = 0.0;
    int denominador = 1;

    for (int i = 0; i < n; i++) { 
        if (i % 2 == 0) { // O operador aritmético muda se o índice for par ou ímpar
            soma += 1.0 / (double)(denominador * denominador * denominador);
        } else {
            soma -= 1.0 / (double)(denominador * denominador * denominador);
        }
        denominador += 2;
    }

    return soma * 32.0;
}

int main() {
    int n;
    printf("Digite o numero de termos para calcular pi: ");
    scanf("%d", &n);

    double pi = pow(calcular_pi(n), 1.0 / 3.0);
    
    printf("Valor aproximado de pi com %d termos: %.5lf\n", n, pi);

    return 0;
}
