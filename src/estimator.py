import datetime

def estimator(data):
  impact = {}
  severeImpact = {}
  factor = 3
  futureDate = datetime.date(2020,5,13)
  today = datetime.date.today()
  days = (futureDate - today).days



  impact['currentlyInfected'] = data['reportedCases'] * 10
  severeImpact['currentlyInfected'] = data['reportedCases'] * 50

  impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * (2 ** (days/factor))
  severeImpact['infectionsByRequestedTime'] = severeImpact['currentlyInfected'] * (2 ** (days/factor))

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
#   'timeToElapse': 58,
#   'reportedCases': 674,
#   'population': 66622705,
#   'totalHospitalBeds': 1380614
# }

# estimator(data)



#Expected output
# {
# data: {}, // the input data you got
# impact: {}, // your best case estimation
# severeImpact: {} // your severe case estimation
# }

