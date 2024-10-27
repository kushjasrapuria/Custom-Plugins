#!/usr/bin/env python3

from pwn import *

{bindings}

gs = ('''
init-pwndbg
continue
''')

context.binary = {bin_name}

def conn():
    if args.GDB:
        return gdb.debug({proc_args}, gdbscript=gs)
    elif args.LOCAL:
        return process({proc_args})
    else:
        return remote("addr", 1337)

r = conn()

def main():

    # good luck pwning :)

    r.interactive()

if __name__ == "__main__":
    main()
