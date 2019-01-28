'''
Unit Tests
function: ObjectId2UnixTimeStamp
'''

import unittest
import sys
from bson.objectid import ObjectId

sys.path.append("..")

import Mongo


class TestObjectId2UnixTimeStamp(unittest.TestCase):

    def test_ObjectId2UnixTimeStamp1(self):

        objstr = "5c4dc95cbb8b0b4811da29b4"
        test = Mongo.Mongo.ObjectId2UnixTimeStamp(objstr)
        self.assertEquals(test, 1548572892.0)

    def test_ObjectId2UnixTimeStamp2(self):

        objstr = "5c4dc95cbb8b0b4811da29b4"
        objectid = ObjectId(objstr)
        test = Mongo.Mongo.ObjectId2UnixTimeStamp(objectid)
        self.assertEquals(test, 1548572892.0)

    def test_ObjectId2UnixTimeStamp3(self):

        objstr = "5c4dc95cbb8b0b4811da29b"
        try:
            Mongo.Mongo.ObjectId2UnixTimeStamp(objstr)
        except TypeError as err:
            self.assertEquals(err.message, "Invalid ObjectId!")

    def test_ObjectId2UnixTimeStamp4(self):

        objstr = 123
        try:
            Mongo.Mongo.ObjectId2UnixTimeStamp(objstr)
        except TypeError as err:
            self.assertEquals(err.message, "Invalid ObjectId!")
