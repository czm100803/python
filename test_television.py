import unittest

from television import Television

class TestTelevision(unittest.TestCase):
    def test_tv1(self):
        tv_1 = Television()
        tv_1.power()
        self.assertEqual(str(tv_1), "Power = True, Channel = 0, Volume = 0")

        tv_1.channel_up()
        tv_1.channel_up()
        tv_1.volume_up()
        self.assertEqual(str(tv_1), "Power = True, Channel = 2, Volume = 1")

        tv_1.channel_up()
        tv_1.channel_up()
        tv_1.channel_up()
        tv_1.volume_down()
        tv_1.volume_down()
        self.assertEqual(str(tv_1), "Power = True, Channel = 1, Volume = 0")

        tv_1.power()
        tv_1.volume_up()
        tv_1.channel_down()
        self.assertEqual(str(tv_1), "Power = False, Channel = 1, Volume = 0")

        tv_1.power()
        tv_1.volume_up()
        tv_1.volume_up()
        tv_1.volume_up()
        tv_1.channel_down()
        tv_1.channel_down()
        self.assertEqual(str(tv_1), "Power = True, Channel = 3, Volume = 2")

        tv_1.mute()
        self.assertEqual(str(tv_1), "Power = True, Channel = 3, Volume = 0")

        tv_1.volume_down()
        self.assertEqual(str(tv_1), "Power = True, Channel = 3, Volume = 1")

        tv_1.mute()
        self.assertEqual(str(tv_1), "Power = True, Channel = 3, Volume = 0")

        tv_1.volume_up()
        self.assertEqual(str(tv_1), "Power = True, Channel = 3, Volume = 2")

        tv_1.power()
        tv_1.mute()
        self.assertEqual(str(tv_1), "Power = False, Channel = 3, Volume = 2")

    def test_tv2(self):
        tv_2 = Television()

        tv_2.power()
        tv_2.channel_up()
        tv_2.volume_up()
        self.assertEqual(str(tv_2), "Power = True, Channel = 1, Volume = 1")
