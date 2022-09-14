import subprocess
import os

raspi_folder = os.getcwd()

# print(raspi_folder)

folder_name1 = 'png'
folder_name2 = 'csv_original'
folder_name3 = 'csv_resampled'

subprocess.run('rclone sync ' + raspi_folder + '/folder_name1' + ' gdrive:' + folder_name1, shell=True)
# subprocess.run('rclone sync ' + raspi_folder + '/folder_name2' + ' gdrive:' + folder_name2, shell=True)
# subprocess.run('rclone sync ' + raspi_folder + '/folder_name3' + ' gdrive:' + folder_name3, shell=True)

print('finished')
