//Manuel Ortiz at 2020
//Data Structure Problem Solving. Extracted from: https://www.hackerrank.com/challenges/sparse-arrays/problem

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;


public class SparseArray {

    // Complete the matchingStrings function below.
    static int[] matchingStrings(String[] strings, String[] queries) {
    	int resultArray[] = new int[queries.length];
 		
    	for (int i = 0; i<queries.length; i++){
    		int match_counter = 0;
    		for (int j = 0; j<strings.length; j++){
    			if (queries[i].matches(strings[j])){
    				match_counter++;
    				resultArray[i] = match_counter;
    			}
    		}
    	}

    	return resultArray;   

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
       
        int stringsCount = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String[] strings = new String[stringsCount];

        for (int i = 0; i < stringsCount; i++) {
            String stringsItem = scanner.nextLine();
            strings[i] = stringsItem;
        }

        int queriesCount = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String[] queries = new String[queriesCount];

        for (int i = 0; i < queriesCount; i++) {
            String queriesItem = scanner.nextLine();
            queries[i] = queriesItem;
        }

        //int[] res = matchingStrings(strings, queries);
        int[] res = matchingStrings(strings, queries);

        for (int i = 0; i < res.length; i++) {
            System.out.println(res[i]);
        }

        scanner.close();
    }
}






