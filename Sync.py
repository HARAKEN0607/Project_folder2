import subprocess
import os

raspi_folder = os.getcwd()

# print(raspi_folder)

gdrive_name = 'png'

subprocess.run('rclone sync' + raspi_folder + '/png' + 'gdrive:' + FolderName)
