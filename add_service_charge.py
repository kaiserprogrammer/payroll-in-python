from service_charge import ServiceCharge

class AddServiceCharge(object):
    def __init__(self, memberId, date, amount, db):
        self.memberId = memberId
        self.date = date
        self.amount = amount
        self.db = db

    def execute(self):
        sc = ServiceCharge(self.date, self.amount)
        e = self.db.get_union_member(self.memberId)
        e.affiliation.add_service_charge(self.date, sc)
