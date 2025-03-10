# Reference: https://realpython.com/token-based-authentication-with-flask/#jwt-setup
import unittest

from flask import current_app
from flask_testing import TestCase

from project.server import app

class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.server.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'diagnostic_secret')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///diagnostic.db'
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.server.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'diagnostic_secret')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///diagnostic_test.db'
        )

class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.server.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] is False)

if __name__ == '__main__':
    unittest.main()
