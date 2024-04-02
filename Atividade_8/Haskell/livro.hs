data Livro = Livro { 
    titulo :: String,
    autor :: String,
    anoPublicacao :: Int,
    copiasDisponiveis :: Int
} deriving (Show) -- deriving aqui cria automaticamente instâncias do tipo entre parênteses, não preciso criá-las manualmente

emprestarLivro :: Livro -> Livro

devolverLivro :: Livro -> Livro

verificarDisponibilidade :: Livro -> Bool

informacoesLivro :: Livro -> (String, String, Int)

