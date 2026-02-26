func isHappy(n int) bool {
    seen := make(map[int]bool)

    for n != 1 && !seen[n] {
        seen[n] = true
        n = operate(n)
    }

    return n == 1
}

func operate(n int) int {
    sum := 0
    for n != 0 {
        digit := n % 10
        sum += digit * digit
        n = n / 10
    }
    return sum
}