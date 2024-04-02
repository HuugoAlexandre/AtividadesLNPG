data Empregado = Empregado {
    nome :: String,
    id :: Int,
    cargo :: String,
    salario :: Float,
    departamento :: Departamento
} deriving (Show)

data Departamento = Departamento {
    nomeDep :: String,
    idDep :: Int,
    localizacao :: String,
    empregados :: [Empregado]
} deriving (Show)


atualizarInformacoes :: Empregado -> String -> String -> Float -> Empregado

transferirDepartamento :: Empregado -> Departamento -> Empregado

informacoesDepartamento :: Empregado -> Departamento

adicionarEmpregado :: Empregado -> Departamento -> Departamento

removerEmpregado :: Int -> Departamento -> Departamento

informacoesEmpregados :: Departamento -> [Empregado]
