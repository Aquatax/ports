import pandas
BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("data/french_words.csv")
# TODO 1. Create a dictionary in this format:
newlist = {row.French: row.English for (index, row) in data.iterrows()}
list = newlist
lista = []
listb = []

suba = []
subb = []

x = 0


for x in newlist:
    lista.append(x)
    listb.append(newlist[x])

for x in range(0, len(listb) - 1):
    value1 = listb[x]
    for z in range(0, len(listb) - 1):
        if z == x:
            pass
        elif value1 == listb[z]:
            print(value1)




