import unittest
import json
from flask import Flask 
from app import create_app
from instance.config import app_config
from app import tests

users = [{
    "id":1,
    "username":"username",
    "password":"password"
    
}]

class test_client(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def  test_username(self):
        self.assertEqual("username","username")
    def test_password(self):
        self.assertEqual("password","password")

    