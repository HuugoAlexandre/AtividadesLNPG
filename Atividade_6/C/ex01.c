#include <stdio.h>
#include <string.h>

// Função para comparar datas de nascimento
int compararDatas(char data1[], char data2[]) {
    return strcmp(data1, data2);
}

int main() {
    int N;
    printf("Informe a quantidade de passageiros: ");
    scanf("%d", &N);
    getchar(); // Limpa o buffer de entrada

    for (int i = 0; i < N; i++) {
        char possuiRG[20];
        char dataNascimentoRG[11];
        char possuiPassagem[20];
        char dataNascimentoPassagem[11];
        char assento[4];
        char enter;
        
        printf("Cliente %d, possui RG? (rg ou nao possui)\n", i + 1);
        fgets(possuiRG, sizeof(possuiRG), stdin); // scanf tava dando erro por ler só até o primeiro espaço em branco em 'nao possui', fgets resolveu
        possuiRG[strcspn(possuiRG, "\n")] = '\0'; // Remove a quebra de linha, antes a próxima iteração dava falha por capturar o \n

        if (strcmp(possuiRG, "nao possui") == 0) {
            printf("A saida e nessa direcao\n");
            continue;
        } 

        printf("Possui passagem? (passagem ou nao possui)\n");
        fgets(possuiPassagem, sizeof(possuiPassagem), stdin);
        possuiPassagem[strcspn(possuiPassagem, "\n")] = '\0'; // Remove a quebra de linha
        
        if (strcmp(possuiPassagem, "nao possui") == 0) {
            printf("A recepcao e nessa direcao\n");
            continue;
        } 

        printf("Informe a data de nascimento do RG (dd/mm/aaaa): ");
        scanf("%s", dataNascimentoRG);
        getchar(); // Limpa o buffer de entrada, antes a próxima iteração dava falha, buffer já estava preenchido
        printf("Informe a data de nascimento da passagem (dd/mm/aaaa): ");
        fgets(dataNascimentoPassagem, sizeof(dataNascimentoPassagem), stdin);
        dataNascimentoPassagem[strcspn(dataNascimentoPassagem, "\n")] = '\0'; // Remove a quebra de linha
        getchar();

        if (compararDatas(dataNascimentoRG, dataNascimentoPassagem) != 0) {
            printf("190\n");
            continue;
        }

        printf("Informe o assento: ");
        scanf("%s", assento);
        printf("O seu assento e %s, tenha um otimo dia\n", assento);

        getchar();
        printf("Pressione enter para continuar...\n");
        scanf("%c", &enter); // Só pra melhorar a visualização no terminal
        
    }
    return 0;
}
