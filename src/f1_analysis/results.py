from data_loader import load_session

def display_classification(results):
    results["Time"] = results["Time"].apply(
    lambda x: str(x).split(" ")[-1]
    )
    return(results[["Position", "FullName", "TeamName", "Time", "Points"]])
    