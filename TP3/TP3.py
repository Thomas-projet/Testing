import unittest


class Task:
    def __init__(self, description, status):
        self.description = description
        self.status = status



class Test(unittest.TestCase):
    def test_taskExist(self):
        task = Task("learn python")
        self.assertEqual("learn python", task.description)

    def test_taskStatusExist(self):
        task = Task("learn python", True)
        self.assertEqual(True, task.status)


if __name__ == '__main__':
    unittest.main()
