import unittest

from src.createHotel import createHotel, createRoomsOnFloor


class TestCreateHotel(unittest.TestCase):
    def setUp(self) -> None:
        print("setup")
        pass

    def tearDown(self) -> None:
        print("teardon")
        pass

    def test_CreateHotel(self):
        actual_hotel_rooms = createHotel()
        expected_rooms_list = ['1A', "1B", '1C', '1D', '1E', '2E', '2D', '2C', '2B', '2A']
        assert actual_hotel_rooms, expected_rooms_list

    def test_createRoomsOnFloor(self):
        actual_rooms = createRoomsOnFloor(5,1)
        expected_rooms = ['1A', "1B", '1C', '1D', '1E']
        assert actual_rooms,expected_rooms




if __name__ == '__main__':
    unittest.main()
