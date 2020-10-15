public class Main {
    public static boolean contains(String longStr, String shortStr) {
        if(shortStr == null || longStr == null)
            throw new ArgumentException();
        if(shortStr.length() == 0)
            return longStr.length() == 0;
        if(shortStr.legnth() > longStr.length())
            return false;
        int i = 0, j = 0;
        while(j < shortStr.length()) { // 找到了，就结束循环
            while(i < longStr.length() && longStr.charAt(i) != shortStr.charAt(j)) // 找longStr中shortStr[i]的位置
                i++;
            if(i == longStr.length()) // 找不到，就结束循环
                break;
            i++; // i和j一样，都自增一继续找
            j++;
        }
        return j == shortStr.length(); // 如果找到了，j就是shortStr.length()
    }
    
    public static void main(String[] args) {
        System.out.println(contains("abcd", "cd"));
    }
}