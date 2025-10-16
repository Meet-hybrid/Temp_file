public class LowerCaseLetters {
   public static void main(String[] args) {
	String word = "Onyekachi";
	int count = 0;
	System.out.println("Number of uppercase in a string:");
   	
        for(int number = 0; number < word.length(); number++) {
		char letter = word.charAt(i);

		if(Character.isLowerCase(letter)) {
		count++;
						
		}
		
	}
		System.out.print(count);
    }
}