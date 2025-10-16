let word = "Onyekachi";
let reverse = "";
	
	for(let number = word.length() -1; number >= 0; number--){
		reverse = reverse + word.charAt(number);
	}
	console.log(reverse);
