public class Count {
   public static void main(String[] args) {
	int count = 0;		
	for (int number = 1; number <= 100; number++) {
          
            if (9 % number == 0) {
		count++;
           	 
            }
        }
      System.out.print(count);  
   }	
}