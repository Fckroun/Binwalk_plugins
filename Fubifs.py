import binwalk.core.plugin
import subprocess,os

class FUBIFS(binwalk.core.plugin.Plugin):
    MODULES = ['Signature']
    def scan(self, result):
        if result.valid and result.description.startswith("UBI erase"):
            offset = result.offset
            filename = result.file.name
            out_filename = filename + ".ubirootfs"
            print(filename)
            cmd1 = f"ubireader_extract_images \"{filename}\" -o \"{out_filename}\""
            subprocess.call(cmd1, shell=True)
            directory = out_filename
            for subdir, dirs, files in os.walk(directory):
                for i in files:
                    if 'rootfs' in i :
                        cmd2 = f"binwalk -Me --run-as=root \"{os.path.join(subdir, i)}\""
                        subprocess.call(cmd2, shell=True)
                        exit(0)
