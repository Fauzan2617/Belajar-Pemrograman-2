package arrayRecoord;

import java.util.Scanner;

import ARRAY.ArrayChar;

public class ArrMahasiswa {
	int N=2;
	Mahasiswa[] a=new Mahasiswa[N];
	
	void IsiLarik() {
		Mahasiswa x;
		Scanner sc= new Scanner(System.in);
		for (int i=0 ; i<N;i++) {
			 x=new Mahasiswa();
			System.out.println("elemen ke :"+i+":");
			x.BacaMahasiswa();
			a[i]=x;
		}
	}
	void ShowArray() {
		for (int i=0;i<N;i++) {
			System.out.println("Elemen ke :"+i+":");
		a[i].TampilMahasiswa();
		}
	}
	
	public static void main (String[] args) {
		ArrMahasiswa A= new ArrMahasiswa();
		A.IsiLarik();A.ShowArray();
		}
}

