from data_loader import load_session
import result_features as result_features

'''
year = int(input("Year of Grand Prix: "))
race = input("Name of Race or Round Number: ")
gp_session = str(input("Session: "))

session = load_session(year, race, gp_session)
'''

session = load_session(2024, "Silverstone", "R")
results = session.results


#print(result_features.display_classification(results))
driver = input("enter a driver: ").title()
print(result_features.display_driver_summary(results, driver))
