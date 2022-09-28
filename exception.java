package trabalho;

public class exceptions {

    public static void main(String args[]) {

        int[] list = {1, 2, 3, 4, 5};
        try {
            for (int c = 0; c < 6; c++){
                System.out.println(list[c]);
            }
        } catch (ArrayIndexOutOfBoundsException e){
            System.out.println("\nO index da lista que o sistem está tentando acessar não existe");
        }

    }
