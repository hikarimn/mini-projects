# US
# California -> Santa Clara County -> students
# California -> San Mateo County -> students
# Maryland -> Montgomery County -> students
# Maryland -> PG County -> students


class Country():
    def __init__(self, name, states = None):
        self.name = name
        self.states = states

class State():
    def __init__(self, name, counties = None):
        self.name = name
        self.counties = counties

class County():
    def __init__(self, name, students = None, counties = None):
        self.name = name
        self.students = students
        self.counties = counties
        
def add_county_to_county(parent, children):
    if not parent.counties:
        pass
    parent.counties.append(children)
    
def count_females(country):
    counter = 0
    print(len(country.states))
    print(country.name)
    for state in country.states:
        # print(state.name)
        print('state')
        print(state.name)
        if not state.counties:
           continue 
       
        for county in state.counties:
            print(county.name)
            counter += helper(county)
            # if not county.students:
            #     continue 
            # for student in county.students:
            #     print(student)
            #     if student['gender'] == 'female':
            #         counter += 1
    print('counter')
    print(counter)
    return counter

def helper(county):
    if county.students:
        counter = 0
        for student in county.students:
            if student['gender'] == 'female':
                counter += 1
        print('counter')
        print(counter)
        return counter
    else:
        if not county.counties:
            return 0
        for county_elem in county.counties:
            return helper(county_elem)
    

california = State("California")
maryland = State("Maryland")
montgomery = County('Montgomery County',  counties = [])

# montomery2 = County('county_name', [{
#     'name': 'name1', 'gender' : 'female'
# }, {
#     'name': 'name2', 'gender': 'male'
# }])
montgomery2 = County('county_name', counties = [])

montgomery3 = County('county_name2', [{
    'name': 'name1', 'gender' : 'female'
}, {
    'name': 'name2', 'gender': 'male'
}, {
    'name': 'name1', 'gender' : 'female'
}, {
    'name': 'name2', 'gender': 'male'
}])

add_county_to_county(montgomery, montgomery2)

add_county_to_county(montgomery2, montgomery3)

pg = County('PG County', students=[{'name': 'name3', 'gender': 'female'}])
maryland.counties = [montgomery, pg]


usa = Country("USA", [california, maryland])

count_females(usa)
