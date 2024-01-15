import java.util.Scanner;

public class ATM {
    private static Account[] accountArray;

    public static void initializeAccounts(int numberOfAccounts) {
        accountArray = new Account[numberOfAccounts];
        Scanner input = new Scanner(System.in);

        for (int i = 0; i < numberOfAccounts; i++) {
            System.out.print("Masukkan password untuk Akun " + i + ": ");
            String password = input.next();
            accountArray[i] = new Account(0, password);
        }
    }

    public static void mainMenu() {
        Scanner input = new Scanner(System.in);
        boolean isRunning = true;

        while (isRunning) {
            System.out.println("SELAMAT DATANG DI BANK SEDERHANA");
            System.out.print("Masukkan nomor akun: ");
            int accountNumber = input.nextInt();
            System.out.print("Masukkan password: ");
            String enteredPassword = input.next();

            if (accountNumber >= 0 && accountNumber < accountArray.length) {
                if (accountArray[accountNumber].checkPassword(enteredPassword)) {
                    transactionMenu(accountNumber);
                } else {
                    System.out.println("Password salah. Coba lagi.");
                }
            } else {
                System.out.println("Nomor akun tidak valid.");
            }
        }
    }

    private static void transactionMenu(int accountNumber) {
        Scanner input = new Scanner(System.in);
        boolean isTransactionRunning = true;

        while (isTransactionRunning) {
            System.out.println("1. Memasukkan Uang");
            System.out.println("2. Mengambil Uang");
            System.out.println("3. Check Saldo");
            System.out.println("4. Change Password");
            System.out.println("5. Cancel");
            System.out.print("SILAHKAN PILIH NO 1/2/3/4/5 :");
            String choice = input.next();

            switch (choice) {
                case "1":
                    deposit(accountNumber);
                    break;
                case "2":
                    withdraw(accountNumber);
                    break;
                case "3":
                    checkBalance(accountNumber);
                    break;
                case "4":
                    changePassword(accountNumber);
                    break;
                case "5":
                    isTransactionRunning = false;
                    System.out.println("Terima kasih atas penggunaan layanan ATM !!");
                    break;
                default:
                    System.out.println("Pilihan tidak valid. Silakan coba lagi.");
                    break;
            }
        }
    }

    private static void deposit(int accountNumber) {
        Scanner input = new Scanner(System.in);
        System.out.print("Masukkan jumlah uang yang ingin Anda simpan: ");
        double amount = input.nextDouble();

        if (amount > 0) {
            double previousBalance = accountArray[accountNumber].getSaldo();
            accountArray[accountNumber].setSaldo(previousBalance + amount);
            System.out.println("Anda telah menyimpan " + amount + " ke Akun " + accountNumber + ".");
        } else {
            System.out.println("Jumlah yang dimasukkan tidak valid. Harap masukkan jumlah uang yang valid.");
        }
    }

    private static void withdraw(int accountNumber) {
        Scanner input = new Scanner(System.in);
        System.out.print("Masukkan jumlah uang yang ingin Anda ambil: ");
        double amount = input.nextDouble();
        double previousBalance = accountArray[accountNumber].getSaldo();

        if (amount > 0 && previousBalance >= amount) {
            accountArray[accountNumber].setSaldo(previousBalance - amount);
            System.out.println("Anda telah mengambil " + amount + " dari Akun " + accountNumber + ".");
        } else {
            System.out.println("Jumlah yang dimasukkan tidak valid atau saldo tidak mencukupi.");
        }
    }

    private static void checkBalance(int accountNumber) {
        System.out.println("Saldo Akun " + accountNumber + " saat ini: " + accountArray[accountNumber].getSaldo());
    }

    private static void changePassword(int accountNumber) {
        Scanner input = new Scanner(System.in);
        System.out.print("Masukkan password baru: ");
        String newPassword = input.next();

        accountArray[accountNumber].changePassword(newPassword);
    }
}
