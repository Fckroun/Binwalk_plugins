import os
import subprocess
import binwalk.core.plugin

class Fubifs(binwalk.core.plugin.Plugin):
    MODULES = ['Signature']
    def init(self):
        if self.module.extractor.enabled:
            self.module.extractor.add_rule(txtrule=None,
                                           regex=".*ubi erase.*",
                                           extension="ubirootfs",
                                           cmd=self.extractor)

    def extractor(self, fname):
        fname = os.path.abspath(fname)
        outfile = os.path.splitext(fname)[0]
        cmd1 = f"ubireader_extract_images \"{fname}\" -o \"{outfile}\""
        print(cmd1)
        subprocess.call(cmd1, shell=True)
        return True