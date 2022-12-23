import sys

 #step1
def task_medals(file_with_data, country, year):
    n = 0
    medals = []
    with open(file_with_data, "r") as file:
        headline = file.readline()
        line = file.readline()
        gold = 0
        silver = 0
        bronze = 0
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
                            gold += 1
                        if "Silver" in medal_line:
                            silver += 1
                        if "Bronze" in medal_line:
                            bronze += 1

            line = file.readline()
        print(f"Gold medals", {gold}, "Silver medals", {silver}, "Bronze medals", {bronze})



# year_list = sorted(year_set)
# for i,y, in enumerate(year_list[:10],1):
#     print(i, "\t", y, "\t" )

# set cortage
file_with_data = "data.tsv"
# country = "DEN"
# year = "1900"
#
# task_medals(file_with_data, country, year) !!!!!!!!

#step2
def total():
    dict ={}
    file = sys.argv[1]
    year = sys.argv[3]
    with open(file, "r") as file:
        line = file.readline()
        while line:
            line_splited = line.split("\t")
            medal_line = line_splited[-1][:-1]
            year_file = line_splited[9]
            country_file = line_splited[6]
            country_team = line_splited[7]
            if country_file and country_team in line_splited:
                if medal_line != "NA":
                    if country_team not in dict and year_file == year:
                        dict[country_team] = [0,0,0]
                    elif medal_line == "Gold" and year_file == year:
                        dict[country_team][0] += 1
                    elif medal_line == "Silver" and year_file == year:
                        dict[country_team][1] += 1
                    elif medal_line == "Bronze" and year_file == year:
                        dict[country_team][2] += 1
            line = file.readline()
        for country, medals in dict.items():
            if medals != [0,0,0]:
                print(f"{country} - gold medals {medals[0]}, silver medals {medals[1]}, bronze medals {medals[2]}")


def overall(countries):
    file = sys.argv[1]
    # countries = sys.argv[3:],
    dict = {}
    for country in countries:
        with open(file, "r") as file:
            line = file.readline()
            line = file.readline()
            while line:
                line_splited = line.split("\t")
                country_team = line_splited[7]
                country_file = line_splited[6]
                medal_line = line_splited[-1][:-1]
                year_file = line_splited[9]
                if year_file not in dict and (country_team == country or country_file == country):
                    dict[year_file] = 0
                elif medal_line != "NA" and year_file in dict and country_team == country:
                    dict[year_file] += 1
                line = file.readline()
        dict_keys = [int(key) for key in dict.keys()]
        dict_values = [int(key) for key in dict.values()]
        max_value = max(dict_values)
        print(f'{country} - {max_value} - {dict_keys[dict_values.index(max_value)]}')
        dict.clear()
        return dict_keys, dict_values


#step4
def interactive():
    file = sys.argv[1]
    input_country = input("Enter a country: ")
    first_year_olimp = None
    first_place_olimp = None
    years = []
    golds = 0
    silvers = 0
    bronzes = 0
    with open(file, "r") as file:
        line = file.readline()
        while line:
            line_splited = line.split("\t")
            country_team = line_splited[7]
            country_file = line_splited[6]
            medal_line = line_splited[-1][:-1]
            # country_line2 = line_after_split[8]
            year_file = line_splited[9]
            city_line = line_splited[-4]
            if (country_team == input_country or country_file == input_country) and year_file not in years:
                years.append(year_file)
            if (country_team == input_country or country_file == input_country) and medal_line != "NA":
                if medal_line == "Gold" and year_file in years:
                    golds += 1
                elif medal_line == "Silver" and year_file in years:
                    silvers += 1
                elif medal_line == "Bronze" and year_file in years:
                    bronzes += 1
                if (country_team == input_country or country_file == input_country) and first_year_olimp is None:
                    first_year_olimp = year_file
                    first_place_olimp = city_line
                elif (first_year_olimp is not None and country_team == input_country or country_file == input_country) and year_file < first_year_olimp:
                    first_year_olimp = year_file
                    first_place_olimp = city_line
            line = file.readline()
    average_gold_medals = golds / len(years)
    average_silver_medals = silvers / len(years)
    average_bronze_medals = bronzes / len(years)
    print(f"First olympiade for {input_country} was in {first_year_olimp} and that was in {first_place_olimp}")
    dict_values, dict_keys = overall([input_country])
    min_medals = min(dict_values)
    print(f"The fewest medals {input_country} earned in {dict_keys[dict_values.index(min_medals)]}'s year and the number was {min_medals}")
    print(f"Average number of gold medals: {average_gold_medals}\nAverage number of silver medals: {average_silver_medals}\nAverage number of bronze medals: {average_bronze_medals}")


mode = sys.argv[2]

if mode == "-total":
     total()
elif mode == "-medals":
    task_medals(file_with_data, country, year)
elif mode == "-overall":
    overall(countries)
elif mode == "-interactive":
    interactive()
