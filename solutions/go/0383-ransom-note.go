func canConstruct(ransomNote string, magazine string) bool {
    // Create a map to store the frequency of each letter in magazine 
    letterFreq := make(map[rune]int) 

    // Populate the map with the frequency of each letter in magazine 
    for _, letter := range magazine { 
        letterFreq[letter]++ 
    } 

    // Iterate through the ransomNote and check if we can construct it 
    for _, letter := range ransomNote { 
        if freq, exists := letterFreq[letter]; !exists || freq == 0 { 
            return false 
        } 
        // Decrement the frequency of the current letter 
        letterFreq[letter]-- 
    } 

    return true 
                                                                                         
}
