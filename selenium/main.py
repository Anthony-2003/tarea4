import os
import unittest
from lib2to3.pgen2 import driver

import HtmlTestRunner
from selenium import webdriver
from PageObject.LoginPage import LoginPage
from TestCase.EventTest import EventTest
from TestCase.PublicationTest import PublicationTest
from TestCase.RecoveryUserTest import RecoveryUserTest
from TestCase.loginTest import TestLogin
from TestCase.RegisterTest import RegisterTest

# Test exitoso inicio de sesion
"""test_login = TestLogin()
test_login.setUp()
test_login.test_successful_login()
test_login.tearDown()"""

# Test fallido inicio de sesion
"""test_login = TestLogin()
test_login.setUp()
test_login.test_failed_login()
test_login.tearDown()"""

#Test registro exitoso
"""test_register = RegisterTest()
test_register.setUp()
test_register.test_successful_register()
test_register.tearDown()"""

#Test registro con campos vacios
"""test_register = RegisterTest()
test_register.setUp()
test_register.test_empty_field()
test_register.tearDown()"""

#Test mismo usuario
"""test_register = RegisterTest()
test_register.setUp()
test_register.test_same_user()
test_register.tearDown()"""

#test exitoso para recuperar user
"""test_recovery = RecoveryUserTest()
test_recovery.setUp()
test_recovery.test_successful_recovery()
test_recovery.tearDown()"""

#test fallido para recuperar user
"""test_recovery = RecoveryUserTest()
test_recovery.setUp()
test_recovery.test_failed_recovery()
test_recovery.tearDown()"""

#test de evento exitoso
"""test_event = EventTest()
test_event.setUp()
test_event.create_event_succesfully()
test_event.tearDown()"""

#test de evento fallido
"""test_event = EventTest()
test_event.setUp()
test_event.create_event_failed()
test_event.tearDown()"""

#test de evento con fecha pasada
"""test_event = EventTest()
test_event.setUp()
test_event.create_event_past_date()
test_event.tearDown()"""

#test de publicacion exitosa
"""test_publicacion = PublicationTest()
test_publicacion.setUp()
test_publicacion.test_publication_succesfully()
test_publicacion.tearDown()"""

#test de publicacion fallida
"""test_publicacion = PublicationTest()
test_publicacion.setUp()
test_publicacion.test_publication_failed()
test_publicacion.tearDown()"""

suite = unittest.TestSuite()

# Agregar casos de prueba a la suite
suite.addTest(unittest.makeSuite(EventTest))
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(PublicationTest))
suite.addTest(unittest.makeSuite(RecoveryUserTest))
suite.addTest(unittest.makeSuite(RegisterTest))

# Crear el informe HTML
report_dir = "reports"  # Directorio donde se guardará el informe HTML
os.makedirs(report_dir, exist_ok=True)  # Crear el directorio si no existe

report_file = os.path.join(report_dir, "test_report.html")

with open(report_file, "w") as f:
    runner = HtmlTestRunner.HTMLTestRunner(
        stream=f,
        report_title="Test Report",
        descriptions="Test Results"
    )
    # Ejecutar la suite de pruebas y generar el informe HTML
    runner.run(suite)

# Cerrar el WebDriver al finalizar
driver.quit()





