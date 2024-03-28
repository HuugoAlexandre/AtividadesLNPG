typedef struct {
    char[255] tipo;
    char[255] cor;
} Peca;

typedef struct {
    Peca[8][8] tabuleiro;
} Xadrez;

void inicializarXadrez(Xadrez *xadrez, Peca[8][8] tabuleiro) {}
void inicializarPeca(Peca *peca, char[255] tipo, char[255] cor) {}

void moverPeca(Xadrez *xadrez, Peca *peca, int linha, int coluna) {}
void capturarPeca(Xadrez *xadrez, Peca *atual, Peca *inimiga) {}
int podeMover(Xadrez *xadrez, Peca *peca, int linha, int coluna) {}
char *cor(Peca *peca) {}
char *tipo(Peca *peca) {}