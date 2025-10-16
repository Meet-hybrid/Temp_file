 let number = 12345678;
 let reverse = 0;
        
     
        for (let i = 0; number > 0; number /= 10) {
            let digit = number % 10;
            reverse = reverse * 10 + digit;
        }
        
        console.log(reverse);
