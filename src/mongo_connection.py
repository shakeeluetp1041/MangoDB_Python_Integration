from logger import setup_logger
logger = setup_logger(__name__, level='INFO')
logger.info('mongodb atles connection in progress.')
import pandas as pd
import os
from pymongo import MongoClient

# Replace <username>, <password>, and add your database name
uri = "mongodb+srv://shakeeluetp1041:Uk6GUBwkb7AulwHA@cluster0.3hunfmm.mongodb.net/"

client = MongoClient(uri)
logger.info('mongodb atles connection setup completed.')

# Mention the database name "store" you want to connect to and the file name you want to store/retrive the data in "train_data"
db = client["store"]
collection = db["train_data"]


# Load CSV into DataFrame
csv_file_path = "train.csv"  # As the file is in the project root
df = pd.read_csv(csv_file_path) # Dataframe from CSV file
logger.info('Local CSV file loaded into DataFrame.')

# Delete local CSV file
if os.path.exists(csv_file_path):
    os.remove(csv_file_path)
    logger.info('Local CSV file deleted.')
else:
    print("CSV file not found.")


# Convert to dictionary and insert into MongoDB
data_dict = df.to_dict(orient="records")
collection.insert_many(data_dict)
logger.info('File uploded to MongoDB Atles database.')

# Fetch all data from MongoDB
retrieved_data = list(collection.find())

# Convert ObjectId to string and remove "_id" if not needed
for doc in retrieved_data:
    doc.pop("_id", None)  # Remove _id field

# Convert to DataFrame
df_retrieved = pd.DataFrame(retrieved_data)

# Save to new CSV file
df_retrieved.to_csv("train.csv", index=False)

logger.info('Data retrived succesfully from MongoDB Atles')

if __name__ == "__main__":
    # Example usage
    #logger = setup_logger('test_logger')
    logger.debug('test:This is Test debug message.')
    logger.info('Test:This is an Test info message.')
    logger.error('Test:This is an Test error message.')