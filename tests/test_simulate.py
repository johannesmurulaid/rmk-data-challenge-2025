import unittest
from src.simulate import simulate_arrival_probability

class TestSimulation(unittest.TestCase):
    def test_extremely_early_time(self):
        prob = simulate_arrival_probability("07:00")
        self.assertTrue(0 <= prob <= 1)

    def test_normal_range(self):
        prob = simulate_arrival_probability("08:15")
        self.assertTrue(0 <= prob <= 1)

    def test_edge_case_meeting_time(self):
        prob = simulate_arrival_probability("08:55")
        self.assertTrue(0 <= prob <= 1)

if __name__ == '__main__':
    unittest.main()
