#Format time - type timedelta => string and slice out days column
def format_time(laps):
    formatted_laps = laps.copy()

    formatted_laps["LapTime"] = formatted_laps["LapTime"].apply(
    lambda x: str(x).split(" ")[-1]
    )
    return formatted_laps

#Display every lap for a specified driver
def display_every_lap(laps, driver): 
    formatted_laps = format_time(laps)
    return formatted_laps["LapTime"][formatted_laps["Driver"] == driver.split(" ")[-1][0:3].upper()]