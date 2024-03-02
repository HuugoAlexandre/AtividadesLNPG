#include <stdio.h>
#include <stdlib.h>
#include <float.h>

int main() {
    char mes_ano[10];
    double ipca, soma_ipca = 0.0;
    double menor_ipca = DBL_MAX;
    double maior_ipca = -DBL_MAX;
    char menor_mes_ano[10], maior_mes_ano[10];
    int total_meses = 0;

    while (1) {
        scanf("%s", mes_ano);
        if (mes_ano[0] == '*') {
            break;
        }
        scanf("%lf", &ipca);

        soma_ipca += ipca;
        total_meses++;

        if (ipca < menor_ipca) {
            menor_ipca = ipca;
            sprintf(menor_mes_ano, "%s", mes_ano);
            getchar();
        }

        if (ipca > maior_ipca) {
            maior_ipca = ipca;
            sprintf(maior_mes_ano, "%s", mes_ano);
            getchar();
        }
    }

    printf("Menor IPCA: %.2lf (%s)\n", menor_ipca, menor_mes_ano);
    printf("Maior IPCA: %.2lf (%s)\n", maior_ipca, maior_mes_ano);
    printf("Media do IPCA: %.2lf\n", soma_ipca / total_meses);

    return 0;
}

