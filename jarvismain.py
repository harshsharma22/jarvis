import subprocess
import workingmain as work
def execue_command(str):
    subprocess.Popen(['c:\Program Files (x86)\espeak\command_line\espeak.exe',str])




tt=input("enter what you want to say")
t=work.working(tt)
execue_command(t)
