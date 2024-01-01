package ARRAY;

import java.util.Scanner;

public class arrayInt {
	int N=5;
	int[] a = new int[N];
	
	void isiArray() {
		Scanner  sc = new Scanner(System.in);
		
		for (int i=0; i < N; i++) {
			System.out.print("element array ke " + i + ": ");
			a[i] = sc.nextInt();
		}
	}
	
	void tampilArray() {
		
		for (int i=0; i < N; i++) {
			System.out.println("element array ke " + i + ": " + a[i]);
		}
	}
	
	void hitungRataArray() {
		double Total=0; 
		double Rata=0;
		
		for(int i=0; i< N; i++) {
			Total = Total + a[i];
		}
		Rata = Total/N;
		System.out.println("Rata rata array: "+ Rata);
	}
	
	void nilaiMaksArray() {
		int maks = a[0];
		
		for(int i=1; i< N; i++) {
			if(maks < a[i]) {
				maks = a[i];
			}
		}
		
		System.out.println("Nilai maksimal array: "+ maks);
		
	}
	
	public static void main(String[] args) {
		arrayInt A = new arrayInt();
		
		A.isiArray();
		A.tampilArray();
		A.hitungRataArray();
		A.nilaiMaksArray();
	}
}