##FORMATTING##

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

#Convert lap times to seconds to aid time comparisons
#for a series of timedelta values
def times_to_seconds(times):
    return times.dt.total_seconds()

#Individual timedelta value
def time_to_seconds(time):
    return time.total_seconds()


###RACE FEATURES###

#Display every lap for a specified driver
def display_every_lap(laps, driver): 
    formatted_laps = format_time(laps)
    return formatted_laps["LapTime"][formatted_laps["Driver"] == format_driver_name(driver)]

'''
#Output delta difference between drivers laps
def comapare_laps(laps, driver1, driver2):
    laps_in_seconds = times_to_seconds(laps)
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
'''
def compare_laps(laps, driver1, driver2):

    driver1 = format_driver_name(driver1)
    driver2 = format_driver_name(driver2)

    driver1_laps = laps.pick_drivers(driver1)
    driver2_laps = laps.pick_drivers(driver2)

    driver1_laps = driver1_laps[["LapNumber", "LapTime"]]
    driver2_laps = driver2_laps[["LapNumber", "LapTime"]]

    #Essentially inner join between two tables (df's) for each driver
    comparison = driver1_laps.merge(
        driver2_laps, 
        on="LapNumber",
        suffixes=(f"_{driver1}", f"_{driver2}") #LapTime => LapTime_PIA
    )

    driver1_times = times_to_seconds(comparison[f"LapTime_{driver1}"])
    driver2_times = times_to_seconds(comparison[f"LapTime_{driver2}"])

    comparison["delta"] = driver1_times - driver2_times

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
    
    driver1 = format_driver_name(driver1)
    driver2 = format_driver_name(driver2)

    driver1_best = laps.pick_drivers(driver1).pick_fastest()
    driver2_best = laps.pick_drivers(driver2).pick_fastest()

    driver1_best_secs = time_to_seconds(driver1_best["LapTime"])
    driver2_best_secs = time_to_seconds(driver2_best["LapTime"])
    
    return round((driver1_best_secs - driver2_best_secs), 3)

def compare_sectors(laps, driver1, driver2, lap):
    
    driver1_lap = laps.pick_drivers(format_driver_name(driver1))
    driver1_lap = driver1_lap[driver1_lap["LapNumber"] == lap]

    driver2_lap = laps.pick_drivers(format_driver_name(driver2))
    driver2_lap = driver2_lap[driver2_lap["LapNumber"] == lap]
    sectors = ["Sector1Time", "Sector2Time", "Sector3Time"]
    
    deltas = driver1_lap[sectors].iloc[0] - driver2_lap[sectors].iloc[0]    

    return times_to_seconds(deltas)


    

    
    