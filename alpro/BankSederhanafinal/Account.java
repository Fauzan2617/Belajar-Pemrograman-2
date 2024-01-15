public class Account {
    private double saldo;
    private String password;

    public Account(double saldo, String password) {
        this.saldo = saldo;
        this.password = password;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public boolean checkPassword(String enteredPassword) {
        return this.password.equals(enteredPassword);
    }

    public void changePassword(String newPassword) {
        this.password = newPassword;
        System.out.println("Password berhasil diubah.");
    }
}
