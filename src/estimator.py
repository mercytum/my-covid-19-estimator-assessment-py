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
  else:
    days = data['timeToElapse']



  impact['currentlyInfected'] = data['reportedCases'] * 10
  severeImpact['currentlyInfected'] = data['reportedCases'] * 50

  impact['infectionsByRequestedTime'] = math.trunc(impact['currentlyInfected']) * (2 ** math.trunc((days/factor)))
  severeImpact['infectionsByRequestedTime'] = math.trunc(severeImpact['currentlyInfected']) * (2 ** math.trunc((days/factor)))

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
#   'periodType': 'weeks',
#   'timeToElapse': 58,
#   'reportedCases': 674,
#   'population': 66622705,
#   'totalHospitalBeds': 1380614
# }

# print(estimator(data))



#Expected output
# {
# data: {}, // the input data you got
# impact: {}, // your best case estimation
# severeImpact: {} // your severe case estimation
# }

