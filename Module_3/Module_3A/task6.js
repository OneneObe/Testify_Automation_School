const side1 = 10
const side2 = 15
const side3 = 10
if (side1 === side2 && side2 === side3){
    console.log("Equilateral Triangle")
} else if(side1 === side2 || side1 === side3 || side2 === side3){
    console.log("Isosceles triangle")
}else{"Scalene triangle"}