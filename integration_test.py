import unittest
from student import Students
from payment import pay

class TestIntegration(unittest.TestCase):

    def test_payment_student(self):
        student = Students("Rizki")
        results = pay(student, 700000)
        self.assertEqual(results, "Rizki paid 700000")

if __name__ == '__main__':
    unittest.main()
