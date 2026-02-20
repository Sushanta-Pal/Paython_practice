import logging

logging.basicConfig(
    filename="f4.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def sortCheck(l:list)->bool:
    """
    Check if a given list of numbers is sorted in non-decreasing order.
    Parameters:
        l (list): Input list of numbers
    Returns:
        bool: True if sorted, False otherwise.
    """
    logging.info("Checking if list is sorted")
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            logging.info("List is not sorted")
            return False
    logging.info("List is sorted")
    return True
l=eval(input("Enter a list of numbers"))
res=sortCheck(l)
print(res)