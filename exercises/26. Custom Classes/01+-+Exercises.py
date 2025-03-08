# #### Question 1

# Write a custom class that will be used to model a single bank account.

# Your class should implement functionality to:
# - allow initialization with values for `first_name`, `last_name`, `account_number`, `balance`, `is_overdraft_allowed`
# - keep track of a "ledger" that keeps a record of all transactions (just use a list to keep track of this)
#     - at a minimum, it should keep track of the transaction date (the current UTC datetime) and the amount 
#       (positive, or negative to indicate deposits/withdrawals) - later you could add tracking the running balance as well.
# - provide read-only properties for `first_name`, `last_name`, `account_number`, and `balance`
# - provide a property to access the ledger in such a way that a user of this class cannot mutate the ledger directly
# - provide a read-write property for `is_overdraft_allowed` that indicates whether overdrafts are allowed on the account.
# - provide methods to debit (`def withdraw`) and credit (`def deposit`) transactions that:
#     - verify withdrawals against the available balance and `is_overdraft_allowed` flag
#         - if the withdrawal is larger than the available balance and overdrafts are not allowed, this should raise a custom `OverdraftNotAllowed` exception.
#         - if the transaction value is not positive, this should raise a `ValueError` exception (we have separate methods for deposits and withdrawals, 
#           and we expect the value to be positive in both cases - one will add to the balance, one will subtract from the balance).
#     - add an entry to the ledger with a current UTC timestamp (positive or negative to indicate credit/debit)
#     - keep the available balance updated
# - implements a good string representation for the instance (maybe something like `first_name last_name (account_number): balance`)

from datetime import datetime

# Custom exception for overdraft not allowed
class OverdraftNotAllowed(Exception):
    """ Raise error for insufficient value if overdraft is not allowed """
    pass

# Bank account class
class Acc:
    def __init__(self, first_name, last_name, acc_num, initial_balance=0, allow_draft=False):
        # Initializing the account with given parameters
        self._first_name = first_name
        self._last_name = last_name
        self._acc_num = acc_num
        self._balance = initial_balance
        self._ledger = []
        self._allow_draft = allow_draft
        self._make_ledger_entry(0, initial_balance)
    
    @property
    def first_name(self):
        """ Return first name """
        return self._first_name
    
    @property
    def last_name(self):
        """ Return last name """
        return self._last_name
    
    @property
    def acc_num(self):
        """ Return account number """
        return self._acc_num
    
    @property
    def balance(self):
        """ Return current balance """
        return self._balance
    
    @property
    def ledger(self):
        """ Return ledger as a read-only tuple """
        return tuple(self._ledger)

    @property
    def allow_draft(self):
        """ Return overdraft allowed flag """
        return self._allow_draft
    
    @allow_draft.setter
    def allow_draft(self, value):
        """ Set overdraft allowed flag. Only accepts boolean values """
        if isinstance(value, bool):
            self._allow_draft = value
        else:
            raise ValueError('Allowed values: True/False')
    
    def _make_ledger_entry(self, value, current_balance):
        """ Adds a new entry to the ledger with the current UTC timestamp """
        dt = datetime.utcnow()  # Get current UTC time
        self._ledger.append((dt, value, current_balance))  # Add entry to ledger
    
    def make_deposit(self, value):
        """ Method to make a deposit """
        if value <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        self._make_ledger_entry(value, self.balance)
        self._balance += value
    
    def make_withdraw(self, value):
        """ Method to make a withdrawal """
        if value <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        
        if value > self.balance and not self.allow_draft:
            raise OverdraftNotAllowed(f'Withdrawal exceeds balance. Current balance: {self.balance}')
        
        self._make_ledger_entry(-value, self.balance)
        self._balance -= value
    
    def __repr__(self):
        """ Return a string representation of the account """
        return (
            f'Acc num: ({self.acc_num})\n'
            f'Acc name:  {self.last_name}\n'
            f'Balance: {self.balance}\n'
            f'Overdraft: {self.allow_draft}\n'
            f'Transactions: {len(self.ledger)}'
        )
    
    def __str__(self):
        """ Return a string with account number and balance """
        return f'{self.acc_num}: {self.balance}'
    
    def __eq__(self, other):
        """ Equality comparison based on account number """
        if isinstance(other, Acc):
            return self.acc_num == other.acc_num
        return False

# Test with an account
acct = Acc('John', 'Smith', '123456', 0, True)

# Check ledger entries
print(acct.ledger)

# Try making withdrawals and deposits with validation
try:
    acct.make_withdraw(10)
except OverdraftNotAllowed as ex:
    print(f'OverdraftNotAllowed exception raised:', ex)

try:
    acct.make_deposit(0)
except ValueError as ex:
    print(ex)

try:
    acct.make_deposit(-1)
except ValueError as ex:
    print(ex)

try:
    acct.make_withdraw(0)
except ValueError as ex:
    print(ex)

try:
    acct.make_withdraw(-1)
except ValueError as ex:
    print(ex)

# Print account details
print(acct)

# #### Question 2

# Expand on your class above to implement equality (`==`) comparisons between instances of your class.
# Two accounts should be considered equal if the account numbers are the same.

acct1 = Acc('Will', 'Smith', '123', 525)
acct2 = Acc('Ana', 'Souza', '444552', 125455)

# Check equality comparison
print(acct1 == acct2)  # False (different account numbers)
