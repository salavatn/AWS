import boto3
from faker import Faker

fake = Faker()

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('KinderGarten')


# count = 1
# while count <= 1:
#     count += 1
firts_name = fake.first_name()
last_name = fake.last_name()
birthday = fake.date_of_birth(minimum_age=1, maximum_age=6)
age = fake.random_int(min=1, max=6)

if age <= 3:    group = 'First Group'
elif age <= 5:  group = 'Second Group'
else:           group = 'Third Group'

record = {'ID': 1, 'Group': group, 'Kids': [{'Name': firts_name, 'Surname': last_name, 'Birthday': str(birthday), 'Age': age}]}

# table.put_item(Item=record)
print(f"\n\n{record}")


searching = "item"
parameters = dir(table)
for element in parameters:
    if searching in element:
        print(f"\t- {element}")