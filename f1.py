import logging

logging.basicConfig(
    filename="f1.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
s=eval(input("Enter a String"))
def countVowel(s:str)->int:
    """
    Count the number of vowels in a given string.
    Parameters:
        s (str): Input string
    Returns:
        int: Total number of vowels in the string.
    """
    logging.info("Counting vowels in the string")
    res=0
    for ch in s:
        if str.upper(ch) in "AEIOU":
            res +=1
    logging.info(f"Vowel count calculated: {res}")
    return res
res=countVowel(s)
print(f"Total vowel = {res}")