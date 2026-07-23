from data_loader import load_session

desired_session = load_session(2024, "Silverstone", "R")

print(desired_session.results)