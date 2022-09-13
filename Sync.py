import subprocess

FolderName = 'png'

subprocess.run('rclone sync' + FolderName + 'gdrive:' + FolderName)
