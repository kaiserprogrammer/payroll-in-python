from memory_db import MemoryDB
from add_hourly_employee import AddHourlyEmployee
from delete_employee import DeleteEmployee


def test_deleting_an_employee():
    db = MemoryDB()
    empId = AddHourlyEmployee("Jim", "Home", 32.25, db).execute()

    db.get_employee(empId)

    dt = DeleteEmployee(empId, db)
    dt.execute()

    try:
        db.get_employee(empId)
        raise "employee not deleted"
    except KeyError:
        pass
