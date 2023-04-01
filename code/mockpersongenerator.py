import json
import person as pn
import random as rm


# returns n youth or saving accounts
def mock_person_generator(number_people, person_type):

    # Erstellen von Kundenlisten
    people_mock = []

    # opens json mock data file
    with open('mockdata.json') as json_file:
        daten = json.load(json_file)

    if person_type == 'youth':

        for i in range(number_people):

            # generates n people
            random_person = rm.randint(1, 1000)

            person_youth = pn.Person(daten[random_person]['name'], rm.randint(10, 25),
                                     f'756.7545.{rm.randint(1000, 9999)}.{rm.randint(10, 99)}',
                                     daten[random_person]['address'])

            people_mock.append(person_youth)

    if person_type == 'adult':

        for k in range(number_people):
            random_person = rm.randint(1, 1000)

            person_saving = pn.Person(daten[random_person]['name'], rm.randint(25, 89),
                                      f'756.7545.{rm.randint(1000, 9999)}.{rm.randint(10, 99)}',
                                      daten[random_person]['address'])

            people_mock.append(person_saving)

    return people_mock


if __name__ == '__main__':
    test = mock_person_generator(5, 'adult')
    print(type(test[0]))
    for i in test:
        print(i)
