"""
Install plugins to Krita and run Krita with console.
"""

import sys
import os
from shutil import (
        copy2,
        copytree,
        rmtree)
from subprocess import (
        Popen,
        PIPE)


def solve_krita_start_cmd():
    krita_start_cmd = None  # Change this to something that starts up Krita

    if krita_start_cmd is not None:
        return krita_start_cmd

    try:
        # try to find krita start command from Windows registry
        import winreg
        import shlex
        registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        key = winreg.OpenKey(registry, r"SOFTWARE\Krita\Capabilities\shell\open\command")
        cli_cmd = winreg.QueryValueEx(key, '')[0]
        krita_start_cmd = shlex.split(cli_cmd)[0]
        return krita_start_cmd
    except:
        pass  # not a Windows os, or no missing registry key?


def get_krita_resource_dir():
    platform_dirs = [
            ("linux",  r"~/.local/share/krita/pykrita"),
            ("darwin", r"~/.local/share/krita/pykrita"),
            ("win32",  r"~\AppData\Roaming\krita\pykrita")]
    for prefix, dir in platform_dirs:
        if sys.platform.startswith(prefix):
            return os.path.expanduser(dir)
    raise RuntimeError("Not supported platform, Krita resource dir can NOT be solved. (platform: {sys.platform!r})".format(**locals()))


def run_krita():
    """
    Pipe left for future redirecting...
    """
    krita_start_cmd = solve_krita_start_cmd()
    if krita_start_cmd:
        process = Popen(krita_start_cmd, stdout=PIPE)
        while process.poll() is None:
            data = process.stdout.readline()
            sys.stdout.write(data.decode("utf-8"))
            sys.stdout.flush()
        # read lingering data
        data = process.stdout.read()
        sys.stdout.write(data.decode("utf-8"))
        sys.stdout.flush()


if __name__ == "__main__":
    this_dir = os.path.dirname(sys.argv[0])
    krita_resource_dir = get_krita_resource_dir()

    pykrita_src_dir = lambda entry: os.path.abspath(os.path.join(this_dir, "..", "pykrita", entry))
    pykrita_trg_dir = lambda entry: os.path.abspath(os.path.join(krita_resource_dir, entry))

    check_src_dir = pykrita_src_dir(".")
    check_trg_dir = pykrita_trg_dir(".")
    if check_src_dir == check_trg_dir:
        raise RuntimeError("Insanity check! source dir is destination dir? (Stopping, bad install!)")

    for entry in ["pix_fika"]:
        src_dir = pykrita_src_dir(entry)
        trg_dir = pykrita_trg_dir(entry)
        if os.path.isdir(trg_dir):
            rmtree(trg_dir)
            print('remove old folder\nrmtree("{trg_dir}")'.format(**locals()))
        copytree(src_dir, trg_dir)
        print('copytree("{src_dir}",\n         "{trg_dir}")\n'.format(**locals()))

    for entry in ["pix_fika.desktop"]:
        src_dsk = pykrita_src_dir(entry)
        copy2(src_dsk, krita_resource_dir)
        print('copy2("{src_dsk}",\n      "{krita_resource_dir}")\n'.format(**locals()))

    print("\nrun_krita()\n")
    run_krita()
