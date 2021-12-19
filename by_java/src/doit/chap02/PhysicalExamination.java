package doit.chap02;

import java.util.Scanner;

public class PhysicalExamination {
    static final int VMAX = 21;

    static class PhyscData {
        String name;
        int height;
        double vision;

        PhyscData(String name, int height, double vision) {
            this.name = name;
            this.height = height;
            this.vision = vision;
        }
    }

    static double aveHeight(PhyscData[] data) {
        double sum = 0;

        for (int i = 0; i < data.length; i++) {
            sum += data[i].height;
        }
        return sum / data.length;
    }

    static void distVision(PhyscData[] data, int[] dist) {
        int i = 0;
        dist[i] = 0;
        for (i = 0; i < data.length; i++)
            if (data[i].vision >= 0.0 && data[i].vision <= VMAX / 10.0)
        dist[(int) (data[i].vision * 10)]++;
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        PhyscData[] x = {
            new PhyscData("Park", 162, 0.3),
            new PhyscData("Kim", 173, 0.7),
            new PhyscData("Hong", 175, 2.0),
            new PhyscData("Choi", 168, 1.5),
            new PhyscData("Cho", 174, 0.4),
            new PhyscData("Ki", 174, 1.2),
            new PhyscData("Lee", 169, 0.8),
        };
        int[] vdist = new int[VMAX];
        System.out.println("신체 검사 리스트");
        System.out.println("이름        키    시력");
        for(int i=0; i< x.length; i++) {
            System.out.printf("%-8s%3d%5.1f\n", x[i].name, x[i].height, x[i].vision);
        }
        System.out.printf("\n평균 키 : %5.1fcm\n", aveHeight(x));

        distVision(x, vdist);

        System.out.println("\n시력 분포");
        for (int i=0; i<VMAX; i++)
            System.out.printf("%3.1f~:%2d명\n", i / 10.0, vdist[i]);
    }
}
