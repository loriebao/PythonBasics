def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fib2(n, fn=[]):
    fn = [0, 1] 
    if n == 0:
        return fn.pop()
    elif n == 1:
        return fn

    for i in range(2,n+1):
        fn.append(fn[i-1] + fn[i-2])
    return fn

def user_prompt(prompt, retries=4, reminder="Please try again"):
    """Document your function purpose

    describe key algorithms here
    """
    while True:
        user_string = input(prompt)
        if user_string in ("ok", "yes", "y"):
            return True
        elif user_string in ("no", "n", "nope"):
            return False
        else:
            print(reminder)
        retries = retries - 1
        if retries < 0:
            print("Invalid input, run ouf of reties")
            break

def findword(word: str) -> str:
    """
    Searches a word for the pattern "cat" and returns the matched portion.

    Parameters:
    word (str): The word to search.

    Returns:
    str: The matched portion of the word, or None if no match is found.

    Raises:
    ValueError: If the input word is not a string.
    """
    if not isinstance(word, str):
        raise ValueError("Input must be a string")

    match word: #########only supported in 3.10
        case "cat":
            return word
