import unittest
import Tkinter as tk

from hall import Hall

class MyTestCase(unittest.TestCase):
    def test_create_hall(self):
        # Given
        root = tk.Tk()

        # When
        hall = Hall(root)


        tk.mainloop()

        # Then
        # I see the hall
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
