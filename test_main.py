import unittest
from main import database, authenticate, experiment

class QueryTests(unittest.TestCase):
    def setUp(self):
        self.db = database()
        self.addCleanup(self.db.close)
    def test_valid_login(self):
        self.assertTrue(authenticate(self.db, "student", "lab-secret"))
    def test_wrong_password(self):
        self.assertFalse(authenticate(self.db, "student", "wrong"))
    def test_unknown_user(self):
        self.assertFalse(authenticate(self.db, "missing", "lab-secret"))
    def test_vulnerable_bypass(self):
        self.assertTrue(authenticate(self.db, "' OR 1=1 -- ", "wrong", False))
    def test_parameterized_blocks_bypass(self):
        self.assertFalse(authenticate(self.db, "' OR 1=1 -- ", "wrong", True))
    def test_quotes_are_data(self):
        self.db.execute("INSERT INTO accounts VALUES (?, ?)", ("o'neal", "a'b"))
        self.assertTrue(authenticate(self.db, "o'neal", "a'b"))
    def test_empty_input(self):
        self.assertFalse(authenticate(self.db, "", ""))
    def test_proof_contract(self):
        r = experiment()
        self.assertTrue(r['vulnerable_bypass'])
        self.assertFalse(r['parameterized_bypass'])
