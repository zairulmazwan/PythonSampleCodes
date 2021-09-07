import pandas as pd


data = [["Zairul",89],["Babak",91],["Rizwana",90],["Jilani",82],["Mazwan",75],["Rania",90],["Peter",75],["John",89],["Susan",75]]

print("This is a 2D list : ")
print("Name\t\tMarks")
print("-----------------")
for row in data:
        for col in row:
                print(col, end="\t\t ")

        print()



print("\nThis is how to convert from list to dataFrame : ")
colName = ["Name","Marks"]
pdData = pd.DataFrame(data, columns =colName)
print(pdData)

print("\nBut I dont want the index to be printed on the console!")
print(pdData.to_string(index=False))

print("\nHow about to revert from dataframe back to list format?")
dataList = pdData.values
print(dataList)


print("\nI want to see who get 75%")
res = pdData.loc[pdData.Marks==75]
print(res.to_string(index=False))
