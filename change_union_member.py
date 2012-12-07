from change_affiliation import ChangeAffiliation
from union_affiliation import UnionAffiliation

class ChangeUnionMember(ChangeAffiliation):
    def __init__(self, empId, dues, db):
        ChangeAffiliation.__init__(self, empId, db)
        self.dues = dues

    def record_membership(self, employee):
        self.db.add_union_member(employee)

    def make_affiliation(self, employee):
        employee.affiliation = UnionAffiliation(self.dues)
