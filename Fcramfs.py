import binwalk.core.plugin
import subprocess,os

class Fcramfs(binwalk.core.plugin.Plugin):
    MODULES = ['Signature']
    def scan(self, result):
        if result.valid and result.description.startswith("CramFS filesystem, big endian"):
            offset = result.offset
            filename = result.file.name
            out_filename = filename + ".cramrootfs"
            print(filename)
            cmd1 = f"7z x \"{filename}\" -o\"{out_filename}\""
            subprocess.call(cmd1, shell=True)
            exit(0)