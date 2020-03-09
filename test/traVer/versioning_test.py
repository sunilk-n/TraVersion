import unittest

from traVer.versioning import Version


class Test(unittest.TestCase):
    """ The basic class that inherits unittest.TestCase
    """
    testVersions = ["1.1.0", "2.5.0-beta.3", "5.0.1-alpha.1"]
    testPreRelease = []

    def test_is_pre_version(self):
        for version in self.testVersions:
            version = Version(version)
            result = version.is_pre_version
            if result:
                self.assertTrue(result)
            self.testPreRelease.append(result)
        for i, is_pre in enumerate(self.testPreRelease):
            version = Version(self.testVersions[i])
            self.assertEqual(is_pre, version.is_pre_version)


if __name__ == '__main__':
    unittest.main()
