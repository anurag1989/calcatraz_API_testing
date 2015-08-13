__author__ = 'Anurag'

from calcatraz_action.calcatraz_Addition import *
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises
from nose.plugins.attrib import attr

class Calcatraz_Addition_Test(object):


    def setUp(self):
        calcatraz_add=Calcatraz_Addition()


    def teardown(self):
        """This method is run once after _each_ test method is executed"""

    @attr(runwith='Positive_Tests')
    def test_addition_two_integer(self):
        calcatraz_add= Calcatraz_Addition()
        print calcatraz_add.request(4,5)
        assert_equal(calcatraz_add.request(5,6),11,"Addition of %d and %d gave %d instead of %d" %(5,6,calcatraz_add.request(5,6),11))

    @attr(runwith='Positive_Tests')
    def test_addition_negative_number(self):
        calcatraz_add= Calcatraz_Addition()
        assert_equal(calcatraz_add.request(-5,-6),-11,"Addition of two negative number is not matching with expected result")

    @attr(runwith='Positive_Tests')
    def test_addition_postive_negative(self):
        calcatraz_add= Calcatraz_Addition()
        assert_equal(calcatraz_add.request(6,-5),1,"Addition of one positive and one negative number is not matching with expected result")

    @attr(runwith='Positive_Tests')
    def test_addition_positive_zero(self):
        calcatraz_add= Calcatraz_Addition()
        assert_equal(calcatraz_add.request(6,0),6,"Addition of one positive and zero  is not matching with expected results")

    @attr(runwith='Positive_Tests')
    def test_addition_negative_zero(self):
        calcatraz_add= Calcatraz_Addition()
        assert_equal(calcatraz_add.request(-6,0),-6,"Addition of one negative and zero  is not matching with expected results")

    @attr(runwith='Positive_Tests')
    def test_addition_long_small(self):
        calcatraz_add= Calcatraz_Addition()
        assert_equal(calcatraz_add.request(2165496761454353,5),2165496761454358,"Addition of one positive and one negative number is not matching with expected results")

    @attr(runwith='Positive_Tests')
    def test_addition_long_long(self):
        calcatraz_add= Calcatraz_Addition()
        assert_equal(calcatraz_add.request(2165496761454353321,216549676145435398766),2.1872E+20,"Addition of one negative and zero  is not matching with expected results")

    @attr(runwith='Positive_Tests')
    def test_addition_float_integer(self):
        calcatraz_add= Calcatraz_Addition()
        assert_equal(calcatraz_add.request(2.75,6),8.75,"Addition of one negative and zero  is not matching with expected results")

    @attr(runwith='Positive_Tests')
    def test_addition_float_float(self):
        calcatraz_add= Calcatraz_Addition()
        assert_equal(calcatraz_add.request(2.75,2.05),4.80,"Addition of one negative and zero  is not matching with expected results")

    # Negative test Cases
    @attr(runwith='Negative_Tests')
    def test_addition_string_string(self):
        calcatraz_add= Calcatraz_Addition()
        assert_equal(calcatraz_add.request("Testing","Addition"),"Testing Addition","Addition of Two Integers  is not matching with expected results")

    @attr(runwith='Negative_Tests')
    def test_passing_number_as_string(self):
        calcatraz_add= Calcatraz_Addition()
        assert_equal(calcatraz_add.request("129","6"),"Not able to do addition","There should be message -Not able to do addition- if we pass number as string")

    @attr(runwith='Negative_Tests')
    # def test_500Error(self):
    #     calcatraz_add= Calcatraz_Addition()
    #     assert_equal(calcatraz_add.request("Testing","Addition"),"Found 500 internal server error","We did'nt found 500 Internal server error")

    @attr(runwith='Negative_Tests')
    # def test_400Error(self):
    #     calcatraz_add= Calcatraz_Addition()
    #     assert_equal(calcatraz_add.request("!@","!@"),"Found 404 Status code")


    #performance testing
    @attr(runwith='Performance_Tests')
    # def test_response_time(self):
    #     calcatraz_add= Calcatraz_Addition()
    #     assert_equal(calcatraz_add.request("Testing","Addition"),"Testing Addition","Addition of Two Integers  is not matching with expected results")

    @attr(runwith='Performance_Tests')
    # def test_responsetime_addition_Long_number(self):
    #     calcatraz_add= Calcatraz_Addition()

    @attr(runwith='Performance_Tests')
    def test_responsetime_on_concurrent_request(self):
        calcatraz_add= Calcatraz_Addition()


