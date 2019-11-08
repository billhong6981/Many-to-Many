#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
import console
from contextlib import contextmanager
from datetime import datetime
import inspect
from io import StringIO
import models
import pep8
import sys
from os import environ, stat
import unittest

Department = models.Department
Employee = models.Employee
User = models.User
STORAGE_TYPE = environ.get('HBNB_TYPE_STORAGE')
BHCommand = console.BHCommand
storage = console.storage
CNC = models.CNC


@contextmanager
def redirect_streams():
    """function redirects streams: stdout & stderr for testing purposes
    first creates StringIO obj, then saves / updates stdout & stderr"""
    new_stdout, new_stderr = StringIO(), StringIO()
    old_stdout, sys.stdout = sys.stdout, new_stdout
    old_stderr, sys.stderr = sys.stderr, new_stderr
    try:
        # returns new file streams
        yield new_stdout, new_stderr
    finally:
        # restore std streams to the previous value
        sys.stdout, sys.stderr = old_stdout, old_stderr


class TestBHcmdDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    @classmethod
    def setUpClass(cls):
        """init: prints output to mark new tests"""
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('.......  For the Console  .......')
        print('.................................\n\n')
        cls.all_funcs = inspect.getmembers(console.BHCommand,
                                           inspect.isfunction)

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nCommand interpreter for BH Todos project\n'
        actual = console.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = '\n    Command inerpreter class\n    '
        actual = BHCommand.__doc__
        self.assertEqual(expected, actual)

    def test_all_function_docs(self):
        """... tests for ALL DOCS for all functions in console file"""
        AF = TestBHcmdDocs.all_funcs
        for f in AF:
            if "_BHCommand_" in f[0]:
                self.assertIsNotNone(f[1].__doc__)

    def test_pep8_console(self):
        """... console.py conforms to PEP8 Style"""
        pep8style = pep8.StyleGuide(quiet=True)
        errors = pep8style.check_files(['console.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_file_is_executable(self):
        """... tests if file has correct permissions so user can execute"""
        file_stat = stat('console.py')
        permissions = str(oct(file_stat[0]))
        actual = int(permissions[5:-2]) >= 5
        self.assertTrue(actual)


@unittest.skipIf(STORAGE_TYPE == 'db', 'FS tests not for DB')
class TestBHcmdCreate(unittest.TestCase):
    """testing instantiation of CLI & create() function"""

    @classmethod
    def setUpClass(cls):
        """init: prints output to mark new tests"""
        print('\n\n.................................')
        print('.... Test create() w/ params ....')
        print('..... For BHCommand Class .....')
        print('.................................\n\n')
        storage.delete_all()
        print('...creating new Place object: ', end='')
        cls.cli = BHCommand()
        cls.cli.do_create('Employee '
                          'department_id="0001" '
                          'first_name="Bob" '
                          'last_name="Nil" '
                          'email="abc@example.com" '
                          'description="i am a test" '
        print('')
        cls.storage_objs = storage.all()
        for v in cls.storage_objs.values():
            cls.obj = v

    def setUp(self):
        """initializes new BHCommand instance for each test"""
        self.CLI = TestBHcmdCreate.cli
        self.obj = TestBHcmdCreate.obj

    def test_instantiation(self):
        """... checks if BHCommand CLI Object is properly instantiated"""
        self.assertIsInstance(self.CLI, BHCommand)

    def test_create(self):
        """... tests creation of class Department with attributes"""
        self.assertIsInstance(self.obj, CNC['Employee'])

    def test_attr_first_name(self):
        """... checks if proper parameter for first_name was created"""
        actual = self.obj.first_name
        expected = "Bob"
        self.assertEqual(expected, actual)

    def test_attr_department_id(self):
        """... checks if proper parameter for department_id was created"""
        actual = self.obj.department_id
        expected = "0001"
        self.assertEqual(expected, actual)

    def test_attr_last_name(self):
        """... checks if proper parameter for last_name was created"""
        actual = self.obj.last_name
        expected = 'Nil'
        self.assertEqual(expected, actual)

    def test_attr_email(self):
        """... checks if proper parameter for email was created"""
        actual = self.obj.email
        expected = "abc@example.com"
        self.assertEqual(expected, actual)

    def test_attr_description(self):
        """... checks if proper parameter for description was created"""
        actual = self.obj.description
        expected = "i am a test"
        self.assertEqual(expected, actual)

@unittest.skipIf(STORAGE_TYPE != 'db', 'DB tests made for DBStorage not FS')
class TestBHcmdCreateDB(unittest.TestCase):
    """testing instantiation of CLI & create()
    for Classes Department, User, Employee, Todo"""

    @classmethod
    def setUpClass(cls):
        """init: prints output to mark new tests"""
        print('\n\n.................................')
        print('.... Test create() w/ params ....')
        print('... Department, User, Employee, Todo ....')
        print('.................................\n\n')
        storage.delete_all()
        print('...creating new Employee object: ', end='')
        cls.cli = BHCommand()
        CLI = cls.cli
        with redirect_streams() as (std_out, std_err):
            CLI.do_create('Department '
                          'name="Accounting" '
                          'description="i am a test" ')
        cls.test_department_id = std_out.getvalue()[:-1]
        with redirect_streams() as (std_out, std_err):
            CLI.do_create('Employee '
                          'email="abc@gmail.com" '
                          'department_id="0001" '
                          'first_name="a_first_name" '
                          'last_name="a_last_name" '
                          'description="i am a test" ')
        cls.test_employee_id = std_out.getvalue()[:-1]
        with redirect_streams() as (std_out, std_err):
            CLI.do_create('User '
                          'department_id="{}" '
                          'last_name="b_last_name" '
                          'first_name="b_first_name" '
                          'email="string" '
                          'password="apass" '.format(cls.test_department_id))
        cls.test_user_id = std_out.getvalue()[:-1]
        with redirect_streams() as (std_out, std_err):
            CLI.do_create('Employee '
                          'department_id="{}" '
                          'last_name="A_Guy" '
                          'first_name="A_f" '
                          'email="a@b.com" '
                          'description="aaa" '.format(cls.test_department_id))
        cls.test_employee_id = std_out.getvalue()[:-1]
        print('... done creating')
        storage_objs = storage.all()
        for v in storage_objs.values():
            if v.id == cls.test_employee_id:
                cls.obj = v

    def setUp(self):
        """initializes new BHCommand instance for each test"""
        self.CLI = TestBHcmdCreateDB.cli
        self.obj = TestBHcmdCreateDB.obj
        self.department_id = TestBHcmdCreateDB.test_department_id
        self.user_id = TestBHcmdCreateDB.test_user_id
        self.employee_id = TestBHcmdCreateDB.test_Epmployee_id

    def test_instantiation(self):
        """... checks if BHCommand CLI Object is properly instantiated"""
        self.assertIsInstance(self.CLI, BHCommand)

    def test_create(self):
        """... tests creation of class Department with attributes"""
        self.assertIsInstance(self.obj, CNC['Employee'])

    def test_attr_user_id(self):
        """... checks if proper parameter for user_id was created"""
        actual = self.obj.user_id
        expected = self.user_id
        self.assertEqual(expected, actual)

    def test_attr_department_id(self):
        """... checks if proper parameter for department_id was created"""
        actual = self.obj.department_id
        expected = self.department_id
        self.assertEqual(expected, actual)

    def test_attr_first_name(self):
        """... checks if proper parameter for name was created"""
        actual = self.obj.first_name
        expected = 'a_first_name'
        self.assertEqual(expected, actual)

    def test_attr_last_name(self):
        """... checks if proper parameter for last_name was created"""
        actual = self.obj.last_name
        expected = "a_last_name"
        self.assertEqual(expected, actual)
        self.assertIs(type(actual), str)

    def test_attr_email(self):
        """... checks if proper parameter for email was created"""
        actual = self.obj.email
        expected = "abc@gmail.com"
        self.assertEqual(expected, actual)
        self.assertIs(type(actual), str)

    def test_attr_description(self):
        """... checks if proper parameter for description was created"""
        actual = self.obj.description
        expected = "i am a test"
        self.assertEqual(expected, actual)
        self.assertIs(type(actual), str)


@unittest.skipIf(STORAGE_TYPE == 'db', 'not designed for DB yet')
class TestHBNBcmdErr(unittest.TestCase):
    """Tests create method -> attempts to throw errors with strange params"""

    @classmethod
    def setUpClass(cls):
        """init: prints output to mark new tests"""
        print('\n\n.................................')
        print('... Can I Kill your program ? ...')
        print('..... For BHCommand Class .....')
        print('.................................\n\n')
        storage.delete_all()
        print('...creating new Employee object: ', end='')
        cls.cli = BHCommand()
        cls.cli.do_create('Employee '
                          'department_id="00""""01" '
                          'last_name="My____little____boy" '
                          'first_name=1 '
                          'email=2.0 '
                          'description="\'\'"HEy-O"\'\'" ')
        print('')
        storage_objs = storage.all()
        for v in storage_objs.values():
            cls.obj = v

    def setUp(self):
        """initializes new BHCommand instance for each test"""
        self.CLI = TestBHcmdErr.cli
        self.obj = TestBHcmdErr.obj

    def test_create(self):
        """... tests creation of class Department with attributes"""
        self.assertIsInstance(self.obj, CNC['Employee'])

    def test_attr_department_id(self):
        """... checks if proper parameter for department_id was created"""
        actual = self.obj.department_id
        expected = '00""""01'
        self.assertEqual(expected, actual)

    def test_attr_last_name(self):
        """... checks if proper parameter for last name was created"""
        actual = self.obj.last_name
        expected = 'My    little    boy'
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main
