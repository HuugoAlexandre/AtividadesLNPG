typedef struct {
    int id;
    char[255] nome;
    char[255] localizacao;
    Empregado[255] empregados;
} Departamento;

void inicializarDepartamento(
    Departamento *departamento, 
    int id, 
    char[255] nome, 
    char[255] localizacao,
    Empregado[255] empregados;
) {}

int pegarIdDepartamento(Departamento *departamento) {}
char pegarNomeDepartamento(Departamento *departamento) {}
char pegarLocalizacaoDepartamento(Departamento *departamento) {}
Empregado *pegarEmpregadosDepartamento(Departamento *departamento) {}
void adicionarEmpregado(Departamento *departamento, Empregado *empregado) {}
void removerEmpregado(Departamento *departamento, Empregado *empregado) {}

typedef struct {
    int id;
    char[255] nome;
    char[255] cargo;
    float salario;
    Departamento *departamento;
} Empregado;

void inicializarDepartamento(
    Departamento *departamento, 
    int id, 
    char[255] nome, 
    char[255] localizacao,
    Empregado[255] empregados;
) {}

void inicializarEmpregado(
    Empregado *empregado,
    int id,
    char[255] nome,
    char[255] cargo,
    float salario,
    Departamento *departamento
) {}

int pegarIdEmpregado(Empregado *empregado) {}
char pegarNomeEmpregado(Empregado *empregado) {}
char pegarCargoEmpregado(Empregado *empregado) {}
float pegarSalarioEmpregado(Empregado *empregado) {}
Departamento *pegarDepartamentoEmpregado(Empregado *empregado) {}
void atualizarNomeEmpregado(Empregado *empregado, char[255] nome) {}
void atualizarCargoEmpregado(Empregado *empregado, char[255] cargo) {}
void atualizarSalarioEmpregado(Empregado *empregado, float salario) {}
void atualizarDepartamento(Empregado *empregado, Departamento *departamento) {}