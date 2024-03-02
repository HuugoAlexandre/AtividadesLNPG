/*
 * Sequência de entradas:
 *   
 * 1. Gabarito, cada resposta separada por espaço
 * 2. Nome do participante
 * 3. Respostas do participante, cada resposta separada por espaço
 
 * Caso queira parar de inserir participantes, basta digitar * no luga do nome
*/

import java.util.Scanner;
import java.util.Arrays;

public class ex04 {

    static final int QTD_QUESTS = 10;

    static class Participante {
        String nome;
        int[] respostas = new int[QTD_QUESTS];
        int acertos;

        Participante(String nome) {
            this.nome = nome;
        }
    }

    public static void lerGabarito(int[] gabarito) {
        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < QTD_QUESTS; i++) {
            gabarito[i] = scanner.nextInt();
            if (gabarito[i] <= 0 || gabarito[i] > 5) {
                System.out.println("Gabarito invalido para a questao " + (i + 1));
                System.out.println("A resposta para uma questao deve ser um numero entre 1 e 5");
                System.exit(1);
            }
        }
        
        
    }

    public static void ordenaPorNome(Participante[] participantes) {
        Arrays.sort(participantes, (a, b) -> a.nome.compareTo(b.nome));
    }

    public static void calculaNotas(Participante[] participantes, int[] gabarito) {
        for (Participante participante : participantes) {
            int nota = 0;
            for (int j = 0; j < QTD_QUESTS; j++) {
                if (participante.respostas[j] == gabarito[j])
                    nota++;
            }
            participante.acertos = nota;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] gabarito = new int[QTD_QUESTS];
        lerGabarito(gabarito);

        int n_participante = 0;
        int cap_participantes = 10;
        Participante[] participantes = new Participante[cap_participantes];

        while (true) {
            String nome = scanner.next();
            if (nome.equals("*")) break;

            participantes[n_participante] = new Participante(nome);

            for (int i = 0; i < QTD_QUESTS; i++) {
                participantes[n_participante].respostas[i] = scanner.nextInt();
            }

            n_participante++;
            if (n_participante == cap_participantes) {
                cap_participantes *= 2;
                participantes = Arrays.copyOf(participantes, cap_participantes);
            }
        }

        participantes = Arrays.copyOf(participantes, n_participante);
        ordenaPorNome(participantes);
        calculaNotas(participantes, gabarito);

        System.out.println("Lista dos participantes com suas respectivas notas:");
        for (Participante participante : participantes) {
            System.out.println(participante.nome + " " + participante.acertos);
        }
        System.out.println();

        int menor_nota = 0, maior_nota = 0;
        for (int i = 1; i < n_participante; i++) {
            if (participantes[i].acertos < participantes[menor_nota].acertos) menor_nota = i;
            if (participantes[i].acertos > participantes[maior_nota].acertos) maior_nota = i;
        }
        System.out.println("Menor nota: " + participantes[menor_nota].acertos + ", do participante: " + participantes[menor_nota].nome);
        System.out.println("Maior nota: " + participantes[maior_nota].acertos + ", do participante: " + participantes[maior_nota].nome);
        System.out.println();

        int qtd_acima_metade = 0;
        for (Participante participante : participantes) {
            if (participante.acertos > QTD_QUESTS / 2) qtd_acima_metade++;
        }
        System.out.printf("Percentual de participantes com mais da metade de acertos: %.2f%%\n", (double) qtd_acima_metade / n_participante * 100);
    }
}
