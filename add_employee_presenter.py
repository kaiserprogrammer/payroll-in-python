class AddEmployeePresenter(object):
    def __init__(self, view, container, db):
        self._name = None
        self._address = None
        self._hourly = None
        self._hourly_rate = None
        self._commissioned = None
        self._baseRate = None
        self._commission = None
        self._salary = None
        self._salaried = None
        self.view = view

    def all_information_is_collected(self):
        result = self.name and self.address
        result = result and self.hourly and self.hourly_rate
        result = result or self.commissioned and self.baseRate and self.commission
        result = result or self.salaried and self.salary
        return result

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value
        self.update_view()

    name = property(get_name, set_name)

    def get_address(self):
        return self._address

    def set_address(self, value):
        self._address = value
        self.update_view()

    address = property(get_address, set_address)

    def get_hourly(self):
        return self._hourly

    def set_hourly(self, value):
        self._hourly = value
        self.update_view()

    hourly = property(get_hourly, set_hourly)

    def get_hourly_rate(self):
        return self._hourly_rate

    def set_hourly_rate(self, value):
        self._hourly_rate = value
        self.update_view()

    hourly_rate = property(get_hourly_rate, set_hourly_rate)

    def get_commissioned(self):
        return self._commissioned

    def set_commissioned(self, value):
        self._commissioned = value
        self.update_view()

    commissioned = property(get_commissioned, set_commissioned)

    def get_baseRate(self):
        return self._baseRate

    def set_baseRate(self, value):
        self._baseRate = value
        self.update_view()

    baseRate = property(get_baseRate, set_baseRate)

    def get_commission(self):
        return self._commission

    def set_commission(self, value):
        self._commission = value
        self.update_view()

    commission = property(get_commission, set_commission)

    def get_salary(self):
        return self._salary

    def set_salary(self, value):
        self._salary = value
        self.update_view()

    salary = property(get_salary, set_salary)

    def get_salaried(self):
        return self._salaried

    def set_salaried(self, value):
        self._salaried = value
        self.update_view()

    salaried = property(get_salaried, set_salaried)

    def update_view(self):
        self.view.submit_enabled = self.all_information_is_collected()
