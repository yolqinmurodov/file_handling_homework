def file01():
#     """
#     The data is from the file. Return data as a list type.
#     Args:
#         data: str
#     Returns:
#         list: return answer
#     """
    f = open("data/data01.txt", "r")
    data = f.read()
    list1 = data.split(",")
    return list1
print(file01())    
# Read data from file