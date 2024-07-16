from django.db import models
from django.utils import timezone

class Account(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    

    def transfer_funds(self, target_account, amount):
        if self.balance >= amount > 0:
            self.balance -= amount
            target_account.balance += amount
            self.save()
            target_account.save()

            # Create a single transaction record
            transaction = Transaction.objects.create(
                sender=self,
                receiver=target_account,
                amount=amount
            )

            return True

        return False
        
    

class Transaction(models.Model):
    sender = models.ForeignKey(Account, related_name='sent_transactions', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Account, related_name='received_transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.sender} to {self.receiver}: {self.amount}"
