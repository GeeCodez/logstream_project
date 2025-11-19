from django.core.management import BaseCommand
from api.models import logEntry
import random 
import time

class Command(BaseCommand):
    help="Seed the database with large number of entries"

    def handle(self,*args,**kwargs)-> str|None:
        TOTAL_LOGS=100000
        BATCH_SIZE=10,000

        services=["payment-services","frontend-apps","orders-services"]
        levels=['INFO','WARNING','ERROR','DEBUG']

        self.stdout.write(f"Starting to seed {TOTAL_LOGS} number of log enties in {BATCH_SIZE}...")

        star_time=time.time()

        logs_batch=[]

        for i in range(TOTAL_LOGS):
            log=logEntry(
                service_name=random.choice(services),
                level=random.choice(levels),
                message=f"This is log entry {i+1}. A sample log entry.."
            )

            logs_batch.append(log)

            if len(logs_batch)==BATCH_SIZE:
                logEntry.objects.bulk_create(logs_batch)
                logs_batch=[]
                self.stdout.write(f"Inserted {i+1}/{TOTAL_LOGS} logs ...")

        if len(logs_batch):
            logEntry.objects.bulk_create(logs_batch)
            self.stdout.write(f"Inserted the final batch.")

        end_time=time.time()
        self.stdout.write(
            self.style.SUCCESS(
                f"Succesfully added {TOTAL_LOGS} in {end_time-star_time:.2f} seconds"
            )
        )