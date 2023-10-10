from checkers import checkout
from checkers import calc_crc32

out = "/home/user/out"


def test_step1():
    assert (checkout("cd {};7z h arx2.7z".format(out), calc_crc32(None, 'hash_crc'))), "Test1 FAIL"