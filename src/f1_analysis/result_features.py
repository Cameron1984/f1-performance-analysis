from data_loader import load_session

def display_classification(results):
    formatted_results = format_time(results)
    return(formatted_results[["Position", "FullName", "TeamName", "Time", "Points"]])

def display_driver_summary(results, driver):
    formatted_results = format_time(results)
    return formatted_results[["FullName", "Position", "TeamName","Points", "Time"]][results["FullName"] == driver]

    

def format_time(results):
    formatted_results = results.copy()

    formatted_results["Time"] = formatted_results["Time"].apply(
    lambda x: str(x).split(" ")[-1]
    )
    return formatted_results