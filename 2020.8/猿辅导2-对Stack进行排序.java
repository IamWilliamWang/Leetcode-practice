// 猿辅导2：对Stack进行排序（只能使用辅助栈），空间复杂度O(1)

import java.util.Scanner;
import java.util.Stack;

public class Main {
    private static Stack<Integer> sorted(Stack<Integer> stack) {
        int size = stack.size();
        Stack<Integer> result = new Stack<>();
        Stack<Integer> tmp = new Stack<>();
        while (result.size() != size) {
            int min = 1000000;
            while (stack.size() != 0) {
                int element = stack.pop();
                min = Math.min(element, min);
                tmp.push(element);
            }
            while (tmp.size() != 0) {
                int element = tmp.pop();
                if (element == min)
                    result.push(element);
                else
                    stack.push(element);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        stack.push(1);
        stack.push(8);
        stack.push(0);
        stack.push(5);
        stack.push(1);
        System.out.println(sorted(stack));
    }
}