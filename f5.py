import logging

logging.basicConfig(
    filename="f5.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def revstr(s:str)->str:
    """
    Reverse a given string.
    Parameters:
        s (str): Input string
    Returns:
        str: The reversed string.
    """
    logging.info("Reversing the string")
    res=""
    for i in range(len(s)-1,-1,-1):
        res += s[i]
    logging.info(f"Reversed string: {res}")
    return res
print(revstr(input("Enter a String")))