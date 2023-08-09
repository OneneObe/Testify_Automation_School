/** Task: The Odd Ones
Odd numbers are NOT divisible by 2. 
Write a Javascript program that prints out all the odd numbers between 1 and 20. Your code must use a for-loop */

let number = 20

for(let num = 1; num<=20; num++) {
    if(num % 2 !== 0){
      console.log(num)  
    }
}