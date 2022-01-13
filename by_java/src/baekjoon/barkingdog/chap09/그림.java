package baekjoon.barkingdog.chap09;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 그림 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int x = scanner.nextInt();
        int y = scanner.nextInt();

        int[][] paint = new int[x][y];

        for(int i=0; i<x; i++) {
            for(int j=0; j<y; j++) {
                paint[i][j] = scanner.nextInt();
            }
        }

        int count = 0, max = 0;
        int size;
        int[][] visited = new int[x][y];
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        Queue<int[]> Q = new LinkedList<>();
        for(int i=0; i<x; i++) {
            for(int j=0; j<y; j++) {
                if(paint[i][j] == 1 && visited[i][j] != 1) {
                    visited[i][j] = 1;
                    Q.add(new int[]{i, j});
                    count++;
                    size = 1;
                } else continue;
                while (!Q.isEmpty()) {
                    int[] cur = Q.poll();
                    for(int dir=0; dir<dx.length; dir++) {
                        int nx = cur[0] + dx[dir];
                        int ny = cur[1] + dy[dir];

                        if(nx < 0 || nx >= x || ny < 0 || ny >= y) continue;
                        if(paint[nx][ny] != 1 || visited[nx][ny] == 1) continue;

                        visited[nx][ny] = 1;
                        Q.add(new int[]{nx, ny});
                        size++;
                    }
                }
                max = Math.max(max, size);
            }
        }
        System.out.println(count + " " + max);
    }
}
