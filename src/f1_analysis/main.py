from data_loader import load_session

year = int(input("Year of Grand Prix: "))
race = input("Name of Race or Round Number: ")
gp_session = str(input("Session: "))

session = load_session(year, race, gp_session)

results = session.results
#results.columns (returned list of driver numbers)
results.iloc[0]