import unittest
from main import RepositoryNames, RepositoryCommitNumbers

class TestGithub(unittest.TestCase):
    def testRepositoryCommitNumbers(self):
        google = RepositoryNames('google')
        self.assertIn('acai',google)
        self.assertIn('addlicense',google)
        fb = RepositoryNames('facebook')
        self.assertIn('ds2',fb)
        self.assertIn('duckling',fb)
        duckling_num = RepositoryCommitNumbers('duckling','facebook')
        self.assertEquals(duckling_num,30)
        acai_num = RepositoryCommitNumbers('acai','google')
        self.assertEquals(acai_num,30)

