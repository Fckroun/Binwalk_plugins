import binwalk.core.plugin
import subprocess,os

class Fsqshv4(binwalk.core.plugin.Plugin):
    MODULES = ['Signature']
    def scan(self, result):
        if result.valid and result.description.startswith("Squashfs filesystem, big endian, version 4.0"):
            offset = result.offset
            filename = result.file.name
            out_filename = filename + ".squashfs-root"
            print("***** SQUASHFS V4 BE ******")
            cmd1 = f"/bin/sasquatch-v4be -be -no-exit-code -f -d\"{out_filename}\" \"{filename}\""
            subprocess.call(cmd1, shell=True)
            exit(0)