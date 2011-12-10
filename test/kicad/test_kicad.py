import unittest

from os.path import dirname, join

from parser.kicad import KiCAD
from parser.openjson import JSON

TEST_INPUT_FILE = join(dirname(__file__), 'test.sch')
GOOD_OUTPUT_FILE = join(dirname(__file__), 'test.upv')


class KiCADTest(unittest.TestCase):

    def setUp(self):
        self.good = JSON().parse(GOOD_OUTPUT_FILE)
        self.actual = KiCAD().parse(TEST_INPUT_FILE)

    def test_points(self):
        """
        Test that all the points are present and have the right
        positions and connected points.
        """

        good_points = {}

        for net in self.good.nets:
            for pid, p in net.points.items():
                good_points[pid] = p

        self.assertEqual(len(good_points), 24)

        for net in self.actual.nets:
            for pid, p in net.points.items():
                goodp = good_points.pop(pid)
                self.assertEqual(p.point_id, goodp.point_id)
                self.assertEqual(p.x, goodp.x)
                self.assertEqual(p.y, goodp.y)
                self.assertEqual(set(p.connected_points),
                                 set(goodp.connected_points))

        self.assertEqual(good_points, {})

    def test_nets(self):
        """
        Test that all the right nets are present with
        the right points.
        """

        good_nets = self.good.nets[:]

        self.assertEqual(len(good_nets), 5)

        for net in self.actual.nets:
            for goodnet in good_nets:
                if set(net.points) == set(goodnet.points):
                    good_nets.remove(goodnet)
                    break
            else:
                raise Exception('bad net', net)

        self.assertEqual(good_nets, [])


if __name__ == '__main__':
    unittest.main()
