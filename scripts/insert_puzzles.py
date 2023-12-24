import os
import pandas as pd
from pymongo import MongoClient

def create_backup(client, db_name, old_collection_name, backup_collection_name):
    db = client[db_name]

    # Check if the old collection exists before attempting to rename it
    if old_collection_name in db.list_collection_names():
        db[old_collection_name].rename(backup_collection_name)
        print(f"Backup for previous puzzles collection created.")
    else:
        print(f"The old puzzles collection doesn't exist. No backup created.")


def insert_puzzles(collection, df, number_of_puzzles):
    df_shuffled = df.sample(frac=1).reset_index(drop=True)
    selected_puzzles = df_shuffled.head(number_of_puzzles)

    print(f"Inserting {number_of_puzzles} puzzles into the collection...")
    collection.insert_many(selected_puzzles.to_dict(orient='records'))
    print("Done!")

def main():
    client = MongoClient()
    
    try:
        client = MongoClient(os.environ['MONGODB_URL'])
        db_name = os.environ['MONGODB_DB_NAME']
        old_collection_name = 'lichess_puzzles'
        backup_collection_name = old_collection_name + '_backup'

        create_backup(client, db_name, old_collection_name, backup_collection_name)

        collection = client[db_name][old_collection_name]

        try:
            df = pd.read_csv('lichess_db_puzzle.csv')
        except FileNotFoundError as e:
            print(f"CSV file not found: {e}")
            return
        
        number_of_puzzles = int(os.environ.get('NUMBER_OF_PUZZLES', 100000))
        insert_puzzles(collection, df, number_of_puzzles)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        client.close()

if __name__ == "__main__":
    main()
