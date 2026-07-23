import fastf1

fastf1.Cache.enable_cache('cache')

def load_session(year, race, session):
    session = fastf1.get_session(year, race, session)
    session.load()
    return session
    
