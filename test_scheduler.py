import unittest
from scheduler import schedule

class TestScheduler(unittest.TestCase):
    def job(self, duration, priority):
        return {'duration' : duration, 'priority' : priority}

    def test_equal_priority(self):
        initial_jobs = [self.job(3,1), self.job(2,1), self.job(1,1)]
        schedule(initial_jobs)
        self.assertEqual(initial_jobs, [self.job(1,1), self.job(2,1), self.job(3,1)])

    def test_equal_duration(self):
        initial_jobs = [self.job(1,2), self.job(1,1), self.job(1,3)]
        schedule(initial_jobs)
        self.assertEqual(initial_jobs, [self.job(1,3), self.job(1,2), self.job(1,1)])

    def test_mixed_values_and_duplicates(self):
        initial_jobs = [self.job(2,2), self.job(2,2), self.job(1,5), self.job(1,3), self.job(4,2), self.job(4,1)]
        schedule(initial_jobs)
        print initial_jobs
        self.assertEqual(initial_jobs, [self.job(1,5), self.job(1,3), self.job(2,2), self.job(2,2), self.job(4,2), self.job(4,1)])

if __name__ == '__main__':
    unittest.main()
