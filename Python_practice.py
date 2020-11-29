print("Hello World")

print(5+2*3)

counties = ["arapahoe","denver","jefferson"]
counties

my_list = list()
my_list

print(counties[-1])

len(counties)
counties[:2]

counties.append("El Paso")
counties.insert(2,"el paso")
counties
counties.remove("el paso")
counties.pop(3)

counties[1]="El Paso"
counties.remove("arapahoe")
counties.append("denver")
counties
counties.append("arapahoe")
counties
my_tuple =()
my_tuple
counties_tuple = ("araphoe",'denver','jefferson')
len(counties_tuple)
counties_tuple[1]

my_dictionary = dict()
counties_dict = {}
counties_dict["arapahoe"]= 422829
counties_dict
counties_dict["denver"]=463353
counties_dict["jefferson"]=432438
len(counties_dict)
counties_dict.values()
counties_dict.get("denver")

voting_data =[]
voting_data.append({"county":"arapahoe","registered_voters": 422829})
voting_data.append({"county":"denver","registered_voters":463353})
voting_data.append({"count":"jefferson","registered_voters":432438})
voting_data
voting_data.append({"county":"el paso","registered_voters":461149})
voting_data.remove("arapahoe")




voting_data = []
    voting_data.append({"county":"arapahoe","r_voters":"422829"})
    voting_data.append({"county":"denver","r_voters":"463353"})
    voting_data.append({"county":"jefferson","r_voters":"432438"})
    len(voting_data)
    voting_data.insert(1,{"county":"el paso","r_voters":"461149"})
    voting_data
    voting_data.remove({"county":"arapahoe","r_voters":"422829"})
    voting_data.insert(1,{"county":"jefferson","r_voters":"432438"})
    voting_data.pop(-1)



    #3.2.8 
