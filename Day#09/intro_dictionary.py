#Create directionary

job_description = {
    'title': "Software Engineer",
    'descrption': "Experienced with python programming and REST API",
    'salary': '45usd/hour',
    }


print(job_description)

# adding new items
job_description['location'] = "Remote"

print(job_description)

# create empty dictionary
programming_languages = {}

print(programming_languages)

# we can also empty a dictionary

#job_description = {}

#print("going to empty job_description dictionary")
#print(job_description)

#editing an item in dictionary
 
job_description['title'] = "Web Engineer"

print(job_description)



#loop through a directionary


for thing in job_description:
    print(thing)

print("Now going to print values")
for key in job_description:
    print(job_description[key])