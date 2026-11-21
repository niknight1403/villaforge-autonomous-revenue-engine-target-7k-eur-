import subprocess
print(subprocess.check_output(['which', 'python3']).decode().strip())