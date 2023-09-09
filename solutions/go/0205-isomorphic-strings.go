func isIsomorphic(s string, t string) bool {
    sToTMap := make(map[byte]byte) 
    tToSMap := make(map[byte]byte) 

    if len(s) != len(t) { 
        return false 
    } 

    for i := 0; i < len(s); i++ { 
        sChar, tChar := s[i], t[i] 

        if mappedChar, exists := sToTMap[sChar]; exists { 
            if mappedChar != tChar { 
                return false 
            } 
        } else { 
            sToTMap[sChar] = tChar 
        } 

        if mappedChar, exists := tToSMap[tChar]; exists { 
            if mappedChar != sChar { 
                return false 
            } 
        } else { 
            tToSMap[tChar] = sChar 
        } 
    } 

    return true 
                                                                                                                                                                                                           
}
