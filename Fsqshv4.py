import os
import subprocess
import binwalk.core.plugin

class Fsqshv4be(binwalk.core.plugin.Plugin):
    MODULES = ['Signature']
    def init(self):
        if self.module.extractor.enabled:
            self.module.extractor.add_rule(txtrule=None,
                                           regex=".*quashfs filesystem, big endian, version 4.0.*",
                                           extension="squashfs",
                                           cmd=self.extractor)

    def extractor(self, fname):
        fname = os.path.abspath(fname)
        outfile = os.path.splitext(fname)[0]
        print("***** Fsqshv4be ******")
        cmd1 = f"/bin/sasquatch-v4be -f -d \"{outfile}\"  \"{fname}\""
        subprocess.call(cmd1, shell=True)
        return True