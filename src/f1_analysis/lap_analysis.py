###RACE FEATURES###

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

#Convert lap times to seconds
def laps_to_seconds(laps):
    laps_to_seconds = laps.copy()
    laps_to_seconds["LapTimeSeconds"] = laps_to_seconds["LapTime"].dt.total_seconds()
    return laps_to_seconds

#Output delta difference between drivers laps
def comapare_drivers_laps(laps, driver1, driver2):
    laps_in_seconds = laps_to_seconds(laps)
    driver1 = driver1.split(" ")[-1][0:3].upper()
    driver2 = driver2.split(" ")[-1][0:3].upper()

    driver1_laps = laps_in_seconds.pick_drivers(driver1)
    driver2_laps = laps_in_seconds.pick_drivers(driver2)

    delta = (
        driver2_laps["LapTimeSeconds"].reset_index(drop=True)
        - driver1_laps["LapTimeSeconds"].reset_index(drop=True))

    lap_deltas = []
    for value in delta:
        lap_deltas.append(round(value, 3))
    return lap_deltas