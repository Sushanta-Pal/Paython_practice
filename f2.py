import logging

logging.basicConfig(
    filename="f2.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def frequency(s:str):
    """
    Count the frequency of each character in a given string.
    Parameters:
        s (str): Input string
    Returns:
        dict: Dictionary with character frequencies.
    """
    logging.info("Counting frequency of each character in the string")
    d={}
    for ch in s:
        if ch not in d:
            d[ch]=1
        else:
            d[ch]+=1
    logging.info(f"Character frequency calculated: {d}")
    return d
s=eval(input("Enter a String"))
res=frequency(s)
print(res)