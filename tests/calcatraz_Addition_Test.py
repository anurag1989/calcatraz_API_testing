__author__ = 'Anurag'

from calcatraz_action.calcatraz_Addition import *
from nose.tools import assert_equal
from datetime import datetime
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises
from nose.plugins.attrib import attr

class Calcatraz_Addition_Test(object):


    @attr(runwith='Positive_Tests')
    def test_addition_two_integer(self):
        calcatraz_add= Calcatraz_Addition()
        print calcatraz_add.request(4,5)
        assert_equal(int(calcatraz_add.request(5,6)),11,"Addition of %d and %s gave %d instead of %d" %(5,6,int(calcatraz_add.request(5,6)),11))

    @attr(runwith='Tests')
    def test_addition_negative_number(self):
        calcatraz_add= Calcatraz_Addition()
        assert_equal(calcatraz_add.request(-5,-6),-11,"Addition of %d and %d gave Blank instead of %d" %(-5,-6,-11))

    @attr(runwith='Positive_Tests')
    def test_addition_postive_negative(self):
        calcatraz_add= Calcatraz_Addition()
        assert_equal(int(calcatraz_add.request(8,-5)),3,"Addition of 8 and -5 gave %s instead of %d" %(str(calcatraz_add.request(-5,-6)),3))

    @attr(runwith='Positive_Tests')
    def test_addition_positive_zero(self):
        calcatraz_add= Calcatraz_Addition()
        assert_equal(int(calcatraz_add.request(6,0)),6,"Addition of %d and %d gave %d instead of %d" %(6,0,int(calcatraz_add.request(6,0)),6))

    @attr(runwith='Positive_Tests')
    def test_addition_negative_zero(self):
        calcatraz_add= Calcatraz_Addition()
        assert_equal(calcatraz_add.request(-6,0),-6,"Addition of %d and %d gave blank instead of %d" %(-6,0,-6))

    @attr(runwith='Positive_Tests')
    def test_addition_long_small(self):
        calcatraz_add= Calcatraz_Addition()
        assert_equal(str(calcatraz_add.request(2165496761454353,5)).lower().replace("0e+15",""),str(2.16550),"Addition of small number and small number is not matching")

    @attr(runwith='Positive_Tests')
    def test_addition_long_long(self):
        calcatraz_add= Calcatraz_Addition()
        assert_equal(calcatraz_add.request(21653296653321,2165496798766).lower(),str(2.38188e+13),"Addition of two long value is not matching with expected value")

    @attr(runwith='Positive_Tests')
    def test_addition_float_integer(self):
        calcatraz_add= Calcatraz_Addition()
        assert_equal(str(calcatraz_add.request(2.75,6)),'8.75',"Addition of %f and %f gave %s instead of %f" %(2.75,6,calcatraz_add.request(2.75,6),8.75))

    @attr(runwith='Positive_Tests')
    def test_addition_float_float(self):
        calcatraz_add= Calcatraz_Addition()
        assert_equal(calcatraz_add.request(2.75,2.05),str(4.8),"Addition of %f and %f gave %s instead of %f" %(2.75,2.05,calcatraz_add.request(2.75,2.05),4.8))

    @attr(runwith='Positive_Tests')
    def test_success_status_code(self):
        calcatraz_add= Calcatraz_Addition()
        assert_equal(calcatraz_add.response_status(5,10),200,"We are not getting 200 in status code")

    # Negative test Cases
    @attr(runwith='Negative_Tests')
    def test_addition_string_string(self):
        calcatraz_add= Calcatraz_Addition()
        assert_equal(calcatraz_add.request("Testing","Addition"),"TestingAddition","Addition of two String is giving error")

    @attr(runwith='Negative_Tests')
    def test_passing_number_as_string(self):
        calcatraz_add= Calcatraz_Addition()
        assert_equal(calcatraz_add.request("12270","6"),"12276","Addition of of number as string is not matching with expected result")

    @attr(runwith='Negative_Tests')
    def test_500Error(self):
        calcatraz_add= Calcatraz_Addition()
        assert_equal(calcatraz_add.request("Testing","Addition"),"Found 500 internal server error","We did'nt found 500 Internal server error")

    @attr(runwith='Negative_Tests')
    def test_400Error(self):
        calcatraz_add= Calcatraz_Addition()
        assert_equal(calcatraz_add.response_status("Testing","Addition"),"Found 400 HTTP ERROR")



    #performance testing

    @attr(runwith='Performance_Tests')
    def test_response_time(self):
        calcatraz_add= Calcatraz_Addition()
        date1 = datetime.strptime(str(calcatraz_add.response_time(4,8)), '%H:%M:%S.%f')
        date2 = datetime.strptime("00:00:01.000",'%H:%M:%S.%f')
        assert(date1 < date2)

    @attr(runwith='Performance_Tests')
    def test_responsetime_addition_Long_number(self):
        calcatraz_add= Calcatraz_Addition()
        date1 = datetime.strptime(str(calcatraz_add.response_time(42543543345435345,4598754735987857584)), '%H:%M:%S.%f')
        date2 = datetime.strptime("00:00:01.000",'%H:%M:%S.%f')
        assert(date1 < date2)

    @attr(runwith='Performance_Tests')
    def test_responsetime_on_concurrent_request(self):
        calcatraz_add= Calcatraz_Addition()
        count = 0
        while count < 10:
              # time.sleep(1)
              count += 1
              date1 = datetime.strptime(str(calcatraz_add.response_time(423+count,143+count)), '%H:%M:%S.%f')
              date2 = datetime.strptime("00:00:01.000",'%H:%M:%S.%f')
              assert (date1 < date2)


