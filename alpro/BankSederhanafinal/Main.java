import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Masukkan jumlah akun: ");
        int numberOfAccounts = input.nextInt();

        ATM.initializeAccounts(numberOfAccounts);
        ATM.mainMenu();
    }
}
