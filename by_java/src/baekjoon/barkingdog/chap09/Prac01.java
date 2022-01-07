package baekjoon.barkingdog.chap09;

import java.util.ArrayDeque;
import java.util.Queue;

class Pair {
    Integer x;
    Integer y;
    public Pair(Integer x, Integer y) {
        this.x = x;
        this.y = y;
    }
    public Integer first() {
        return x;
    }
    public Integer second() {
        return y;
    }
}

public class Prac01 {
    public static void main(String[] args) {
        int[][] board = new int[][]
                {{1,1,1,0,1,0,0,0,0,0},
                {1,0,0,0,1,0,0,0,0,0},
                {1,1,1,0,1,0,0,0,0,0},
                {1,1,0,0,1,0,0,0,0,0},
                {0,1,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0,0,0} };
        int[][] vis = new int[502][502];
        int n = 7, m = 10;
        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, 1, 0, -1};

        Queue<Pair> queue = new ArrayDeque<>();
        vis[0][0] = 1;
        queue.add(new Pair(0, 0));
        while(!queue.isEmpty()) {
            Pair cur = queue.poll();
            System.out.print("(" + cur.first() + ", " + cur.second() + " -> ");
            for(int dir =0; dir < 4; dir++) {
                int nx = cur.first() + dx[dir];
                int ny = cur.second() + dy[dir];
                if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                if(vis[nx][ny] == 1 || board[nx][ny] != 1) continue;
                vis[nx][ny] = 1;
                queue.add(new Pair(nx, ny));
            }
        }
    }
}
