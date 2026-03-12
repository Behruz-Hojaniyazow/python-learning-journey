#creating 10 major countries' capital cities
countries = {
        "Argentina" : "Buenos Aires",
        "Australia" : "Canberra",
        "Brazil" : "Brasilia",
        "Canada" : "Ottawa",
        "China" : "Beijing",
        "Egypt" : "Cairo",
        "France" : "Paris",
        "India" : "New Delhi",
        "Japan" : "Tokyo",
        "United States" : "Washington,D.C"
}
#asking from user
requested_c = input("Which country's capital city do you need?").title()
if requested_c in countries:
  print(f"{countries[requested_c]} is the capital city of {requested_c} ")
else:
  print(f"I do not have any information about {requested_c}")