# Account Transfer Task

The Account Transfer Task is a Django web application designed to facilitate fund transfers between accounts. It supports importing account data from CSV files, listing accounts, retrieving account details, and transferring funds between any two accounts.

## Functional Requirements

1. **Import Accounts from CSV Files:**

- Allows uploading a CSV file containing account details (ID, name, balance) to import accounts into the system.

2. **List All Accounts:**

- Displays a paginated list of all accounts currently stored in the system.

3. **Get Account Information:**

- Provides detailed information about a specific account, including its current balance.

4. **Transfer Funds Between Two Accounts:**

- Enables users to transfer funds from one account to another. Checks for sufficient balance and prevents transfers between the same account.

## Installation

To run the Account-Transfer project locally, follow these steps:

1. **Clone the repository**: Clone this repository to your local machine using the following command:

   ```
   git clone https://github.com/MohamedSalahdj/Account-Transfer.git
   ```

2. **Create a Virtual Environment (Optional)**: It's recommended to create a virtual environment to manage project dependencies. You can create one using `virtualenv` or `venv`:

   ```
   python -m venv myenv
   ```

   Activate the virtual environment:

   ```python
   source myenv/bin/activate   # for Linux/Mac
   myenv\Scripts\activate.bat   # for Windows
   ```

3. **Install dependencies:**

   ```python
   pip install -r requirements.txt

4. **Make migration && migrate** 

   ```
   - python manage.py makemigrations
   -  python manage.py migrate
   ```

5. **Start the development server Start the Django development server:**

```python
python manage.py runserver
```
