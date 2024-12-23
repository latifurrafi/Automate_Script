import mysql.connector
import csv
# Database connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="MEDICINE",
    collation='utf8mb4_general_ci'
)
cursor = connection.cursor()

# Create the table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS medicine (
    BRAND_ID INT PRIMARY KEY,
    BRAND_NAME VARCHAR(255),
    TYPE VARCHAR(255),
    SLUG VARCHAR(255),
    DOSAGE_FORM VARCHAR(255),
    GENERIC VARCHAR(255),
    STRENGTH VARCHAR(255),
    MANUFACTURER VARCHAR(255),
    PACKAGE_CONTAINER VARCHAR(255),
    PACKAGE_SIZE VARCHAR(255)
);
''')
# CSV file path
csv_file = 'medicine.csv'
# Insert data from CSV file
with open(csv_file, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        cursor.execute('''
        INSERT INTO medicine (
            BRAND_ID, BRAND_NAME, TYPE, SLUG, DOSAGE_FORM, GENERIC, 
            STRENGTH, MANUFACTURER, PACKAGE_CONTAINER, PACKAGE_SIZE
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        ''', row)

# Commit changes and close the connection
connection.commit()
connection.close()
print("Data inserted successfully.")
