/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
    let maxAltitude = 0; 
    let currentAltitude = 0; 

    for(let g of gain) { 
        currentAltitude += g; 
        if(currentAltitude > maxAltitude) 
            maxAltitude = currentAltitude; 
    } 
    return maxAltitude; 
                                                    
};
