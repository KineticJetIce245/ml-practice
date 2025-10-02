import numpy as np
import pandas as pd

import keras

chicago_taxi_dataset = pd.read_csv("chicago_taxi.csv")

training_df = chicago_taxi_dataset.loc[
    :, ("TRIP_MILES", "TRIP_SECONDS", "FARE", "COMPANY", "PAYMENT_TYPE", "TIP_RATE")
]

print("Read dataset completed successfully.")
print("Total number of rows: {0}\n\n".format(len(training_df.index)))
training_df.head(200)
training_df.describe(include="all")
