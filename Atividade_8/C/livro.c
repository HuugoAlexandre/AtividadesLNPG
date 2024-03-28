typedef struct {
    char[255] autor;
    char[255] titulo;
    int ano;
    int copias;
} Livro;

Livro inicializar(Livro *livro, char[255] autor, char[255] titulo, int ano, int copias) {}
void emprestar(Livro *livro) {}
void devolver(Livro *livro) {}
int temCopia(Livro *livro) {}