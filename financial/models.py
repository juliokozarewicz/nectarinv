from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import uuid


class financialInvoices(models.Model):

    POSTING_TYPES = (
        ('expense', _('expense')),
        ('revenue', _('revenue')),
    )

    STATUS_TYPES = (
        ('pending', _('pending')), 
        ('paid', _('paid')),
        ('canceled', _('canceled')),
        ('overdue', _('overdue')),
    )

    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    posting_type = models.CharField(max_length=50, choices=POSTING_TYPES, default='expense')
    payment_description = models.CharField(max_length=250)
    payment_amount = models.DecimalField(max_digits=20, decimal_places=2)
    due_date = models.DateField()
    payee = models.CharField(max_length=250, null=True, blank=True)
    document_number = models.CharField(max_length=250, null=True, blank=True)
    category = models.CharField(max_length=250)
    bank_account = models.CharField(max_length=100)
    card = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(max_length=300, null=True, blank=True)
    status = models.CharField(max_length=250, choices=STATUS_TYPES, default='pending')