print("Hello World")
type(3)

type(2019)
ballots = 1,341
ballots

type(73.81)
5 + 2 * 3
8 // 5 - 3
(5 + 2) * 3
5 + (9 * 3 / 2 - 4)
counties = ["Arapahoe","Denver","Jefferson"]
counties
counties[0]
counties[-1]
counties[-2]
len(counties)
counties[0:2]
counties[0:3]
counties[:2]
counties[:1]
counties[2:]
counties[1:]
counties[1:]
counties[1] = "El Paso"
counties
counties.insert(0, "Hunter")
counties
counties.insert(2, "Denver")
counties
counties
counties.remove("El Paso")
counties
counties_tuple = ("Arapahoe","Denver","Jefferson")
counties
len(counties_tuple)
counties_tuple[0
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict
len(counties_dict)
counties_dict
{'Arapahoe': 422829}
counties_dict["Arapahoe"] = 422829
counties_dict
counties_dict["Jefferson"] = 432438
counties_dict
counties_dict.items()
counties_dict.keys()counties_dict.values()
counties_dict.values()
counties_dict.get("Denver")
counties_dict[Arapahoe]
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data



# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
    print("I received " + str(percentage_votes)+"% of the total votes.")








# Pratice 3.2.8
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])    



counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")


if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")


x = 0
while x <= 5:
    print(x)
    x = x + 1

count = 7
while count < 1:
    print("Hello World")

for county in counties:
    print(county)


numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)


for i in range(len(counties)):
    print(counties[i])


for i in range(len(counties_tuples)):
      print(counties_tuples[i])


for i in len(counties_tuples):
    print(counties_tuples[i])



counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}


#Skill Drill 3.2.10
for county,voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")



for county in counties_dict.items():
    print(county + "has 463353 registered registerd voters")


for county in counties_dict.keys():
     print(voters)

for county in counties_dict:
    print(counties_dict.get(county))

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

    voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

        for county_dict in voting_data:
for county_dict in voting_data:
    print(county_dict['registered_voters'])


print("Your interest for the year is $" + str(interest))

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")


counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
    
for county, voters in counties_dict.items():
        print(county + " county has " + str(voters) + " registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))