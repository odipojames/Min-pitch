import unittest
from app.models import User,Comment,Pitch

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password='peech')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('peech'))

class CommentModelTest(unittest.TestCase):

    def setUp(self):
        self.new_comment = Comment(id = 1, comment = 'its cool', user_id = 2 , pitchs_id = 4)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))

    def test_variables(self):
        self.assertEquals(self.new_comment.id, 1)
        self.assertEquals(self.new_comment.comment,'its cool')
        self.assertEquals(self.new_comment.user_id, 2)
        self.assertEquals(self.new_comment.pitchs_id, 4)

    # def test_get_comment(self):
    #     self.new_comment.save_comment()
    #     get_comment = Comment.get_comment(4)
    #     self.assertTrue(len(get_comment)==1)

class PitchModelTest(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(id = 1, category ='same' ,pitch='hi' ,user_id= 2)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))

    def test_variables(self):
        self.assertEquals(self.new_pitch.id, 1)
        self.assertEquals(self.new_pitch.category, 'same')
        self.assertEquals(self.new_pitch.pitch, 'hi')
        self.assertEquals(self.new_pitch.user_id, 2)
