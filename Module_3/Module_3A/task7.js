/** Task 7
Task: Types of triangle
Triangles can be classified based on the length of the sides relative to one another. 

If all the sides of  triangle are equal, that triangle is called Equilateral triangle

If ONLY TWO sides of the triangle are equal, that triangle is called Isosceles triangle

If NONE of sides of  the triangle are equal, that triangle is called Scalene triangle

Write a Javascript program that prints the name of the triangle based on the length of the sides in relation to one another.

Print Equilateral triangle if all the sides are equal

Print Isosceles triangle if only two the sides are equal

Print Scalene triangle if only none of the sides are equal

Steps

Initialize three variables side1, side2 and side3, and assign each a number which represents the each side of the triangle

Write an if statement to check if all side1, side2 and side3 are all equal. Then print: Equilateral triangle to the console.

Add an else …if block to check if there are any two sides that are equal (side1 === side2 or side1 === side3 or side2 === side3). Then print: Isosceles triangle to the console.

Add an else block that  just prints: Scalene triangle to the console. */

const side1 = 10
const side2 = 15
const side3 = 10
if (side1 === side2 && side2 === side3){
    console.log("Equilateral Triangle")
} else if(side1 === side2 || side1 === side3 || side2 === side3){
    console.log("Isosceles triangle")
}else{"Scalene triangle"}
