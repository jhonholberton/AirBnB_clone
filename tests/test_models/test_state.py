#!/usr/bin/python3
"""Modulo de pruebas para la clase State"""
from models.base_model import BaseModel
from models.state import State
import unittest
import inspect
import time
from datetime import datetime
from unittest import mock
import models


class TestState(unittest.TestCase):
    """Probar la clase State"""

    def test_sub_class(self):
        """
            probar si la clase de state es una subclase del BaseModel
        """
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertFalse(hasattr(state, "update_at"))

    def test_name(self):
        """
            Atributo de clase y si esta vacia la cadena
        """
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_to_dictstate_create(self):
        """
            El método test to_dict crea un diccionario
            con los atributos adecuados
        """
        state = State()
        diccionario = state.to_dict()
        self.assertEqual(type(diccionario), dict)
        for atributo in state.__dict__:
            self.assertTrue(atributo in diccionario)
            self.assertTrue("__class__" in diccionario)

    def test_str(self):
        """prueba que el método str tiene la salida correcta"""
        state = State()
        string = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(string, str(state))

    def test_to_valores_dicci(self):
        """los valores en dict devueltos desde to_dict sean correctos"""
        formato = "%Y-%m-%dT%H:%M:%S.%f"
        state = State()
        di = state.to_dict()
        self.assertEqual(di["__class__"], "State")
        self.assertEqual(type(di["created_at"]), str)
        self.assertEqual(type(di["updated_at"]), str)
        self.assertEqual(di["created_at"], state.created_at.strftime(formato))
        self.assertEqual(di["updated_at"], state.updated_at.strftime(formato))

    def test_instancia(self):
        """Prueba la instanciación de la clase State"""
        state = State()
        self.assertEqual(str(type(state)), "<class 'models.state.State'>")
        self.assertIsInstance(state, State)
        self.assertTrue(issubclass(type(state), BaseModel))


if __name__ == '__main__':
    unittest.main()
