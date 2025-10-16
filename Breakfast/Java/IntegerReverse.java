public class IntegerReverse {
    public static void main(String[] args) {
        int number = 12345678;
        int reverse = 0;
        
     
        for (int i = 0; number > 0; number /= 10) {
            int digit = number % 10;
            reverse = reverse * 10 + digit;
        }
        
        System.out.println(reverse);
    }
}