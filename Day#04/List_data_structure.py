
states_of_america = ["Delaware","Pennsylvania","New Jersey","Georgia","Connecticut","Massachusetts","Maryland","South Carolina","New Hampshire","Virginia","New York","North Carolina","Rhode Island","Vermont","Kentucky","Tennessee","Ohio","Louisiana","Indiana","Mississippi","Illinois","Alabama","Maine","Missouri","Arkansas","Michigan","Florida","Texas","Iowa","Wisconsin","California","Minnesota","Oregon","Kansas","West Virginia","Nevada","Nebraska","Colorado","North Dakota","South Dakota","Montana","Washington","Idaho","Wyoming","Utah","Oklahoma","New Mexico","Arizona","Alaska","Hawaii"]


# start from 0 index
print(states_of_america[0])

# Negative index start from the end
print(states_of_america[-1])
print(states_of_america[-50])

# update any item

states_of_america[1] = "Delaware-updated"

print(states_of_america[1])

#add to the list at the end
##append add single items at the end
states_of_america.append("Chitraliza")

print(states_of_america)

## adding list of items using extend()

states_of_america.extend(["Angelaland", "Jack Bauer Land"])

print(states_of_america)

