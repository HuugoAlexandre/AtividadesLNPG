#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define QTD_QUESTS 10

typedef struct Participante {
    char nome[100];
    int respostas[QTD_QUESTS];
    int acertos;
} Participante;

void lerGabarito(int *gabarito) {
    for(int i = 0; i < QTD_QUESTS; i++) {
        scanf("%d", gabarito + i);
        if(gabarito[i] <= 0 || gabarito[i] > 5) {
            printf("Gabarito invalido para a questao %d\n", i+1);
            printf("A resposta para uma questao deve ser um numero entre 1 e 5\n");
            exit(1);
        }
    }
    scanf("\n");
}

void ordenaPorNome(Participante *participantes, int n_participantes) {
    for(int i = 0; i < n_participantes; i++) {
        for(int j = i+1; j < n_participantes; j++) {
            if(strcmp(participantes[i].nome, participantes[j].nome) > 0) {
                Participante tmp = participantes[i];
                participantes[i] = participantes[j];
                participantes[j] = tmp;
            }
        }
    }
}

void calculaNotas(Participante *participantes, int n_participantes, int *gabarito) {
    int nota;
    for(int i = 0; i < n_participantes; i++) {
        nota = 0;
        for(int j = 0; j < QTD_QUESTS; j++) {
            if(participantes[i].respostas[j] == gabarito[j])
                nota++;
        }
        participantes[i].acertos = nota;
    }
}

int main() {

    int gabarito[QTD_QUESTS] = {};
    lerGabarito(gabarito);

    int n_participante = 0;
    int cap_participantes = 10;
    Participante *participantes = malloc(sizeof(Participante) * cap_participantes);;

    while(1) {
       scanf("%s", participantes[n_participante].nome); //lendo o nome do participante
       if(strcmp(participantes[n_participante].nome, "*") == 0) break;

       for (int i = 0; i < QTD_QUESTS; i++) {
           scanf("%d", &participantes[n_participante].respostas[i]);
       }

       n_participante++;
       if(n_participante == cap_participantes) {
           cap_participantes *= 2;
           participantes = realloc(participantes, sizeof(Participante) * cap_participantes);
       }
    }

    ordenaPorNome(participantes, n_participante);
    calculaNotas(participantes, n_participante, gabarito);

    printf("Lista dos participantes com suas respectivas notas:\n");
    for(int i = 0; i < n_participante; i++) {
        printf("%s %d\n", participantes[i].nome, participantes[i].acertos);
    }
    printf("\n");

    printf("Menor e maior nota:\n");
    int menor_nota = 0, maior_nota = 0;
    for(int i = 1; i < n_participante; i++) {
        if(participantes[i].acertos < participantes[menor_nota].acertos) menor_nota = i;
        if(participantes[i].acertos > participantes[maior_nota].acertos) maior_nota = i;
    }
    printf("A menor nota foi: %d, do participante: %s\n", participantes[menor_nota].acertos, participantes[menor_nota].nome);
    printf("A maior nota foi: %d, do participante: %s\n", participantes[maior_nota].acertos, participantes[maior_nota].nome);
    printf("\n");

    //percentual de participantes com mais da metade de acertos
    int qtd_acima_metade = 0;
    for(int i = 0; i < n_participante; i++) {
        if(participantes[i].acertos > QTD_QUESTS / 2) qtd_acima_metade++;
    }
    printf("Percentual de participantes com mais da metade de acertos: %.2f%%\n", (float)qtd_acima_metade / n_participante * 100);

    free(participantes);
    return 0;
}
