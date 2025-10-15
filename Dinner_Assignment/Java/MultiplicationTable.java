public class MultiplicationTable {
    
    public static void main(String[] args) {
        
	int number = 9;
	 System.out.println("The multiplication Table of " + number);
   	
        for (int i = 1; i <= 12; i++) {
          
        System.out.println(number + " x " + i 
+ " = " + (number * i));
	}
   }	
}