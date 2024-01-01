package arrayRecoord;

import java.util.Scanner;

public class Nilai {
	int nim;
	String nama;
	float uts;
	float uas;
	double na;
	char index;
	
	void SetIndex() {
		if (na>=85)
			index='A';
		else if (na>=75)
			index='B';
		else if (na>=55)
			index='C';
		else if (na>45)
			index='D';
		else
			index='E';
	}
	
	void BacaNilai() {
		Scanner sc= new Scanner(System.in);
		System.out.print("NIM :"); nim=sc.nextInt();
		System.out.print("Nama :"); nama=sc.next();
		System.out.print("uts :"); uts=sc.nextFloat();
		System.out.print("uas :"); uas=sc.nextFloat();
		na=0.3*uts+0.7*uas;
		SetIndex();

	}
	void TampilNilai() {
		System.out.println("Data :"
				+nim+","+nama+","+uts+","+uas+","+na);
	}
}
