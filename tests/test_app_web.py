import unittest
import importlib.util
import sys
import os

class TestAppWeb(unittest.TestCase):

    def test_app_web_imports(self):
        """Check that app_web.py can be imported without errors"""
        #Get the path to app_web.py relative to this test file
        file_path = os.path.join(os.path.dirname(__file__), "../app_web.py")
        #Load the module specification from the file
        spec = importlib.util.spec_from_file_location("app_web", file_path)
        #Create a module object from the specification
        module = importlib.util.module_from_spec(spec)
        #Add the module to sys.modules so Python recognizes it
        sys.modules["app_web"] = module
        #Execute the module code to import it
        spec.loader.exec_module(module)
        #Check that the module has Streamlit imported as 'st'
        self.assertTrue(hasattr(module, "st"), "Streamlit should be imported")

if __name__ == "__main__":
    #Run all unit tests in this file
    unittest.main()
