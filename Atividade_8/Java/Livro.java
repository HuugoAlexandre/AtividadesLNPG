public class Livro{

    private String titulo;
    private String autor;
    private int ano;
    private int numCopias;

    public int emprestaLivro(){
        return 0;
    }
    public int devolveLivro(){
        return 0;
    }
    public boolean verificaCopias(){
        return false;
    }

    public int getAno() {
        return ano;
    }

    public int getNumCopias() {
        return numCopias;
    }

    public String getAutor() {
        return autor;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }
    
    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public void setNumCopias(int numCopias) {
        this.numCopias = numCopias;
    }
} 