from ._anvil_designer import investNow_applyForLoanTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class investNow_applyForLoan(investNow_applyForLoanTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.main_form.login_page')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.main_form.login_page')
