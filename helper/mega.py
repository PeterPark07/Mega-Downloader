import time
import os
from mega import Mega
from helper.files import get_directory_size , delete_files_in_directory

def download_file_from_mega(url):
    # Instantiate the Mega object
    mega = Mega()
    
    output_path = '/opt/render/mega/'

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Delete files in the output directory
    delete_files_in_directory(output_path)

    # Start time tracking
    start_time = time.time()

    # Download the file using the URL
    mega.download_url(url, output_path)

    # Calculate download duration
    end_time = time.time()

    # Get the directory size
    file_size = get_directory_size(output_path)

    duration = end_time - start_time

    # Calculate download speed in MB/s
    download_speed = file_size / duration / 1048576

    # Print download statistics
    print(f"Download completed in {duration:.2f} seconds.")
    print(f"Download speed: {download_speed:.2f} MBs/second")
