def letterCombinations(digits):
    if not digits:
        return []

    result = []
    letters = {
        "0": "",
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    stack = [(0, [])]
    while stack:
        index, chars = stack.pop()
        if index == len(digits):
            result.append("".join(chars))
        else:
            for child in letters[digits[index]]:
                stack.append([index+1, chars + [child]])
    return result


if __name__ == "__main__":
    digits = "23"
    print(letterCombinations(digits))
