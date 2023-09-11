func dailyTemperatures(temperatures []int) []int {
    n := len(temperatures) 
    answer := make([]int, n) 
    stack := []int{} 
 
    for i, temp := range temperatures { 
            for len(stack) > 0 && temperatures[stack[len(stack)-1]] < temp { 
                        last := stack[len(stack)-1] 
            stack = stack[:len(stack)-1] 
            answer[last] = i - last 
            } 
        stack = append(stack, i) 
    } 

    return answer 
                                                                         
}
