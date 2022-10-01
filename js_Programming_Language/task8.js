/**
 * Return Boolean if number is divisible by 10
 */
function returnBool(){
    const numbers = [2]
    for(let i=0; i< numbers.length; i++){
        if(numbers[i] % 10 === 0){
            return true
            
        }else{
            return false
        }

    }
   
}

console.log(returnBool())
