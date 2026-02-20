import logging

logging.basicConfig(
    filename="f7.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def findmissing(l:list)->int:
    """
    Find the missing number in a given list of numbers.
    Parameters:
        l (list): Input list of numbers
    Returns:
        int: The missing number in the list.
    """
    logging.info("Finding missing number in the list")
    n=len(l)+1
    sum1=n*(n+1)//2
    sum2=sum(l)
    logging.info(f"Missing number calculated: {sum1-sum2}")
    return sum1-sum2
l=eval(input("Enter a list of numbers"))
res=findmissing(l)
print(res)  
