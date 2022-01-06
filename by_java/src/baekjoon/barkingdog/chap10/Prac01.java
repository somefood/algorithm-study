package baekjoon.barkingdog.chap10;

import java.util.Arrays;
import java.util.Stack;

public class Prac01 {
    public static void main(String[] args) {
        int[][] board = {
                {1,1,1,0,1,0,0,0,0,0},
                {1,0,1,0,1,0,0,0,0,0},
                {1,1,1,0,1,0,0,0,0,0},
                {1,1,0,0,1,0,0,0,0,0},
                {0,1,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0}};
        int[][] vis = new int[502][502];
        int n = 7, m = 10;
        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, 1, 0, -1};

        Stack<int[]> stack = new Stack<>();
        vis[0][0] = 1;
        stack.push(new int[] {0, 0});
        while(!stack.isEmpty()) {
            int[] cur = stack.pop();
            System.out.print("(" + cur[0] + ", " + cur[1] + ") -> ");
            for(int dir=0; dir<4; dir++) {
                int nx = cur[0] + dx[dir];
                int ny = cur[1] + dy[dir];
                if(nx < 0 || nx >=n || ny < 0 || ny >= m) continue;
                if(vis[nx][ny] == 1 || board[nx][ny] != 1) continue;

                vis[nx][ny] = 1;
                stack.push(new int[] {nx, ny});
            }
        }
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                System.out.print(vis[i][j] + " ");
            }
            System.out.println();
        }
    }
}
