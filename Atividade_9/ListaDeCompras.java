// O erro estava no método removerItem ao tentar remover um item que não
// foi adicionado antes. Para corrigir, bastou fazer uma verificação dos itens.
// Se o item já foi adicionado, ele é excluído normalmente, senão um aviso é exibido.

import java.util.ArrayList;

public class ListaDeCompras {
    public static void main(String[] args) {
        ListaDeCompras lista = new ListaDeCompras();
        lista.adicionarItem("Maçã");
        lista.adicionarItem("Banana");
        lista.adicionarItem("Pêra");
        lista.removerItem("Banana");
        lista.removerItem("Laranja");
        lista.exibirLista();
    }

    private ArrayList<String> itens;

    public ListaDeCompras() {
        this.itens = new ArrayList<>();
    }

    public void adicionarItem(String item) {
        itens.add(item);
    }

    public void removerItem(String item) {
        if(itens.contains(item)){
            itens.remove(item);
        } else {
            System.out.println("Item " + item + " não encontrado para remoção.");
        }
         
    }

    public void exibirLista() {
        System.out.println("Lista de Compras:");
        for (String item : itens) {
            System.out.println("- " + item);
        }
    }
}