public class WordReverse {
   public static void main(String[] args) {
	String word = "Onyekachi";
	String reverse = "";
	
	for(int number = word.length() -1; number >= 0; number--){
		reverse = reverse + word.charAt(number);
	}
	System.out.print(reverse);
   }
}
		