import time


class CleanerError(Exception):
    pass


class Battery20(CleanerError):
    pass


class Battery0(CleanerError):
    pass


class WaterError(CleanerError):
    pass


class TrashError(CleanerError):
    pass



class VacuumCleaner:
    def __init__(self, level_battery, level_trash, level_water):
        self.level_battery = round(float(level_battery))
        self.level_trash = round(float(level_trash))
        self.level_water = round(float(level_water))

    def move(self):
        while True:
            try:
                if self.level_battery <= 2:
                    raise Battery0()
                elif self.level_battery <= 20:
                    raise Battery20()
                if self.level_water <= 0 and self.level_trash >= 4:
                    print("I don't have neither water not space for trash ")
                    break
                elif self.level_trash < 0:
                    print("Value can't be zero")
                    break
                elif self.level_water < 0:
                    print("Value can't be zero")
                    break
                VacuumCleaner.wash(self)
                VacuumCleaner.vacuum_cleaner(self)
                time.sleep(1)
            except Battery0:
                print('Goodbye............')
                break
            except Battery20:
                if self.level_trash < 0:
                    print("Value can't be zero")
                    break
                elif self.level_water < 0:
                    print("Value can't be zero")
                    break
                elif VacuumCleaner.wash(self) == False and VacuumCleaner.vacuum_cleaner(self) == False:
                    print("I don't have neither water not space for trash ")
                    break
                print('Boss i need your help. Charge me')
                VacuumCleaner.wash(self)
                VacuumCleaner.vacuum_cleaner(self)

    def wash(self):
        try:
            if self.level_water == 0:
                raise WaterError()
            elif self.level_water < 1:
                self.level_battery -= round(self.level_battery * 0.1)
                return self.level_water - self.level_water
            elif self.level_water == 1:
                print('Running out of water')
            print('-Washing-')
            self.level_battery -= round(self.level_battery * 0.2)
            self.level_water -= 1
            print(f'Level baterry: {self.level_battery} Level water: {self.level_water}')
        except WaterError:
            return False

    def vacuum_cleaner(self):
        try:
            if self.level_trash >= 4:
                raise TrashError()
            elif self.level_trash == 3:
                print('Stop bro enough')
            print('-Cleaning-')
            self.level_battery -= round(self.level_battery * 0.2)
            self.level_trash += 1
            print(f'Level baterry: {self.level_battery} Trash level:'
                  f' {self.level_trash} ')
        except TrashError:
            return False

