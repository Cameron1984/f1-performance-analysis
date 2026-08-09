from pathlib import Path
import pandas as pd
import fastf1

root = Path(__file__).resolve().parent.parent.parent

cache_path = root / "cache"

#enable caching to prevent repeated calls 
fastf1.Cache.enable_cache(cache_path)

#load a session. returns a session from an event
def load_session(year, race, session):
    session = fastf1.get_session(year, race, session)
    session.load()
    return session

