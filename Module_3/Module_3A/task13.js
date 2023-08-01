
/**My Personal Library 2

Task

Add a toggleReadingStatus method to your books objects. 

The method should update the value of the reading property of the book object.

Remember to log the reading property to the console to confirm the current status. */

const books = {
    title: 'First Games',
    description: 'Fantasy',
    numberOfPages: 87,
    author: 'Nezz Nest',
    reading: true,
    toggleReadingStatus: function() {
        if(books.reading === true) {
            books.reading = false
        } else {
            books.reading = true
        }
    }
}

books.reading = true;
books.toggleReadingStatus();
console.log(books.reading);