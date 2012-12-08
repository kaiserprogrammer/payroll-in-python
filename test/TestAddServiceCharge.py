from memory_db import MemoryDB
from change_union_member import ChangeUnionMember
from add_salaried_employee import AddSalariedEmployee
from add_service_charge import AddServiceCharge
from datetime import date

def test_adding_a_service_charge_to_a_member():
    db = MemoryDB()
    empId = AddSalariedEmployee("Bill", "Home", 1000, db).execute()
    e = db.get_employee(empId)

    ChangeUnionMember(empId, 10.0, db).execute()

    sct = AddServiceCharge(e.memberId, date.today(), 12.95, db)
    sct.execute()

    sc = e.affiliation.get_service_charge(date.today())
    assert sc.charge == 12.95
    assert sc.date == date.today()
