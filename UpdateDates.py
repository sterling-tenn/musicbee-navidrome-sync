import sqlite3
import csv
from datetime import datetime

# dates follow RFC 3339 - https://pkg.go.dev/time#Time.MarshalJSON
def convert_date(date):
    if date is None:
        return None

    dt = datetime.strptime(date, "%Y-%m-%d %H:%M")
    dt_with_seconds = dt.strftime("%Y-%m-%dT%H:%M:%S") + ".000000000"
    dt_with_tz = dt_with_seconds + "-04:00"
    return dt_with_tz




# Update the created_at field in the media_file table to match the date_added field in the MusicBee_Export.csv file
conn = sqlite3.connect('navidrome.db')
cursor = conn.cursor()

with open('MusicBee_Export.csv', 'r', encoding='utf8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row

    count = 0
    for row in csv_reader:
        filename = row[1]
        date_added = convert_date(row[9])
        path = f'/var/lib/navidrome/Music/{filename}'

        # Update the created_at field in the media_file table
        cursor.execute("UPDATE media_file SET created_at = ? WHERE path = ?", (date_added, path))
        count += cursor.rowcount

if count > 0:
    print(f"{count} records affected.")
else:
    print("No rows were affected.")

conn.commit()
conn.close()





# Format the play_date field in the annotation table properly
conn = sqlite3.connect('navidrome.db')
cursor = conn.cursor()

cursor.execute("SELECT ann_id, play_date FROM annotation")
annotations = cursor.fetchall()

for ann in annotations:
    ann_id = ann[0]
    play_date = ann[1][:-3]

    play_date = convert_date(play_date)
    cursor.execute("UPDATE annotation SET play_date = ? WHERE ann_id = ?", (play_date, ann_id))

conn.commit()
conn.close()