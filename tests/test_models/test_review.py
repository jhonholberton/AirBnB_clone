#!/usr/bin/python3
"""Modulo de pruebas para la clase Review"""
from models.base_model import BaseModel
from models.review import Review
import unittest
import inspect
import time
from datetime import datetime
from unittest import mock
import models


class TestReview(unittest.TestCase):
    """Probar la clase Review"""

    def test_subclass(self):
        """Prueba si Review es una subclase de BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_place_id(self):
        """Atributo de clase y si esta vacio"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")

    def test_user_id(self):
        """Atributo de clase y si esta vacia la cadena"""
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")

    def test_text(self):
        """Atributo de clase y si esta vacia la cadena"""
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")

    def test_str(self):
        """prueba que el método str tiene la salida correcta"""
        review = Review()
        string = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(string, str(review))

    def test_to_dict_values(self):
        """valores en dict devueltos desde to_dict sean correctos"""
        formato = "%Y-%m-%dT%H:%M:%S.%f"
        review = Review()
        di = review.to_dict()
        self.assertEqual(di["__class__"], "Review")
        self.assertEqual(type(di["created_at"]), str)
        self.assertEqual(type(di["updated_at"]), str)
        self.assertEqual(di["created_at"], review.created_at.strftime(formato))
        self.assertEqual(di["updated_at"], review.updated_at.strftime(formato))

    def test_to_dict_creates_dict(self):
        """to_dict crea un diccionario con los atributos adecuados"""
        review = Review()
        diccionario = review.to_dict()
        self.assertEqual(type(diccionario), dict)
        for Atributo in review.__dict__:
            self.assertTrue(Atributo in diccionario)
            self.assertTrue("__class__" in diccionario)

    def test_instancia(self):
        """Prueba la creación de instancias de la clase Review"""

        review = Review()
        self.assertEqual(str(type(review)), "<class 'models.review.Review'>")
        self.assertIsInstance(review, Review)
        self.assertTrue(issubclass(type(review), BaseModel))


if __name__ == '__main__':
    unittest.main()
