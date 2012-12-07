from memory_db import MemoryDB
from add_hourly_employee import AddHourlyEmployee
from change_union_member import ChangeUnionMember
from change_unaffiliated import ChangeUnaffiliated
from no_affiliation import NoAffiliation

def test_removing_affiliations_from_employee():
    db = MemoryDB()
    empId = AddHourlyEmployee("Jim", "Home", 12.25, db).execute()

    ChangeUnionMember(empId, 99.42, db).execute()

    cut = ChangeUnaffiliated(empId, db)
    cut.execute()

    e = db.get_employee(empId)
    assert isinstance(e.affiliation, NoAffiliation)
    try:
        db.get_union_member(e.memberId)
        raise "member not deleted"
    except KeyError:
        pass
