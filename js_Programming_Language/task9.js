//9. Return the number of vowels in a string
function vowels (string){
    let vowels = [ 'a', 'e', 'i', 'o', 'u'];
    let numberOfVowels = 0;
    let vow = string.split('');
    for (let i = 0; i < vow.length; i++) {
        for (let j = 0; j < vowels.length; j++) {
            if (vow[i] === vowels[j]) {
                numberOfVowels ++;
            }
            
        }
    }
    return numberOfVowels;


}
console.log(vowels('Learning Javascript'));