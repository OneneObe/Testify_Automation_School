// Create a length converter function

function lengthConverter(val, output ){
    let result=0;
        let unit = {
            'cm': 10,
            'km': 1,
            'mm': 1000,
        }
        for(let key in unit){
            result = val* unit[output];
        }
        return result;
    }
    console.log(lengthConverter(30, 'mm'));