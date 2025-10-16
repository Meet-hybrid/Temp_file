public class SumOfEvenNumbers {
    
    public static void main(String[] args) {
        int sum = 0;
        for (int number = 1; number <= 100; number++) {
          
            if (number % 2 == 0) {
		sum = sum + number;
          	 
            }
        }
         System.out.println(sum);
   }	
}