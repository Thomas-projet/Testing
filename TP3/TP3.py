import unittest


class Task:
    
    def __init__(self, description):
        self.description = description
        self.status = True
        


class Test(unittest.TestCase):
    def test_taskExist(self):
        task = Task("learn python")
        self.assertEqual("learn python", task.description)

    def test_taskStatusExist(self):
        task = Task("learn python")
        self.assertEqual(True, task.status)

    def test_taskIdExist(self):
        task = Task("learn python", 0)
        self.assertEqual(0, task.id)


if __name__ == '__main__':
    unittest.main()
