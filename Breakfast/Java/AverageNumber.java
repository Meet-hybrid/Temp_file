public class AverageNumber {
   public static void main(String[] args) {
	int sum = 0;
	int average = 0;
   	
        for(int i = 1; i <= 100; i++) {
	sum = sum + i;
	average = sum / i;
	}
	System.out.print(average);
    }
}
	
