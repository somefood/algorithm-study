package baekjoon;

import java.io.*;
import java.util.StringTokenizer;

public class 빠른AB {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int a, b;

        for(int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());

            bw.write(a + b + "\n");
        }
        bw.flush();
        bw.close();
        br.close();
    }
}
