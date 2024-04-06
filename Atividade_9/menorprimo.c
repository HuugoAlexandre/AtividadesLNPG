#include <stdio.h>
#include <stdlib.h>

/*
Erro 1.

O erro pode acontecer quando o usuário digita um caracter,
C interpreta como inteiro, então fiz uma função que avise ao usuário
da entrada inválida e encerro o programa.

Erro 2.

Pode acontecer da entrada ser um valor tão grande que estoure o limite do valor
que int suporta. Depois de algumas tentativas cheguei nesse número, 2147483628,
como sendo o último número inteiro suportado dado o contexto de encontrar o próximo primo. 
Um int em C é um pouco maior do que isso (2147483647), mas quando tentei valores
superiores ao número citado (2147483628) o programa retorna 2 como sendo o menor
número primo. Poderia trocar o tipo de dado para long int em um sistema de 64 bits,
mas não acho que seja o foco da atividade.


Obs: Se entendi bem, a entrada pode ser um número qualquer, não precisando ser primo,
então a entrada pode ser um número negativo, ao contrário do valor primo.
*/


/*
Este programa implementa um algoritmo para encontrar o menor número primo maior que um número inteiro fornecido pelo usuário.
*/

// Função para verificar se um número é primo
int verificar_primo(int num) {
    if (num <= 1)  
        return 0; // Não é primo
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0)
            return 0; // Não é primo
    }
    return 1; // É primo
}

// Função para encontrar o próximo número primo após um número dado
int proximo_primo(int num) {
    num++;
    while (!verificar_primo(num))
        num++;
    return num;
}

int verifica_entrada() {
    int n;
    if (scanf("%d", &n) != 1) {
        printf("Entrada invalida.\n");
        exit(1); 
    }

    if (n > 2147483628) { 
        printf("Valor muito alto para int.\n");
        exit(1);
    }

    return n;
}

int main() {
    int num;
    printf("Digite um numero inteiro: ");
    num = verifica_entrada();
    int primo = proximo_primo(num);
    printf("O menor numero primo maior que %d eh: %d\n", num, primo);
    
    return 0;
}