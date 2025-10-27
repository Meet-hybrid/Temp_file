import java.util.Scanner;
import java.util.Random;

public class SimpleArithmeticApp {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Random rand = new Random();

        int correctAnswers = 0;

        System.out.println("Welcome to Simple Arithmetic App");

        for (int i = 1; i <= 10; i++) {
		int num1 = rand.nextInt(50) + 1;             
		int num2 = rand.nextInt(num1) + 1; 
            int correct = num1 - num2;

            System.out.println(i + num1 + " - " + num2 + "=");
            System.out.print("Enter your answer: ");
            int userInput = input.nextInt();

            if (userInput == correct) {
		//correctAnswers += correct;
                //correctAnswers++;
            System.out.println(" Correct!");
            } else {
                System.out.println(" Incorrect! try next time");
            }
        }

        System.out.println("Na " + correctAnswers + " out of 10 you get.");
    }
}
