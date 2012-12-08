from memory_db import MemoryDB
from add_hourly_employee import AddHourlyEmployee
from change_union_member import ChangeUnionMember

def test_changing_an_employee_to_be_in_a_union_affiliation():
    db = MemoryDB()
    empId = AddHourlyEmployee("Jim", "Home", 12.25, db).execute()

    cut = ChangeUnionMember(empId, 99.42, db)
    cut.execute()

    e = db.get_employee(empId)

    af = e.affiliation
    assert af is not None
    assert af.dues == 99.42

    member = db.get_union_member(e.memberId)
    assert member is e
