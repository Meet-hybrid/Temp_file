public class PrintEvenNumbers {
    
    public static void printEvenNumbers() {
        String result = ""; 
        for (int i = 1; i <= 100; i++) {
          
            if (i % 2 == 0) {
            	result += i + " "; 
            }
        }
        
   	return result; 
}