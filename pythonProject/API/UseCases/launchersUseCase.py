from API.DataAccess.LauncherDataAccess import LauncherDataAccess
from API.Models.Launcher import Launcher

class LauncherUseCase:
    def __init__(self):
        self.dataAccess = LauncherDataAccess()

    def newLauncher(self, launcherName):
        if self.dataAccess.getLauncherByName(launcherName):
            return False, 'Launcher already exists'

        launcher = self.dataAccess.newLauncher(Launcher(launcherName))
        if not launcher:
            return False, 'Failed to create launcher'
        return True, launcher

    def getAllLaunchers(self):
        launchers = self.dataAccess.getAllLaunchers()
        if launchers is None:
            return False, 'Unable to get launchers'
        return True, launchers