//Manuel Ortiz Hernández at 2020
//Data Structure Problem Solving. Extracted from: https://www.hackerrank.com/challenges/crush/problem
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class ArrayManipulation {


    static long arrayManipulation(int n, int[][] queries) {
        long hello = 132456;
        long zeroArray[] = new long[n];
        int i = 0;

        zeroArray = arrayManipulationRec(i, zeroArray, queries);
        
        System.out.println(Arrays.toString(zeroArray));

        return hello;
    }

    static long[] arrayManipulationRec(int i, long[] zeroArray, int[][] queries){
        int init = queries[i][0];
        int limit = queries[i][1]-1;
        long toAdd = queries[i][2];
        if (i > queries.length)
            return zeroArray;
        else{

            if (limit >= init) {
                zeroArray[limit] += toAdd;
                limit--;
                long toAdd = queries[i+1][2];
            }else{
                i++;

            }

            arrayManipulationRec(i, zeroArray, queries);
        }

        return zeroArray;
    }


    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
    
        String[] nm = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nm[0]);

        int m = Integer.parseInt(nm[1]);

        int[][] queries = new int[m][3];

        for (int i = 0; i < m; i++) {
            String[] queriesRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 3; j++) {
                int queriesItem = Integer.parseInt(queriesRowItems[j]);
                queries[i][j] = queriesItem;
            }
        }


        long result = arrayManipulation(n, queries);

        System.out.println(result);

        scanner.close();
    }
}
