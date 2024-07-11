import os
import shutil
from datetime import datetime, timedelta

#base_path need to assign in format of window which is has ***double backslash "\\" in between each directory***
base_path = ''

#datetime is in for mat (YYYY,MM,DD) *no 0 infront the date
start_date = datetime(2024, 4, 9)
end_date = datetime(2024, 6, 4)

# Generate list of dates
dates = [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range((end_date - start_date).days + 1)]

for date in dates:
    source = os.path.join(base_path, date, date)
    destination = os.path.join(base_path, date)
    directory = source

    if os.path.exists(source):
        # Gather all files
        allfiles = os.listdir(source)

        # Iterate on all files to move them to the destination folder
        for f in allfiles:
            src_path = os.path.join(source, f)
            dst_path = os.path.join(destination, f)
            os.rename(src_path, dst_path)

        # Remove the directory if it exists and is a directory
        if os.path.exists(directory) and os.path.isdir(directory):
            shutil.rmtree(directory)
            print(f"The directory {directory} and all its contents have been removed.")
        else:
            print(f"The directory {directory} does not exist.")
    else:
        print(f"The source directory {source} does not exist.")

