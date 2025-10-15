public class PrintOddNumbers {
    
    public static void main(String[] args) {
        
        for (int i = 50; i <= 100; i++) {
          
            if (i % 2 == 1) {
            System.out.print(i + " ");	 
            }
        }
        System.out.println();
   }	
}