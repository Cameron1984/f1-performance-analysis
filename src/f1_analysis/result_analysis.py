#Display a full session classification with relevant columns
def display_classification(results):
    formatted_results = format_time(results)
    return(formatted_results[["Position", "FullName", "TeamName", "Time", "Points"]])

#Display relevant data about a specified drivers session
def display_driver_summary(results, driver):
    formatted_results = format_time(results)
    return formatted_results[["FullName", "Position", "TeamName","Points", "Time"]][results["FullName"] == driver]

    
#Convert timedelta => string and slice out days 
def format_time(results):
    formatted_results = results.copy()

    formatted_results["Time"] = formatted_results["Time"].apply(
    lambda x: str(x).split(" ")[-1]
    )
    return formatted_results