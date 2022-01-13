package baekjoon.barkingdog.chap09;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 미로탐색 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int x = scanner.nextInt();
        int y = scanner.nextInt();

        int[][] map = new int[x][y];

        for(int i=0; i<x; i++){
            String[] split = scanner.next().split("");
            for(int j=0; j<split.length; j++) {
                map[i][j] = Integer.parseInt(split[j]);
            }
        }

        int[][] visited = new int[x][y];
        visited[0][0] = 1;
        Queue<int[]> Q = new LinkedList<>();
        Q.add(new int[]{0, 0});

        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        while(!Q.isEmpty()) {
            int[] cur = Q.poll();

            for(int dir=0; dir<4; dir++) {
                int nx = cur[0] + dx[dir];
                int ny = cur[1] + dy[dir];

                if(nx < 0 || nx >= x || ny < 0 || ny >= y) continue;
                if(map[nx][ny] != 1 || visited[nx][ny] >= 1 ) continue;

                visited[nx][ny] = visited[cur[0]][cur[1]] + 1;
                Q.add(new int[]{nx, ny});
            }
        }
        System.out.println(visited[x-1][y-1]);
    }
}
