package arrayRecoord;

import java.util.Scanner;

public class Mahasiswa {
	int nim;
	String nama;
	float ipk;
	
	void BacaMahasiswa() {
		Scanner sc=new Scanner(System.in);
		System.out.println("nim: "); nim=sc.nextInt();
		System.out.println("nama: "); nama=sc.next();
		System.out.println("ipk: "); ipk=sc.nextFloat();
	}
	
	void TampilMahasiswa() {
		System.out.println("Data: "
				+nim+","+nama+","+ipk);
	}
}
