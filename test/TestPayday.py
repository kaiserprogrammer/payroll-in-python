from memory_db import MemoryDB
from add_salaried_employee import AddSalariedEmployee
from add_hourly_employee import AddHourlyEmployee
from add_commissioned_employee import AddCommissionedEmployee
from add_time_card import AddTimeCard
from add_sales_receipt import AddSalesReceipt
from change_union_member import ChangeUnionMember
from add_service_charge import AddServiceCharge
from payday import Payday
import datetime

def test_paying_a_single_salaried_employee():
    db = MemoryDB()
    t = AddSalariedEmployee("Bill", "Home", 1000.0, db)
    empId = t.execute()

    pay_date = datetime.date(2001, 11, 30)
    pt = Payday(pay_date, db)
    pt.execute()

    pc = pt.get_paycheck(empId)
    assert pc.pay_date == datetime.date(2001, 11, 30)
    assert pc.gross_pay == 1000.0
    assert pc.deductions == 0
    assert pc.net_pay == 1000.0
    assert pc.disposition == "Hold"

def test_not_paying_a_salaried_employee_on_wrong_date():
    db = MemoryDB()
    t = AddSalariedEmployee("Bill", "Home", 1000.0, db)
    empId = t.execute()

    pay_date = datetime.date(2001, 11, 29)
    pt = Payday(pay_date, db)
    pt.execute()

    try:
        pt.get_paycheck(empId)
        raise "paycheck found on wrong date"
    except KeyError:
        pass

def test_paying_nothing_to_an_hourly_employee_with_no_timecards():
    db = MemoryDB()
    empId =  AddHourlyEmployee("Bob", "Home", 15.25, db).execute()
    pay_date = datetime.date(2001, 11, 9)
    pt = Payday(pay_date, db)
    pt.execute()

    pc = pt.get_paycheck(empId)
    assert pc.pay_date == datetime.date(2001, 11, 9)
    assert pc.gross_pay == 0
    assert pc.deductions == 0
    assert pc.net_pay == 0

def test_paying_an_hourly_employee_with_one_timecard():
    db = MemoryDB()
    empId =  AddHourlyEmployee("Bob", "Home", 15.25, db).execute()
    pay_date = datetime.date(2001, 11, 9)
    AddTimeCard(empId, pay_date, 2.0, db).execute()
    pt = Payday(pay_date, db)
    pt.execute()

    pc = pt.get_paycheck(empId)
    assert pc.pay_date == datetime.date(2001, 11, 9)
    assert pc.gross_pay == 30.5
    assert pc.deductions == 0
    assert pc.net_pay == 30.5

def test_paying_an_hourly_employee_for_over_time():
    db = MemoryDB()
    empId =  AddHourlyEmployee("Bob", "Home", 10.0, db).execute()
    pay_date = datetime.date(2001, 11, 9)
    AddTimeCard(empId, pay_date, 10.0, db).execute()
    pt = Payday(pay_date, db)
    pt.execute()

    pc = pt.get_paycheck(empId)
    assert pc.pay_date == datetime.date(2001, 11, 9)
    print pc.gross_pay
    assert pc.gross_pay == 110
    assert pc.deductions == 0
    assert pc.net_pay == 110

def test_not_paying_an_hourly_employee_on_wrong_date():
    db = MemoryDB()
    empId =  AddHourlyEmployee("Bob", "Home", 15.25, db).execute()
    pay_date = datetime.date(2001, 11, 29)
    pt = Payday(pay_date, db)
    pt.execute()

    try:
        pt.get_paycheck(empId)
        raise "pay on wrong date"
    except KeyError:
        pass

def test_paying_an_hourly_employee_with_two_timecards():
    db = MemoryDB()
    empId =  AddHourlyEmployee("Bob", "Home", 15.25, db).execute()
    pay_date = datetime.date(2001, 11, 9)
    AddTimeCard(empId, pay_date, 2.0, db).execute()
    AddTimeCard(empId, datetime.date(2001, 11, 2), 2.0, db).execute()
    pt = Payday(pay_date, db)
    pt.execute()

    pc = pt.get_paycheck(empId)
    assert pc.pay_date == datetime.date(2001, 11, 9)
    assert pc.gross_pay == 61
    assert pc.deductions == 0
    assert pc.net_pay == 61

