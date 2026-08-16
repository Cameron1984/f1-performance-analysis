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

d1, d2 = "Lewis Hamilton", "Max Verstappen"

lap_comparisons = lap_analysis.comapare_drivers_laps(laps, d1, d2)
count = 0
for lap in lap_comparisons:
    if lap < 0:
        print(f"lap {count}: {d1} was {lap} faster than {d2}")
    else:
        print(f"lap {count}: {d1} was +{lap} slower than {d2}")
    count+=1

