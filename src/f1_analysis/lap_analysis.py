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

#Compare each lap for two drivers
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

#Get fasters lap for a driver + other data
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

#Compare sectors for specific lap between two drivers - returning delta for all 3
def compare_sectors(laps, driver1, driver2, lap):
    
    driver1_lap = laps.pick_drivers(format_driver_name(driver1))
    driver1_lap = driver1_lap[driver1_lap["LapNumber"] == lap]

    driver2_lap = laps.pick_drivers(format_driver_name(driver2))
    driver2_lap = driver2_lap[driver2_lap["LapNumber"] == lap]
    sectors = ["Sector1Time", "Sector2Time", "Sector3Time"]
    
    deltas = driver1_lap[sectors].iloc[0] - driver2_lap[sectors].iloc[0]    

    return times_to_seconds(deltas)

#Average lap time across a race
def get_average_lap_time(laps, driver):
    driver_laps = laps.pick_drivers(format_driver_name(driver))
    times = times_to_seconds(driver_laps["LapTime"])

    return round(times.mean(), 3)


def compare_average_lap_time(laps, driver1, driver2):
    return get_average_lap_time(laps, driver1) - get_average_lap_time(laps, driver2)
    

##QUALI FEATURES##

#Get fastest sectors in a Quali session
def get_fastest_sectors(laps, driver):
    driver = format_driver_name(driver)
    driver_laps = laps.pick_drivers(driver)
    sectors = ["Sector1Time", "Sector2Time", "Sector3Time"]
    return driver_laps[sectors].min()

#Add 3 fastest sectors to return a theoretical fastest lap
def get_theoretical_fastest(laps, driver): 
    sectors = get_fastest_sectors(laps, format_driver_name(driver))
    sectors = times_to_seconds(sectors)
    sectors_in_seconds = sum(sectors)

    return round(sectors_in_seconds, 3)

def compare_theoretcial_fastest_laps(laps, driver1, driver2):
    driver_1_theoretcial = get_theoretical_fastest(laps, format_driver_name(driver1))
    driver_2_theoretcial = get_theoretical_fastest(laps, format_driver_name(driver2))

    theoretical_delta = round((driver_1_theoretcial - driver_2_theoretcial), 3)

    return theoretical_delta



    