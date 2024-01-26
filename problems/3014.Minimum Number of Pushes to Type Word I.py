class Solution:
    def minimumPushes(self, word: str) -> int:
         # Initialize variables to store the result, the size of the word, and the current row
        ans = 0
        n = len(word)
        row = 1

        # Calculate the quotient and remainder when dividing the length of the string by 8
        quotient = n // 8
        remainder = n % 8

        # Iterate over complete cycles (quotient)
        while quotient > 0:
            # Add the product of 8 (number of keys in a cycle) and the current row to the result
            ans += 8 * row

            # Decrement the quotient and increment the row for the next cycle
            quotient -= 1
            row += 1

        # Add the product of the remainder and the final row to account for remaining letters
        ans += remainder * row

        # Return the final result, representing the minimum number of key presses
        return ans       