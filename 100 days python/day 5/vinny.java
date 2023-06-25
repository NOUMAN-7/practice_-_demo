import java.util.*;
import java.io.*;
import java.lang.Math;

public class vinny
{
  public static int magicArray(int N,int[] A)
  {

    //this is default OUTPUT. You can change it.
    int result = 0;

    //write your Logic here:
    
  public static void main (String[]args)
  {
    Scanner sc = new Scanner (System.in);

    //INPUT [uncomment & modify if required]
    int N = sc.nextInt ();

    int[] A = new int[N];
    for (int i = 0; i < N; i++)
    {
        A[i] = sc.nextInt ();
    }
    
    sc.close ();

    //OUTPUT [uncomment & modify if required]
    System.out.print(magicArray(N,A));
  }
}
}
