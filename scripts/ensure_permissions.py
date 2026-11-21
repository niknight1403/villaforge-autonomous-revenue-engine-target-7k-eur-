import os
import stat
import sys

def ensure_executable(directory):
    if not os.path.exists(directory):
        print(f"Directory {directory} not found.")
        return
    
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if filename.endswith(('.sh', '.py')):
            st = os.stat(filepath)
            os.chmod(filepath, st.st_mode | stat.S_IEXEC)
            print(f"Ensured executable permissions for: {filepath}")

if __name__ == "__main__":
    ensure_executable("scripts")
    print("Pre-flight permission check completed.")