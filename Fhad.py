import binwalk.core.plugin
import subprocess,os

class FUBIFSExtractor(binwalk.core.plugin.Plugin):
    MODULES = ['Signature']
    def scan(self, result):
        if result.valid and '.had' in result.file.name:
            offset = result.offset
            filename = result.file.name
            print('*****************************************\n',filename)
