import json

def seedQualifications:
    file = open("qualifications.txt", "r")
    pk = 1

    data = []

    for line in file:
        commonData = {}
        qualiData = {}

        commonData['model'] = "medRegApp.Qualification"
        commonData['pk'] = str(pk)
        pk = pk + 1
        qualiData['name'] = line
        commonData['fields'] = qualiData
        data.append(commonData)

    json_data = json.dumps(data)

    print (json_data)

    file = open("fixture.json", "w")
    file.write(json_data)