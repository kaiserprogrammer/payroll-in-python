from memory_db import MemoryDB
from add_employee_presenter import AddEmployeePresenter
import nose

presenter = None
view = None

class MockAddEmployeeView(object):
    def __init__(self):
        self.submit_enabled = False

class TransactionContainer(object):
    pass

def setUp():
    global view
    view = MockAddEmployeeView()
    container = TransactionContainer()
    db = MemoryDB()
    global presenter
    presenter = AddEmployeePresenter(view, container, db)

@nose.with_setup(setUp)
def test_for_all_informations_to_be_collected():
    assert not presenter.all_information_is_collected()
    presenter.name = "Bill"
    assert not presenter.all_information_is_collected()
    presenter.address = "123 abc"
    assert not presenter.all_information_is_collected()
    presenter.hourly = True
    assert not presenter.all_information_is_collected()
    presenter.hourly_rate = 1.23
    assert presenter.all_information_is_collected()

    presenter.hourly = False
    assert not presenter.all_information_is_collected()
    presenter.commissioned = True
    assert not presenter.all_information_is_collected()
    presenter.baseRate = 1000
    assert not presenter.all_information_is_collected()
    presenter.commission = 12
    assert presenter.all_information_is_collected()

    presenter.commissioned = False
    assert not presenter.all_information_is_collected()
    presenter.salaried = True
    assert not presenter.all_information_is_collected()
    presenter.salary = 1500
    assert presenter.all_information_is_collected()

@nose.with_setup(setUp)
def test_updating_the_view():
    assert not view.submit_enabled
    presenter.name = "Bill"
    assert not view.submit_enabled
    presenter.address = "123 abc"
    assert not view.submit_enabled
    presenter.hourly = True
    assert not view.submit_enabled
    presenter.hourly_rate = 15
    assert view.submit_enabled
