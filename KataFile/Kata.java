public class Kata {

    public static boolean isEven(int number) {
        return number % 2 == 0;
    }

    public static boolean isPrimeNumber(int number) {
        int counter = 0;
        for (int count = 1; count <= number; count++) {
            if (number % count == 0) {
                counter++;
            }
        }
        return counter == 2;
    }

    public static int subtract(int number1, int number2) {
        return Math.abs(number1 - number2);
    }

    public static float divideNumber(float number1, float number2) {
        if (number2 == 0) {
            throw new ArithmeticException("Cannot divide by zero");
        }
        return number1 / number2;
    }

    public static int factorsOfNumber(int number) {
        int counter = 0;
        for (int count = 1; count <= number; count++) {
            if (number % count == 0) {
                counter++;
            }
        }
        return counter;
    }

    public static boolean isSquare(int number) {
        for (int i = 1; i * i <= number; i++) {
            if (i * i == number) {
                return true;
            }
        }
        return false;
    }

    public static boolean isPalindrome(int number) {
        int reversed = 0;
        int temp = number;

        while (number > 0) {
            int digit = number % 10;
            reversed = (reversed * 10) + digit;
            number = number / 10;
        }

        return temp == reversed;
    }

    public static long factorialOfNumber(long number) {
        long factorial = 1;
        for (int count = 1; count <= number; count++) {
            factorial *= count;
        }
        return factorial;
    }

    public static long squareOf(int number) {
        return (long) number * number;
    }

   
}