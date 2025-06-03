import unittest
import mean_var_std


class UnitTests(unittest.TestCase):

    def test_calculate(self):
        actual = mean_var_std.calculate([2, 6, 2, 8, 4, 0, 1, 5, 7])
        expected = {
            'mean': [[3.6666666666666665, 5.0, 3.0],
                     [3.3333333333333335, 4.0, 4.333333333333333],
                     3.888888888888889],
            'variance':
            [[9.555555555555555, 0.6666666666666666, 13.555555555555555],
             [6.222222222222221, 10.666666666666666, 6.222222222222221],
             9.209876543209875],
            'standard deviation':
            [[3.091206165165235, 0.816496580927726, 3.6837489376754178],
             [2.494438257849294, 3.265986323710904, 2.494438257849294],
             3.0347778408328137],
            'max': [[8, 6, 7], [6, 8, 7], 8],
            'min': [[1, 4, 0], [2, 0, 1], 0],
            'sum': [[11, 15, 9], [10, 12, 13], 35]
        }
        self.assertEqual(actual['mean'][:2], expected['mean'][:2],
                         "Expected different result for 'mean'")
        self.assertAlmostEqual(actual['mean'][2],
                               expected['mean'][2],
                               msg="Expected different result for 'mean'")

        self.assertEqual(actual['variance'][:2], expected['variance'][:2],
                         "Expected different result for 'variance'")
        self.assertAlmostEqual(actual['variance'][2],
                               expected['variance'][2],
                               msg="Expected different result for 'variance'")

        self.assertEqual(actual['standard deviation'][:2],
                         expected['standard deviation'][:2],
                         "Expected different result for 'standard deviation'")
        self.assertAlmostEqual(
            actual['standard deviation'][2],
            expected['standard deviation'][2],
            msg="Expected different result for 'standard deviation'")
        self.assertEqual(actual['max'], expected['max'],
                         "Expected different result for 'max'")
        self.assertEqual(actual['min'], expected['min'],
                         "Expected different result for 'min'")
        self.assertEqual(actual['sum'], expected['sum'],
                         "Expected different result for 'sum'")


if __name__ == "__main__":
    unittest.main()
