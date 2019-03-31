import subprocess

code = subprocess.call('vlc')
if code == 0:
    print('Success!')
else:
    print('Error')