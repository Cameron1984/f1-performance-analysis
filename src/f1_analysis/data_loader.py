from pathlib import Path

root = Path(__file__).resolve().parent.parent.parent

cache_path = root / "cache"


import fastf1

fastf1.Cache.enable_cache(cache_path)

def load_session(year, race, session):
    session = fastf1.get_session(year, race, session)
    session.load()
    return session

