import sys



year_set = set()
file = sys.argv[1]
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

# 1 step
def medals():
    country = sys.argv[3]
    with open(file, "r") as file:
        line = file.readline()
        while line != "":
            line_splited = line.split("\t")
            medal_line = line_splited[-1][:-1]
            sport_athlete = line_splited[-3]

            name_athlete = line_splited[1]
            counter = 1
            yeear = line_splited[9]
            contry = line_splited[-4]

            if country1 in line_splited:
                # if year in line_splited:
                    while counter < 10:
                        if medal_line != "NA":
                        # if name_athlete not in names and medal_line != "NA":
                            print(f'{counter}, {name_athlete} - {sport_athlete} - {medal_line}')
                            counter += 1
                            names.append(name_athletes)
                        else:
                            break
                    medals.append(medal_line)
            line = file.readline()

        if len(names) == 0:
            print("Try another number")
            quit()
        if counter < 10:
            print("It has less then 10 medalists")

        count_medals(medals, year)

country1 = input("Choose a country: ")
year1 = input("Choose a year: ")
command = input("Choose a command: ")

# 2step
def total():
    year = sys.argv[4]
#
# print(sys.argv[1:])
#
# print("country is", country, "year is", year)
