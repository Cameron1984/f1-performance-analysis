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

session = load_session(2024, "Silverstone", "Q")
results = session.results
laps = session.laps

d1 = "Max Verstappen"
d2 = "Lewis Hamilton"

print(f"{d1} best sectors:\n{lap_analysis.get_fastest_sectors(laps, d1)}")
print(f"{d2} best sectors:\n{lap_analysis.get_fastest_sectors(laps, d2)}")
print(f"{d1} best sectors:\n{lap_analysis.get_theoretical_fastest(laps, d1)}")
print(f"{d2} best sectors:\n{lap_analysis.get_theoretical_fastest(laps, d2)}")
theoretical_delta = lap_analysis.compare_theoretcial_fastest_laps(laps, d1, d2)
if theoretical_delta < 0: 
    print(f"{d1} could have been -{theoretical_delta} faster than {d2}")
else:
    print(f"{d2} could have been -{theoretical_delta} faster than {d1}")
