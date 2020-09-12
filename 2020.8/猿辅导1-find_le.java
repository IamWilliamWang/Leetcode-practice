import java.util.Scanner;

public class Main {
    private static int search(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (numbers[mid] > target)
                right = mid - 1;
            else
                left = mid + 1;
        }
        return right;
    }

    public static void main(String[] args) {
        int[] array = new int[] {1, 2, 4, 6, 7};
        System.out.println(search(array, 4));
    }
}