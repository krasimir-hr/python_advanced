def palindrome(word, index=0):
    length = len(word)
    if index >= length // 2:
        return f"{word} is a palindrome"

    if word[index] != word[length - 1 - index]:
        return f"{word} is not a palindrome"

    return palindrome(word, index + 1)