func generate(numRows int) [][]int {
    if numRows == 1 {
        return [][]int{{1}}
    }

    triangle := generate(numRows - 1)
    prevRow := triangle[len(triangle) - 1]
    var newRow []int
    newRow = append(newRow, 1)

    for i := 1; i < len(prevRow); i++ {
        newRow = append(newRow, prevRow[i-1] + prevRow[i])
    }

    newRow = append(newRow, 1)
    triangle = append(triangle, newRow)

    return triangle
}
