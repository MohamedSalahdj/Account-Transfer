from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
import uuid
from .models import Account, Transaction


class AccountModelTests(TestCase):

    def setUp(self):
        self.acc_1 = Account.objects.create(id=uuid.uuid4(), name='Acc_1', balance=1000)
        self.acc_2 = Account.objects.create(id=uuid.uuid4(), name='Acc_2', balance=500)

    def test_create_account(self):
        account = Account.objects.create(id=uuid.uuid4(), name='Test_Account', balance=1000)
        self.assertEqual(account.name, 'Test_Account')
        self.assertEqual(account.balance, 1000)

    def test_account_str(self):
        self.assertEqual(str(self.acc_1), 'Acc_1')


class AccountTests(TestCase):

    def setUp(self):
        self.acc_1 = Account.objects.create(id=uuid.uuid4(), name='Acc_1', balance=1000)
        self.acc_2 = Account.objects.create(id=uuid.uuid4(), name='Acc_2', balance=500)

    def test_account_list_view(self):
        response = self.client.get(reverse('account_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Acc_1')
        self.assertContains(response, 'Acc_2')


class AccountDetailTests(TestCase):

    def setUp(self):
        self.acc = Account.objects.create(id=uuid.uuid4(), name='Acc_1', balance=1000)

    def test_account_detail_view(self):
        response = self.client.get(reverse('account_detail', kwargs={'pk': self.acc.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Acc_1')
        self.assertContains(response, '1000')


class ImportAccountsTests(TestCase):

    def test_import_accounts(self):
        csv_content = "id,name,balance\n" + "\n".join(
            [
                "{},Test Account {},500.00".format(uuid.uuid4(), i)
                for i in range(1, 4)
            ]
        )
        csv_file = SimpleUploadedFile(
            "accounts.csv",
            csv_content.encode('utf-8'),
            content_type="text/csv"
        )
        response = self.client.post(reverse('import_accounts'), {'file': csv_file})
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(Account.objects.count(), 3)


class TransactionListTests(TestCase):

    def setUp(self):
        self.source_acc = Account.objects.create(id=uuid.uuid4(), name='Source', balance=1000)
        self.target_acc = Account.objects.create(id=uuid.uuid4(), name='Target', balance=500)
        self.transaction = Transaction.objects.create(
            sender=self.source_acc,
            receiver=self.target_acc,
            amount=200
        )

    def test_transaction_list_view(self):
        response = self.client.get(reverse('transaction_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.transaction.sender.name)
        self.assertContains(response, self.transaction.receiver.name)
        self.assertContains(response, self.transaction.amount)


