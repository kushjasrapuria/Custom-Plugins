#!/usr/bin/env python3

# Exploit by x90slide

from pwn import *

{bindings}

gs = '''
init-pwndbg
continue
'''

context.binary = {bin_name}
#context.log_level = "debug"

def conn():
    if args.GDB:
        return gdb.debug({proc_args}, gdbscript=gs)
    elif args.LOCAL:
        return process({proc_args})
    else:
        return remote("addr", 1337)

io = conn()

def main():

    # good luck pwning :)

    #gdb.attach(io, gdbscript=gs)

    io.interactive()

if __name__ == "__main__":
    main()
