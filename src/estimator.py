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



  impact['currentlyInfected'] = data['reportedCases'] * 10
  severeImpact['currentlyInfected'] = data['reportedCases'] * 50

  impact['infectionsByRequestedTime'] = math.trunc(impact['currentlyInfected']) * (2 ** math.trunc((days/factor)))
  severeImpact['infectionsByRequestedTime'] = math.trunc(severeImpact['currentlyInfected']) * (2 ** math.trunc((days/factor)))

  impact['severeCasesByRequestedTime'] = math.trunc(impact['infectionsByRequestedTime'] * 0.15)
  severeImpact['severeCasesByRequestedTime'] = math.trunc(severeImpact['infectionsByRequestedTime'] * 0.15)




  total_beds_available = data['totalHospitalBeds'] * 0.35
   
  if total_beds_available >= impact['severeCasesByRequestedTime']:
     impact['hospitalBedsByRequestedTime'] = math.trunc(total_beds_available)
  elif total_beds_available < impact['severeCasesByRequestedTime']:
      impact['hospitalBedsByRequestedTime'] = math.trunc(total_beds_available - impact['severeCasesByRequestedTime'])
  else:
    pass
  
  if total_beds_available >= severeImpact['severeCasesByRequestedTime']:
     severeImpact['hospitalBedsByRequestedTime'] = math.trunc(total_beds_available)
  elif total_beds_available < severeImpact['severeCasesByRequestedTime']:
     severeImpact['hospitalBedsByRequestedTime'] = math.trunc(total_beds_available - severeImpact['severeCasesByRequestedTime'])
  else:
    pass
   


  output = {
    'data': data,
    'impact': impact,
    'severeImpact': severeImpact
    }
  

  return output

# data = {
#   'region': {
#     'name': 'Africa',
#     'avgAge': 19.7,
#     'avgDailyIncomeInUSD': 5,
#     'avgDailyIncomePopulation': 0.71
#     },
#   'periodType': 'days',
#   'timeToElapse': 30,
#   'reportedCases': 674,
#   'population': 66622705,
#   'totalHospitalBeds': 100
# }

# print(estimator(data))



#Expected output
# {
# data: {}, // the input data you got
# impact: {}, // your best case estimation
# severeImpact: {} // your severe case estimation
# }

