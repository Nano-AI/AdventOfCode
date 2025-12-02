import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Main {
    public static Scanner getInput() {
        Scanner s;
        try {
            s = new Scanner(new File("./input.txt"));
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
            return null;
        }
        return s;
    }

    public static int part1() {
        Scanner s = getInput();

        int direction = 50;
        int count = 0;

        while (s.hasNext()) {
            String line = s.nextLine();
            char dir = line.charAt(0);
            int turns = Integer.parseInt(line.substring(1));
            if (dir == 'L') {
                turns *= -1;
            }
            direction += turns;
            direction = direction % 100;
            if (direction == 0) {
                count++;
            }
        }

        return count;
    }

    public static int parity(int val) {
        if (val < 0) return -1;
        if (val > 0) return 1;
        return 0;
    }

    public static int part2() {
        Scanner s = getInput();
        int dial = 50;
        int count = 0;
        while (s.hasNext()) {
            String line = s.nextLine();
            int dir = (line.charAt(0) == 'L') ? -1 : 1;
            int turns = Integer.parseInt(line.substring(1));
            int next_val = dial + turns * dir;
            int leftover = 0;
            if (dir > 0) {
                leftover = (100 - dial) % 100;
                dial = Math.floorMod(dial + turns, 100);
            } else {
                leftover = dial % 100;
                dial = Math.floorMod(dial - turns, 100);
            }
            if (leftover == 0) {
                leftover = 100;
            }
            if (turns >= leftover) {
                count += 1 + (turns - leftover) / 100;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.printf("Part 1: %d\n", part1());
        System.out.printf("Part 2: %d\n", part2());
    }
}

