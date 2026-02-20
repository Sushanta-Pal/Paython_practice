import logging

logging.basicConfig(
    filename="f3.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def secondlargest(num:list)->int:
    """
    Find the second largest number in a given list of numbers.
    Parameters:
        num (list): Input list of numbers
    Returns:
        int: The second largest number in the list.
    """
    logging.info("Finding second largest number in the list")
    max=num[0]
    secondmax=num[0]
    for curr in num:
        if curr>max:
            secondmax=max
            max=curr
        elif curr>secondmax and curr!=max:
            secondmax=curr
    logging.info(f"Second largest number found: {secondmax}")
    return secondmax
num=eval(input("Enter a list of numbers"))
res=secondlargest(num)
print(res)