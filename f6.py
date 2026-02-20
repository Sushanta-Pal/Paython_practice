import logging

logging.basicConfig(
    filename="f6.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def removedupicates(l:list)->list:
    """
    Remove duplicates from a given list.
    Parameters:
        l (list): Input list of numbers
    Returns:
        list: List with duplicates removed.
    """
    logging.info("Removing duplicates from the list")
    res=[]
    for i in l:
        if i not in res:
            res.append(i)
    logging.info(f"List after removing duplicates: {res}")
    return res
l=eval(input("Enter a list of numbers"))
res=removedupicates(l)
print(res)  