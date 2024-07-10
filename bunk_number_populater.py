# insert_bunks.py
import os
import django

# Have this file in the same folder as your proj folder so this works.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CSCWebsite.settings')
django.setup()

from booking.models import Bunk
from django.db import transaction

# Define the Bunks dictionary and prices
Bunks = {
    'WestSide': {
        'Men': ['M01', 'M02', 'M03', 'M04', 'M05', 'M06', 'M07', 'M08', 'M09', 'M10', 'M11', 'M12', 'M13',
                'M14', 'M15', 'M16'],
        'Private1': ['P1', 'P2', 'P3', 'P4', 'P5', 'P6'],
        'Private2': ['P7A', 'P7B', 'P8', 'P9', ],
        'Coed1': ['C19', 'C20', 'C21', 'C22', 'C23', 'C24', 'C25', 'C26', 'C27', 'C28', 'C29', 'C30']
    },
    'EastSide': {
        'Women': ['W45', 'W46', 'W47', 'W48', 'W49', 'W50', 'W51', 'W52', 'W53', 'W54', 'W55'],
        'Private3': ['P10A', 'P10B', 'P11', 'P12'],
        'Coed2': ['C31', 'C32', 'C33', 'C34', 'C35', 'C36', 'C37', 'C38', 'C39', 'C40', 'C41', 'C42', 'C43', 'C44',
                  'C45']
    },
    'TopFloor': {
        'Adults': ['A101', 'A102', 'A103', 'A104', 'A105', 'A106', 'A107', 'A108', 'A109', 'A110', 'A111', 'A112',
                   'A113', 'A114', 'A115'],
        'Snorers': ['S116', 'S117', 'S118', 'S119', 'S120', 'S121', 'S122', 'S123', 'S124', 'S125', 'S126', 'S127']
    }
}

# Define prices
BUNK_PRICE = 20.00
BED_PRICE = 75.00


@transaction.atomic
def insert_bunks():
    for area, bunk_types in Bunks.items():
        for sub_area, bunk_numbers in bunk_types.items():
            for bunk_number in bunk_numbers:
                if bunk_number[-1] == 'A':  # Check if it's a bed
                    price = BED_PRICE
                else:
                    price = BUNK_PRICE

                # Create Bunk object
                bunk = Bunk.objects.create(
                    bunk_number=bunk_number,
                    area=area,
                    sub_area=sub_area,
                    price_per_night=price
                )
                print(f"Created Bunk {bunk.bunk_number} in {bunk.area}/{bunk.sub_area} with price ${price}")


if __name__ == "__main__":
    insert_bunks()
