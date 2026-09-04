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

d1 = "Max Verstappen"
d2 = "George Russell"
lap = 2
delta = lap_analysis.compare_fastest_laps(laps, d1, d2)
print(delta)
