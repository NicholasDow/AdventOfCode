package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func main() {
    // Open the file
    file, err := os.Open("input.txt")
    if err != nil {
        fmt.Println("Error opening file:", err)
        return
    }
    defer file.Close()

    // Initialize total to 0
    total := 0

    // Regular expression to find digits
    re := regexp.MustCompile(`\d`)

    // Create a scanner to read the file
    scanner := bufio.NewScanner(file)

    // Iterate over each line in the file
    for scanner.Scan() {
        // Find all digits in the line
        nums := re.FindAllString(scanner.Text(), -1)

        // Continue if no digits are found
        if len(nums) == 0 {
            continue
        }

        // Extract first and last digit and concatenate them
        firstDigit := nums[0]
        lastDigit := nums[len(nums)-1]
        newDigitStr := firstDigit + lastDigit

        // Convert the concatenated string to integer
        newDigit, err := strconv.Atoi(newDigitStr)
        if err != nil {
            fmt.Println("Error converting string to integer:", err)
            return
        }

        // Add the new digit to the total
        total += newDigit
    }

    // Check for errors during scanning
    if err := scanner.Err(); err != nil {
        fmt.Println("Error reading file:", err)
        return
    }

    // Print the total
    fmt.Println(total)
}