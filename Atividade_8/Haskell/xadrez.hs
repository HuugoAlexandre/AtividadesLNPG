data Peca = Peca {
    tipo :: TipoPeca,
    cor :: CorPeca,
} deriving (Show)

data TipoPeca = Rei | Rainha | Torre | Bispo | Cavalo | Peao deriving (Show)

data CorPeca = Branco | Preto deriving (Show)

type Posicao = (Int, Int)

type Tabuleiro = [[Maybe Peca]]

moverPeca :: Tabuleiro -> Posicao -> Posicao -> Maybe Tabuleiro 

ehCapturavel :: Peca -> Peca -> Bool

verificarMovimentoPossivel :: Peca -> Posicao -> Bool

verificarLimiteTabuleiro :: Posicao -> Bool

informacoesPeca :: Peca -> (TipoPeca, CorPeca)

inicializarTabuleiro :: Tabuleiro

posicaoVazia :: Tabuleiro -> Posicao -> Bool

obterPeca :: Tabuleiro -> Posicao -> Maybe Peca

obterPecasPorCor :: Tabuleiro -> CorPeca -> [Peca]
