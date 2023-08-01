//Print a table containing multiplication tables



/*let multiplicationTable = [];

for(let i=1 ; i<13 ; i++){
    for(let j=1 ; j<13 ; j++){
      multiplicationTable.push(`${i} times ${j} is ${i*j}`);
    }
}

console.log(multiplicationTable);*/

let result = '\n';
for (let i = 1; i < 13; i++) {
    for (let j = 1; j < 13; j++) {
        result += (i*j) + ' ';
    }
    result += '\n'
}
console.log(result)