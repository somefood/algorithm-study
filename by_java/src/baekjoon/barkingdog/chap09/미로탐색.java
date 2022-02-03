package baekjoon.barkingdog.chap09;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 미로탐색 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = scanner.nextInt();
        int[][] board = new int[N][M];
        int[][] visited = new int[N][M];

        for(int i=0; i<N; i++) {
            String s = scanner.next();
            for(int j=0; j<s.length(); j++) {
                board[i][j] = s.charAt(j) - '0';
            }
        }

        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        Queue<int[]> Q = new LinkedList<>();
        visited[0][0] = 1;
        Q.add(new int[]{0, 0});

        while(!Q.isEmpty()) {
            int[] cur = Q.poll();
            for(int i=0; i<4; i++) {
                int nx = cur[0] + dx[i];
                int ny = cur[1] + dy[i];

                if(nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
                if(board[nx][ny] == 0 || visited[nx][ny] != 0) continue;

                visited[nx][ny] = visited[cur[0]][cur[1]] + 1;
                Q.add(new int[]{nx, ny});
            }
        }

        System.out.println(visited[N-1][M-1]);
    }
}