def test_paying_an_hourly_employee_only_in_one_period():
    db = MemoryDB()
    empId =  AddHourlyEmployee("Bob", "Home", 15.25, db).execute()
    pay_date = datetime.date(2001, 11, 9)
    AddTimeCard(empId, pay_date, 2.0, db).execute()
    AddTimeCard(empId, datetime.date(2001, 11, 1), 2.0, db).execute()
    pt = Payday(pay_date, db)
    pt.execute()

    pc = pt.get_paycheck(empId)
    assert pc.pay_date == datetime.date(2001, 11, 9)
    assert pc.gross_pay == 30.5
    assert pc.deductions == 0
    assert pc.net_pay == 30.5

def test_paying_a_commissioned_employee_with_no_sales():
    db = MemoryDB()
    empId = AddCommissionedEmployee("Bob", "Home", 10, 1000, db).execute()

    pay_date = datetime.date(2001, 11, 16)
    pt = Payday(pay_date, db)
    pt.execute()

    pc = pt.get_paycheck(empId)
    assert pc.pay_date == datetime.date(2001, 11, 16)
    assert pc.gross_pay == 1000
    assert pc.deductions == 0
    assert pc.net_pay == 1000

def test_paying_a_commissioned_employee_only_for_one_period():
    db = MemoryDB()
    empId = AddCommissionedEmployee("Bob", "Home", 10, 1000, db).execute()

    pay_date = datetime.date(2001, 11, 16)
    AddSalesReceipt(empId, pay_date, 500, db).execute()
    AddSalesReceipt(empId, datetime.date(2001, 11, 16-14), 500, db).execute()
    AddSalesReceipt(empId, datetime.date(2001, 11, 16+1), 500, db).execute()
    pt = Payday(pay_date, db)
    pt.execute()

    pc = pt.get_paycheck(empId)
    assert pc.pay_date == datetime.date(2001, 11, 16)
    print pc.gross_pay
    assert pc.gross_pay == 1050
    assert pc.deductions == 0
    assert pc.net_pay == 1050

def test_not_paying_a_commissioned_employee_on_wrong_date():
    db = MemoryDB()
    empId = AddCommissionedEmployee("Bob", "Home", 10, 1000, db).execute()

    pay_date = datetime.date(2001, 11, 23)
    pt = Payday(pay_date, db)
    pt.execute()

    try:
        pt.get_paycheck(empId)
        raise "pay on wrong date"
    except KeyError:
        pass

def test_deducting_service_charges():
    db = MemoryDB()
    empId = AddCommissionedEmployee("Bob", "Home", 10, 1000, db).execute()
    ChangeUnionMember(empId, 99.42, db).execute()
    mId = db.get_employee(empId).memberId

    pay_date = datetime.date(2001, 11, 16)
    AddServiceCharge(mId, pay_date, 10, db).execute()
    pt = Payday(pay_date, db)
    pt.execute()

    pc = pt.get_paycheck(empId)
    assert pc.gross_pay == 1000
    print pc.deductions
    assert pc.deductions == 109.42
    assert pc.net_pay == 1000 - 109.42

def test_deducting_service_charges_over_multiple_pay_periods():
    db = MemoryDB()
    empId = AddCommissionedEmployee("Bob", "Home", 10, 1000, db).execute()
    ChangeUnionMember(empId, 99.42, db).execute()
    mId = db.get_employee(empId).memberId

    pay_date = datetime.date(2001, 11, 16)
    early_date = pay_date.replace(day=16-14)
    late_date = pay_date.replace(day=16+1)
    AddServiceCharge(mId, pay_date, 10, db).execute()
    AddServiceCharge(mId, early_date, 10, db).execute()
    AddServiceCharge(mId, late_date, 10, db).execute()
    pt = Payday(pay_date, db)
    pt.execute()

    pc = pt.get_paycheck(empId)
    assert pc.gross_pay == 1000
    print pc.deductions
    assert pc.deductions == 109.42
    assert pc.net_pay == 1000 - 109.42
