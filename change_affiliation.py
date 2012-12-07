from change_employee import ChangeEmployee

class ChangeAffiliation(ChangeEmployee):
    def __init__(self, empId, db):
        ChangeEmployee.__init__(self, empId, db)

    def change(self, e):
        self.record_membership(e)
        self.make_affiliation(e)
