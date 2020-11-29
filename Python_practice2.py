#my_votes = int(input("how many votes?"))
#total_votes = int(input("what is the total?"))
#percentage_votes = (my_votes/total_votes)*100
#print("i recd "+str(percentage_votes)+" % of votes")

#counties = ["arapahoe","denver","jefferson"]
##if counties[1] == "denver":
 ##   print(counties[1])
#if counties[3]!= "jefferson":
    #print(counties[2])

#temp = int(input("what is the temp outside?"))

#if temp > 80:
#    print("turn on AC")
#else:
#    print("open windows")

#if "el paso" in counties:
 #   print("el paso is in the list")
#else:
#    print("el paso is NOT in the list")

#if "arapahoe" in counties and "el paso" in counties:
#    print("both are in counties")
#else:
#    print("both are not in counties")

#if "arapahoe" in counties or "el paso" in counties:
#    print("arapahoe or el paso is in the counties")
#else:
#    print("Arapahoe and El Paso are not in the list of counties")

#if "arapahoe" in counties and "el paso" not in counties:
#   print("Only Arapahoe is in the list of counties.")
#else:
#    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

#for county in counties:
#    print(county)

#for i in range(len(counties)):
#    print (counties[i])
    ## i means the index and represents the values 0,1,2,etc. or in this case the length of the counties, the length of the counties is 0:2 so i is in that range of 2
    ##range() here means how long is the list -- which length determines the range
    ##so in print, it looks at the first i which is zero and prints what is at zero, in this case, its arapahoe, then it does this for i=1, which is denver, and then i=2, which is jefferson
    ##the output prints those three counties -- it will keep going till the range is done

##dictionary
#counties_dict = {"arapahoe":422829,"denver":463353,"jefferson":432438}
#counties_dict

#for i in counties_dict:
#    print (i)

##using keys -- in keys it doesnt matter what variable name you use -- use county or i in the variable
#for i in counties_dict.keys():
#    print(i)

#for voters in counties_dict.values():
#    print(voters)

#you can also get the values using this method:
#for county in counties_dict:
#    print(counties_dict[county])

#for county in counties_dict:
#    print(counties_dict.get(county))

#for county,voters in counties_dict.items():
#    print (str(county)+" county has",str(voters)+" registerd voters")

#voting_data = [
#{"county":"arapahoe","r_voters":"422829"},
#{"county":"denver","r_voters":"463353"},
#{"county":"jefferson","r_voters":"432438"}]

#for county_dict in voting_data:
#    print(county_dict)

##nested for loops - gets values from a list of dictionaries
#for county_dict in voting_data: ##pulls the key
#    for value in county_dict.values(): ##pulls the value to each key
#        print(value) ##prints the value

###using F-strings
#my_votes = int(input("how many votes?"))
#total_votes = int(input("what is the total?"))
##percentage_votes = (my_votes/total_votes)*100
##print(f"I rec'd {percentage_votes}% of the total votes")
#print(f"I rec'd {my_votes/total_votes * 100}% of the total votes")

#for county, voters in counties_dict.items():
#    print (f"{county} county has {voters} registered voters")


###multi-line fstrings
#candidate_votes = int(input("how many votes did you get?"))
#total_votes = int(input("what is total number of votes in the election?"))
#message_to_candidate = (
#    f"you rec'd {candidate_votes} votes."
#    f" the total number of votes in the election was {total_votes}."
#    f" you rec'd {candidate_votes/total_votes * 100:.2f} % of the total votes."
#)
#print(message_to_candidate)

#for county,voters in counties_dict.items():
#    print(f"{county} has {voters:,} registered voters")


voting_data = [
{"county":"arapahoe","r_voters":422829},
{"county":"denver","r_voters":463353},
{"county":"jefferson","r_voters":432438}]

#for voting_data[i]['j']:
#    print(f"{voting_data[i]['county']} county has {voting_data[j]['r_voters']:,} registered voters.")

print(f"{voting_data[0]['county']} county has {voting_data[0]['r_voters']:,} registered voters.")
print(f"{voting_data[1]['county']} county has {voting_data[1]['r_voters']:,} registered voters.")
print(f"{voting_data[2]['county']} county has {voting_data[2]['r_voters']:,} registered voters.")
