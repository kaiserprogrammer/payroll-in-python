from change_affiliation import ChangeAffiliation
from no_affiliation import NoAffiliation

class ChangeUnaffiliated(ChangeAffiliation):
    def __init__(self, empId, db):
        ChangeAffiliation.__init__(self, empId, db)

    def record_membership(self, employee):
        self.db.remove_union_member(employee.memberId)

    def make_affiliation(self, employee):
        employee.affiliation = NoAffiliation()
