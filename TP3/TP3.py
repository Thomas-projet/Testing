import unittest


class Task:
    
    def __init__(self, description):
        self.description = description
        self.status = True
        self.id = 0
        


class Test(unittest.TestCase):
    def test_taskExist(self):
        task = Task("learn python")
        self.assertEqual("learn python", task.description)

    def test_taskStatusExist(self):
        task = Task("learn python")
        self.assertEqual(True, task.status)

    def test_taskIdExist(self):
        task = Task("learn python")
        self.assertEqual(0, task.id)

    def test_taskIdIsValid(self):
        task1 = Task("learn python")
        task2 = Task("learn python")
        self.assertNotEqual(task1.id, task2.id)


if __name__ == '__main__':
    unittest.main()
