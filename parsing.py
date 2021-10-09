import json, csv

jsonFile = './covid_cases.json'
csvFile = './covid_cases.csv'
with open(jsonFile) as file1:
    covidCases = json.loads(file1.read())
with open(csvFile, 'w') as file2:
    covidCasesXml = csv.writer(file2)
    covidCasesXml.writerow(["dateRep", "countriesAndTerritories","cases", "deaths"])

    for case in covidCases ["records"]:
        covidCasesXml.writerow([case["dateRep"], case["countriesAndTerritories"],
        case["cases"], case ["deaths"]])