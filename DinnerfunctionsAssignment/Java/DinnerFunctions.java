public class DinnerFunctions {

public static int getFactorial(int num) {
        int factorial = 1;
        for (int i = 1; i <= num; i++) {
            factorial = factorial * i;
        }
        return factorial;
    }

public static int findGCD(int numOne, int numTwo) {
        int gcd = 1;
        for (int i = 1; i <= Math.min(numOne, numTwo); i++) {
            if (numOne % i == 0 && numTwo % i == 0) {
                gcd = i;
            }
        }
        return gcd;
    }

public static int findLCM(int numOne, int numTwo) {
        int gcd = findGCD(numOne, numTwo);
        int lcm = (numOne * numTwo) / gcd;
        return lcm;
    }

public static boolean isPerfectNumber(int number) {
        int count = 0;
        for (int i = 1; i < number; i++) {
            if (number % i == 0) {
                count = count + i;
            }
        }
        return count == number;
    }

public static boolean isArmstrong(int number) {
        String numStr = Integer.toString(number);
        int length = numStr.length();
        int sum = 0;

        for (int i = 0; i < numStr.length(); i++) {
            int digit = Character.getNumericValue(numStr.charAt(i));
            sum = sum + (int)Math.pow(digit, length);
        }

        return sum == number;
    }
}
    