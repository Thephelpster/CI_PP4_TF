from django.db import models

# Create your models here.
from django.contrib.auth.models import User

time_slots = (
    ('15:00', '15:00'),
    ('16:00', '16:00'),
    ('17:00', '17:00'),
    ('18:00', '18:00'),
    ('19:00', '19:00'),
    ('20:00', '20:00'),
    ('21:00', '21:00'),
)


status_options = (
    ('Awaiting confirmation', 'Awaiting Confirmation'),
    ('Booking Confirmed', 'Booking Confirmed'),
    ('Booking Rejected', 'Booking Rejected'),
    ('Booking Expired', 'Booking Expired'),
)



class Table(models.Model):
    table_id = models.AutoField(primary_key=True)
    table_name = models.CharField(
        max_length=50,
        default='New Table',
        unique=True
        )
    max_seats = models.PositiveIntegerField(default=2)

    class Meta:
        ordering = ['-max_seats']

    def __str__(self):
        return self.table_name


# The booking model for the database


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    requested_date = models.DateField()
    requested_time = models.CharField(
        max_length=25,
        choices=time_slots,
        default='17:00'
        )
    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        related_name="table_reserved",
        null=True
        )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user", null=True)
    name = models.CharField(
        max_length=50,
        null=True
        )
    email = models.EmailField(
        max_length=254,
        default=""
        )
    status = models.CharField(
        max_length=25,
        choices=status_options,
        default='Awaiting confirmation'
        )
    seats = (
        (1, "1 Guest"),
        (2, "2 Guests"),
        (3, "3 Guests"),
        (4, "4 Guests"),
        (5, "5 Guests"),
        (6, "6 Guests"),
        )
    guest_count = models.IntegerField(choices=seats, default=2)

    class Meta:
        ordering = ['-requested_time']
        unique_together = ('requested_date', 'requested_time', 'table')

    def __str__(self):
        return self.status