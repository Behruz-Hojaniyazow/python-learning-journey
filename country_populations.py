#population of countries
popul_countries = {
        "Turkmenistan" : 7703300,
        "Uzbekistan" : 37518100,
        "Turkey" : 87831700,
        "Russia" : 143425200,
        "Kazahstan" : 20600000
}
#Sort by value (population)
sorted_countries = sorted(popul_countries.items(),key=lambda item: item[1])
for country, population in sorted_countries:
  print(f"{country}'s population is {population}")