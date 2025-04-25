from API.Services.databaseContext import *
from API.Models.Launcher import Launcher

class LauncherDataAccess:
    def newLauncher(self, newLauncher: Launcher):
        session = Session()
        try:
            session.add(newLauncher)
            session.commit()
            return session.query(Launcher).filter_by(name=newLauncher.name).first()
        except Exception as e:
            print(e)
            return False
        finally:
            session.close()

    def launcherExistsById(self, launcherId):
        session = Session()
        try:
            session.query(Launcher).filter_by(id=launcherId).first()
            if Launcher is None:
                return False
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            session.close()

    def getLauncherById(self, launcherId):
        session = Session()
        try:
            return session.query(Launcher).filter_by(id=launcherId).first()
        except Exception as e:
            print(e)
            return None
        finally:
            session.close()

    def getLauncherByName(self, launcherName):
        session = Session()
        try:
            return session.query(Launcher).filter_by(name=launcherName).first()
        except Exception as e:
            print(e)
            return None
        finally:
            session.close()

    def getAllLaunchers(self):
        session = Session()
        try:
            return session.query(Launcher).all()
        except Exception as e:
            print(e)
            return None
        finally:
            session.close()