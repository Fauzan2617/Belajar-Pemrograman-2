package arrayRecoord;

import java.util.Scanner;

import ARRAY.ArrayChar;

public class TabMhs {
	int N=2;
	Mahasiswa[] a=new Mahasiswa[N];
	
	void IsiLarik() {
		Mahasiswa x;
		Scanner sc= new Scanner(System.in);
		for (int i=0 ; i<N;i++) {
			 x=new Mahasiswa();
			System.out.println("elemen ke :"+i+":");
			System.out.print("NIM :"); x.nim=sc.nextInt();
			System.out.print("Nama :"); x.nama=sc.next();
			System.out.print("Ipk :"); x.ipk=sc.nextFloat();
			a[i]=x;
		}
	}
	void ShowArray() {
		for (int i=0;i<N;i++) {
			System.out.println("Elemen ke :"+i+":"
		+a[i].nim+","+a[i].nama+","+a[i].ipk);
		}
	}
	
	public static void main (String[] args) {
		TabMhs A= new TabMhs();
		A.IsiLarik();A.ShowArray();
		}
}
