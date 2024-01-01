package matriks;

import java.util.Scanner;

public class matrikint {
	int N=2; int M=3;
	int[][] a=new int[N][M];
	
	void isimatrik() {
		Scanner sc = new Scanner(System.in);
		for (int i=0; i<N ; i++) {
			for (int j=0; j<M; j++) {
			System.out.print("el matrik ke "+i+","+j+":");
			a[i][j]=sc.nextInt();
			}
		}
	}
	
	void tampilmatrik() {
	
		for (int i=0; i<N ; i++) {
			for (int j=0; j<M; j++) {
			System.out.print("matrik ke "+i+","+j+":"+ a[i][j]);
			}
			System.out.println();
		}
	}
	
	
	
	int GetElemen (int i, int j) {
		return a[i][j];
	}
	
	void SetElemen (int i, int j, int x) {
		a[i][j]=x;
	}
	
	static void salinmatrika_b(matrikint A, matrikint B) { 
		int x;
		for (int i=0; i<A.N; i++){
			for (int j=0; j<A.M; j++) {
		x=A.GetElemen(i, j);
		B.SetElemen(i, j,x);
			}
		}
		B.tampilmatrik();
	}
	
	
	static boolean issamaa_b(matrikint A, matrikint B) { 
		boolean sama=true;
		int i=0; int j;
		while ((i<A.N) && (sama==true)){
			j=0;
			while ((i<A.M) && (sama==true)) {
			if (A.GetElemen(i, j) == B.GetElemen(i, j))
				j=j+1;
			else sama=false;
			}
			i=i+1;
		}
		return sama;
	}
	
	
	public static void main(String[] args) {
		matrikint A=new matrikint();
		matrikint B=new matrikint(); //prosedur sama nilai yg berbeda, klo tipe sama bisa disalin
		
		A.isimatrik();
		A.tampilmatrik();
		
		//B.isimatrik();
		//B.tampilmatrik();
		
		
		//salinmatrika_b(A,B);
		
		
	}
}

