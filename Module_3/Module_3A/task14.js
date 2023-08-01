const books = [
    {
        title: 'First Games',
        description: 'Fantasy',
        numberOfPages: 103,
        author: 'Nezz Nest',
        reading: true,
    },

    {
        title: 'faithful',
        description: 'Fantasy',
        numberOfPages: 90,
        author: 'Rose Perkins',
        reading: false
    },

    {
        title: 'All for Them',
        description: 'Action',
        numberOfPages: 112,
        author: 'Madison',
        reading: true
    }
]

for(let i=0; i<books.length; i++) {
    if(books[i].reading === true)
    console.log(books[i]);
}

//console.log(books[i].reading);

/**for(elem in books) {
    if(books[elem].reading === true) {
        console.log(elem, books[elem]);
    }
} **/