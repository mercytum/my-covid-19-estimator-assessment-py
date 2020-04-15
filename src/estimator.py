import datetime
import math 

def estimator(data):
  impact = {}
  severeImpact = {}
  factor = 3

  period_type = data['periodType']

  if period_type == 'weeks':
    days = data['timeToElapse'] * 7
  elif period_type == 'months':
    days = data['timeToElapse'] * 30
  elif period_type == 'days':
    days = data['timeToElapse']
  else:
    pass



  # impact['currentlyInfected'] = data['reportedCases'] * 10
  # severeImpact['currentlyInfected'] = data['reportedCases'] * 50

  impact_currentlyInfected = data['reportedCases'] * 10
  severeImpact_currentlyInfected = data['reportedCases'] * 50
  impact['currentlyInfected'] = math.trunc(impact_currentlyInfected)
  severeImpact['currentlyInfected'] = math.trunc(severeImpact_currentlyInfected)

  impact_infectionsByRequestedTime = impact_currentlyInfected * (2 ** (days/factor))
  severeImpact_infectionsByRequestedTime = severeImpact_currentlyInfected * (2 ** (days/factor))
  impact['infectionsByRequestedTime'] = math.trunc(impact_infectionsByRequestedTime)
  severeImpact['infectionsByRequestedTime'] = math.trunc(severeImpact_infectionsByRequestedTime)

  impact_severeCasesByRequestedTime = impact_infectionsByRequestedTime * 0.15
  severeImpact_severeCasesByRequestedTime = severeImpact_infectionsByRequestedTime * 0.15
  impact['severeCasesByRequestedTime'] = math.trunc(impact_severeCasesByRequestedTime)
  severeImpact['severeCasesByRequestedTime'] = math.trunc(severeImpact_severeCasesByRequestedTime)

  total_beds_available = data['totalHospitalBeds'] * 0.35
   
  if total_beds_available >= impact_severeCasesByRequestedTime:
     impact['hospitalBedsByRequestedTime'] = math.trunc(total_beds_available)
  else:
      impact['hospitalBedsByRequestedTime'] = math.trunc(total_beds_available - impact['severeCasesByRequestedTime'])
   
  if total_beds_available >= severeImpact_severeCasesByRequestedTime:
     severeImpact['hospitalBedsByRequestedTime'] = math.trunc(total_beds_available)
  else:
     severeImpact['hospitalBedsByRequestedTime'] = math.trunc(total_beds_available - severeImpact['severeCasesByRequestedTime'])
   


  output = {
    'data': data,
    'impact': impact,
    'severeImpact': severeImpact
    }
  

  return output

data = {
  'region': {
    'name': 'Africa',
    'avgAge': 19.7,
    'avgDailyIncomeInUSD': 5,
    'avgDailyIncomePopulation': 0.71
    },
  'periodType': 'days',
  'timeToElapse': 30,
  'reportedCases': 674,
  'population': 66622705,
  'totalHospitalBeds': 100
}

print(estimator(data))



#Expected output
# {
# data: {}, // the input data you got
# impact: {}, // your best case estimation
# severeImpact: {} // your severe case estimation
# }

