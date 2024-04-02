data Peca = Peca {
    tipo :: TipoPeca,
    cor :: CorPeca,
    posicao :: (Int, Int)
} deriving (Show)

data TipoPeca = Rei | Rainha | Torre | Bispo | Cavalo | Peao deriving (Show)

data CorPeca = Branco | Preto deriving (Show)

data Tabuleiro = Tabuleiro {
    pecas :: [Peca] -- Lista de peças no tabuleiro
} deriving (Show)

moverPeca :: Peca -> (Int, Int) -> Peca

capturarPeca :: Peca -> Peca -> Maybe Peca

verificarMovimentoPossivel :: Peca -> (Int, Int) -> Bool

informacoesPeca :: Peca -> (TipoPeca, CorPeca, (Int, Int))

inicializarTabuleiro :: Tabuleiro

adicionarPeca :: Tabuleiro -> Peca -> Tabuleiro

removerPeca :: Tabuleiro -> Peca -> Tabuleiro

posicaoVazia :: Tabuleiro -> (Int, Int) -> Bool

obterPeca :: Tabuleiro -> (Int, Int) -> Maybe Peca

obterPecasPorCor :: Tabuleiro -> CorPeca -> [Peca]
