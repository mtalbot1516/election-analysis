print("Hello World")
counties_dict = {}
counties_dict["Arapahoe"] = 422829
print(counties_dict)
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432435
print(len(counties_dict))
print(counties_dict)
print(counties_dict.values())
print(counties_dict.keys())
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)
voting_data.append({"county":"El Paso", "registered_voters": 461169})
voting_data.pop(0)
print(voting_data)

counties = ["Arapahoe", "Denver", "Jefferson"]

#for county in counties:
#    print(county)
#print(range(len(counties)))
#for i in range(len(counties)):
#    print(counties[i])
#for county in counties_dict.keys():
#    print(county)

#for voters in counties_dict.values():
#    print(voters)

#for county in counties_dict:
#    print(counties_dict[county])

#for county in counties_dict:
#    print(counties_dict.get(county))

#for county, voters in counties_dict.items():
#    print(county, voters )

#for county_dict in voting_data:
#    print(county_dict)

#for i in range(len(voting_data)):
#    print(voting_data[i])

for county_dict in voting_data:
    for value in county_dict.values():
        print (value)

for county_dict in voting_data:
    print(county_dict['county'])

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters")

dir(voting_data)