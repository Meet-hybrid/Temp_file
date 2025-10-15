public class Count {
    
    public static void main(String[] args) {
        
	int count = 0;
        for (int i = 1; i <= 100; i++) {
          
            if (i % 7 == 0) {
		count++;
           	 
            }
        }
        System.out.println("The total count of numbers divisible by 7 from 1 to 100 is " + count);
   }	
}