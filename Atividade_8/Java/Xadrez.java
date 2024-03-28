public class Xadrez {

    public class Peca {

        private String id;
        private String cor;

        public void setCor(String cor) {
            this.cor = cor;
        }

        public void setId(String id) {
            this.id = id;
        }

        public String getId() {
            return id;
        }

        public String getCor() {
            return cor;
        }

    }

    Peca[][] tabuleiro;

    public Xadrez(Peca[][] tabuleiro) {
        this.tabuleiro = tabuleiro;
    }

    public Xadrez() {
        this(new Peca[][] {});
    }

    public void moverPeca() {

    }

    public void capturarPeca(Peca inimigo, int linha, int coluna) {

    }

    public boolean podeMoverPara(Peca peca, int posicao) {
        return false;
    }

    public Peca getPeca(int linha, int coluna) {
        return null;
    }

}