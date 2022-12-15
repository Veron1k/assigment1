import sys

# file_with_data = sys.argv[1]
# # file = sys.argv[1]
# country = sys.argv[3]
# year = str(sys.argv[4])
#
# print(sys.argv[1:])
#
# print("country is", country, "year is", year)


def task_medals(file_with_data, country, year):
    n = 0
    medals = []
    with open(file_with_data, "r") as file:
        headline = file.readline()
        line = file.readline()
        Gold = 0
        Silver = 0
        Bronze = 0
        names_of_medalist = []
        while line != "":
            line_splited = line.split("\t")
            medal_line = line_splited[-1][:-1]
            year_file = line_splited[9]
            name = line_splited[1]
            medal = line_splited[-1]
            sport = line_splited[12]
            country_file = line_splited[6]
            country_team = line_splited[7]
            if country == country_file or country == country_team and year == year_file:
                if medal != "NA\n":
                    if n < 10 and name not in names_of_medalist:
                        print(f'{n+1} - {name} - {sport} - {medal}')
                        names_of_medalist.append(name)
                        n += 1
                        if "Gold" in medal_line:
                            Gold += 1
                        if "Silver" in medal_line:
                            Silver += 1
                        if "Bronze" in medal_line:
                            Bronze += 1

            line = file.readline()
        print(f"Gold medals", {Gold}, "Silver medals", {Silver}, "Bronze medals", {Bronze})



    # year_list = sorted(year_set)
# for i,y, in enumerate(year_list[:10],1):
#     print(i, "\t", y, "\t" )

# set cortage
file_with_data = "data.tsv"
country = "DEN"
year = "1900"

task_medals(file_with_data, country, year)

