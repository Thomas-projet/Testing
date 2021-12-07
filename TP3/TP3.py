from typing import Counter
import unittest


class Task:
    counter = 0
    def __init__(self, description):
        self.description = description
        self.status = True
        self.id = self.counter
        Task.counter = self.counter + 1
        


class Test(unittest.TestCase):
    def test_taskExist(self):
        task = Task("learn python")
        self.assertEqual("learn python", task.description)

    def test_taskStatusExist(self):
        task = Task("learn python")
        self.assertEqual(True, task.status)

    def test_taskIdExist(self):
        task = Task("learn python")
        self.assertLessEqual(0, task.id)

    def test_taskIdIsValid(self):
        task1 = Task("learn python")
        task2 = Task("learn python")
        self.assertNotEqual(task1.id, task2.id)


if __name__ == '__main__':
    unittest.main()
