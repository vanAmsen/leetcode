func wordPattern(pattern string, s string) bool {
	wordMap := make(map[byte]string) 
	letterMap := make(map[string]byte) 
	words := strings.Fields(s) // Split s into words separated by space 
 
	if len(pattern) != len(words) { 
			return false 
	} 

	for i := 0; i < len(pattern); i++ { 
		ch := pattern[i] 
		word := words[i] 

		// Check if the character already has a corresponding word 
		if existingWord, ok := wordMap[ch]; ok { 
			if existingWord != word { 
				return false 
			} 
		} else { 
			wordMap[ch] = word 
		} 

		// Check if the word already has a corresponding character 
		if existingCh, ok := letterMap[word]; ok { 
			if existingCh != ch { 
				return false 
			} 
		} else { 
			letterMap[word] = ch 
		} 
	} 
	return true 
																																					
}
