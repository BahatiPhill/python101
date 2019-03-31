import subprocess

program = 'vlc'
process = subprocess.Popen(program)

code = process.wait()
print(code)