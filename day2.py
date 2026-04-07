''' JavaScript Object Notation '''

import json

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''


#print(people_string     )


# to load and manu json data
# data = json.loads(people_string)

# for person in data['people']:
#     print(person['name'])


#     data = json.loads(people_string)

# for person in data['people']:
#     del person['phone']

# new_string = json.dumps(data, indent=2, sort_keys=True)

# print(new_string)

# to print them 1 by 1
# data = json.loads(people_string)

# for person in data['people']:
#     print(person['name'])