import unittest
import os
import csv
import time
from Model import HTMLReport
# from Model.Result import Report
from Model.HTMLResult import Report
from TestSuites import __init__


__author__ = 'kzhu'


def load_suite(modules_to_test):
    suite = unittest.TestSuite()
    for module in map(__import__,modules_to_test):
        suite.addTest(unittest.findTestCases(module))
    return suite

def load_tests(modules_to_test):
    suites = [unittest.defaultTestLoader.loadTestsFromName(module_name) for module_name in modules_to_test]
    testSuite = unittest.TestSuite(suites)
    return testSuite

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    suites = []
    with open(BASE_DIR+'/config.csv') as configfile:
        reader = csv.DictReader(configfile)
        for row in reader:
            sign = row['ToBeExecuted'].lower()
            if sign == 'yes':
                suites.append(row['TestSuite'])

    suite = load_tests(suites)

    unittest.TextTestRunner(verbosity=1).run(suite)

    today = time.strftime("%Y%m%d")
    filename = BASE_DIR+'/Results/testing_report_'+today+'.html'
    fp = file(filename,'wb')
    report = Report(stream=fp,
                    title="Testing Report",
                    description='This demonstrates the report output by HTMLReport.'
                    )
    report.generateReport(__init__.result)

    # today = time.strftime("%Y%m%d")
    # fp = file(BASE_DIR+'/Results/testing_report_'+today+'.html','wb')
    # runner = HTMLReport.HTMLTestRunner(
    #     stream = fp,
    #     title ='Testing Report',
    #     description='This demonstrates the report output by HTMLTestRunner.'
    # )
    # runner.run(suite)



