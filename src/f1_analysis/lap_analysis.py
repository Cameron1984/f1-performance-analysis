###RACE FEATURES###

#Format time - type timedelta => string and slice out days column
def format_time(laps):
    formatted_laps = laps.copy()

    formatted_laps["LapTime"] = formatted_laps["LapTime"].apply(
    lambda x: str(x).split(" ")[-1]
    )
    return formatted_laps

#Format driver names so full names return abbreviation - "Lewis Hamilton" => "HAM"
def format_driver_name(driver):
    return driver.split(" ")[-1][0:3].upper()

#Display every lap for a specified driver
def display_every_lap(laps, driver): 
    formatted_laps = format_time(laps)
    return formatted_laps["LapTime"][formatted_laps["Driver"] == format_driver_name(driver)]

#Convert lap times to seconds to aid time comparisons
def laps_to_seconds(laps):
    #Copy to avoid editing original df
    laps_to_seconds = laps.copy()
    laps_to_seconds["LapTimeSeconds"] = laps_to_seconds["LapTime"].dt.total_seconds()
    return laps_to_seconds

#Output delta difference between drivers laps
def comapare_laps(laps, driver1, driver2):
    laps_in_seconds = laps_to_seconds(laps)
    #Oscar Piastri => PIA
    driver1 = format_driver_name(driver1)
    driver2 = format_driver_name(driver2)

    driver1_laps = laps_in_seconds.pick_drivers(driver1)
    driver2_laps = laps_in_seconds.pick_drivers(driver2)

    #Filter df for desired columns. d1_laps still df but has 2 columns only
    driver1_laps = driver1_laps[["LapNumber", "LapTimeSeconds"]]
    driver2_laps = driver2_laps[["LapNumber", "LapTimeSeconds"]]

    #Essentially inner join between two tables (df's) for each driver
    comparison = driver1_laps.merge(
        driver2_laps,
        on="LapNumber",
        suffixes=(f"_{driver1}", f"_{driver2}") #LapTimeSeconds => LapTimeSeconds_PIA
    )

    comparison["delta"] = (
        comparison[f"LapTimeSeconds_{driver1}"]
        - comparison[f"LapTimeSeconds_{driver2}"]
    )
    
    return comparison["delta"]


def get_fastest_lap_data(laps, driver):
    driver = driver.split(" ")[-1][0:3].upper()
    best_lap = laps.pick_drivers(driver).pick_fastest()
    return best_lap[
        ["Driver",
        "LapTime",
        "Sector1Time",
        "Sector2Time",
        "Sector3Time",
        "Compound",
        "TyreLife"
        ]
    ]

def compare_fastest_laps(laps, driver1, driver2):
    laps_seconds = laps_to_seconds(laps)
    driver1 = format_driver_name(driver1)
    driver2 = format_driver_name(driver2)

    driver1_best = laps_seconds.pick_drivers(driver1).pick_fastest()
    driver2_best = laps_seconds.pick_drivers(driver2).pick_fastest()
    
    return round((driver1_best["LapTimeSeconds"] - driver2_best["LapTimeSeconds"]), 3)
    

    
    