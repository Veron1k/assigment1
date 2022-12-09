import sys

# file = sys.argv[1]
# country = sys.argv[3]
# year = sys.argv[4]
#
# print(sys.argv[1:])
#
# print("country is", country, "year is", year)


year_set = set()
with open(file, "r") as file:
    line = file.readline()
    while line != "":
        line_splited = line.split("\t")
        year = int(line_splited[9])
        year_set.add(year)
        line = file.readline()

year_list = sorted(year_set)
for i,y in enumerate(year_list[:10],1):
    print(i, "\t", y)

# set cortage
