import subprocess
import os, os.path
import ftplib
import random
import shutil
import threading
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer, ThreadedFTPServer
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.filesystems import UnixFilesystem

class DummyFTP(threading.Thread):
    """
    DummyFTP server
    """
    def set_params( self, addr=None, port=None, folder=None, user=None, password=None ):
        self.addr = 'localhost' if not addr else addr
        self.port = '22122' if not port else port
        self.folder = os.path.join(os.curdir) if not folder else folder
        self.user = os.getenv('USER') if not user else user
        self.password = '' if not password else password
        self.server = DummyFTP.ftp_server( addr, port, folder, user, password )

    def run(self):
        try:
            self.server.serve_forever()
        except AttributeError:
            print("Cannot run DummyFTP: you should call 'set_params' prior to running the FTP server")

    def stop(self):
        self.join()
        self.server.stop()
        
    @staticmethod
    def ftp_server(addr, port, folder, user, password):
        handler = FTPHandler
        handler.authorizer = DummyAuthorizer()
        handler.authorizer.add_user(user , password ,folder, perm='elradfmw')
        handler.abstracted_fs = UnixFilesystem
        server = ThreadedFTPServer( (addr, port), handler )
        return server

if __name__=='__main__':
    ftp_server = test()

def test():
    my = DummyFTP()
    my.set_params()
    my.start()
    return my
