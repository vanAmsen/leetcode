func compress(chars []byte) int {
    writeIndex := 0
    readIndex := 0

    for readIndex < len(chars) {
        char := chars[readIndex]
        count := 0

        for readIndex < len(chars) && chars[readIndex] == char {
            readIndex++
            count++
        }

        chars[writeIndex] = char
        writeIndex++

        if count > 1 {
            for _, digit := range strconv.Itoa(count) {
                chars[writeIndex] = byte(digit)
                writeIndex++
            }
        }
    }

    return writeIndex
}
