package baekjoon.barkingdog.chap09;

import java.util.LinkedList;
import java.util.Queue;

public class Prac01 {
    public static void main(String[] args) {
        int[][] board = new int[][] {
                {1,1,1,0,1,0,0,0,0,0},
                {1,0,0,0,1,0,0,0,0,0},
                {1,1,1,0,1,0,0,0,0,0},
                {1,1,0,0,1,0,0,0,0,0},
                {0,1,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0}};

        int[][] visited = new int[502][502];
        int n = 7, m = 10;
        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, 1, 0, -1};

        Queue<int[]> queue = new LinkedList<>();
        visited[0][0] = 1;
        queue.add(new int[]{0, 0});
        while(!queue.isEmpty()) {
            int[] cur = queue.poll();
            System.out.print("(" + cur[0] + ", " + cur[1] + ") -> ");
            for(int dir = 0; dir < 4; dir++) {
                int nx = cur[0] + dx[dir];
                int ny = cur[1] + dy[dir];

                if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                if(visited[nx][ny] == 1 || board[nx][ny] != 1) continue;

                visited[nx][ny] = 1;
                queue.add(new int[]{nx, ny});
            }
        }
    }
}
