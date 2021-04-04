from HW10_1 import VacuumCleaner
import unittest


class TestVauumCleaner(unittest.TestCase):

    def setUp(self) -> None:
        self.prmt1 = VacuumCleaner(0, 0, 0)
        self.prmt2 = VacuumCleaner(20, -1, 0)
        self.prmt3 = VacuumCleaner(50, 10, -10)
        self.prmt4 = VacuumCleaner(100, 100, 100)
        self.prmt5 = VacuumCleaner(100, -1, -1)
        self.prmt6 = VacuumCleaner('10', '-1', '0')
        self.prmt7 = VacuumCleaner(50, 0.2, 3.1)
        self.prmt8 = VacuumCleaner(80.1, 0, 3)
        self.prmt9 = VacuumCleaner(10, 3, 1)
        self.parsms = [self.prmt1, self.prmt2, self.prmt3, self.prmt4, self.prmt5, self.prmt6, self.prmt7, self.prmt8,
                       self.prmt9]

    def test_move(self):
        for x in self.parsms:
            water = x.level_water
            trash = x.level_trash
            battery = x.level_battery
            with self.subTest(print(f'------- battery{battery},trash{trash}, water{water} ')):
                x.move()
        with self.assertRaises(ValueError):
            VacuumCleaner('x', 1, 2)


