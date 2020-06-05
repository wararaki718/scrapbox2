public class Procedural {
    private void printNMultiTable(int n) {
        for (int i = 1; i <= 9; i++) {
            if(i != 9) {
                System.out.print(i * n + " ");
            } else {
                System.out.print(i * n);
            }
        }
        System.out.println();
    }

    public Procedural() {
        this.printNMultiTable(3);
    }
    
    public static void main(String args[]) {
        new Procedural();
    }
}