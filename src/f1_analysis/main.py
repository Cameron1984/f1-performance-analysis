from data_loader import load_session
import result_analysis as result_analysis
import lap_analysis as lap_analysis


'''
#allow input of specific session
year = int(input("Year of Grand Prix: "))
race = input("Name of Race or Round Number: ")
gp_session = str(input("Session: "))

session = load_session(year, race, gp_session)
'''

session = load_session(2024, "Silverstone", "R")
results = session.results
laps = session.laps


#print(result_features.display_classification(results))
driver = input("enter a driver: ").title()
print(lap_analysis.display_every_lap(laps, driver))
