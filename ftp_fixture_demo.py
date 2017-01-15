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

    """
    def set_params( self, addr, port, folder, user, password ):
        self.addr = addr
        self.port = port
        self.folder = folder
        self.user = user
        self.password = password
        self.server = DummyFTP.ftp_server( addr, port, folder, user, password )

    def run(self):
        try:
            self.server.serve_forever()
        except AttributeError:
            print("Cannot run DummyFTP: you should call 'set_params' prior to running the FTP server")

    @staticmethod
    def ftp_server(addr, port, folder, user, password):
        handler = FTPHandler
        handler.authorizer = DummyAuthorizer()
        handler.authorizer.add_user(user , password ,folder, perm='elradfmw')
        handler.abstracted_fs = UnixFilesystem
        server = FTPServer( (addr, port), handler )
        return server



def ftp_server(addr, port, folder, user, password):
    handler = FTPHandler
    handler.authorizer = DummyAuthorizer()
    handler.authorizer.add_user(user , password ,folder, perm='elradfmw')
    handler.abstracted_fs = UnixFilesystem
    server = FTPServer( (addr, port), handler )
    return server


def create_test_folder():
    def random_dir_name():
        len_name = 10
        testDir = ''.join(('{',":0{}x".format(len_name),'}')).format(random.randint(0,16**len_name))
        return testDir

    userHome = os.getenv('HOME')
    success = False
    while True:
        dirName = random_dir_name()
        testFolder=os.path.join( userHome, dirName )
        try:
            os.mkdir( testFolder )
        except:
            print("folder {} already in use. Trying another one".format(dirName))
        else:
            return testFolder

def remove_test_folder(folderName):
    shutil.rmtree(folderName)

def main():
    # import pdb; pdb.set_trace()
    test_folder = create_test_folder()
    userName = os.getenv('USER')
    IPAddr = "localhost"
    password = "**********"
    port = random.randint( 2**7, 2**16 )
    server = ftp_server(IPAddr, port, test_folder, userName, password)
    server.serve_forever()
    import time; time.sleep(1)
    server.close()
    remove_test_folder( test_folder )

if __name__=='__main__':
    my = main()
    print(my)


def test():
    my = DummyFTP()
    my.set_params( 'localhost', 22222, '/home/david/test_ftp', 'david', '' )
    my.start()
    return my
