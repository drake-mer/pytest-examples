import pytest


@pytest.fixture(scope='function')
def write_file(request):
    """ This fixture creates a file with given request
    as parameters (fname, text)"""
    fname, text = request.params
    with open(fname, 'w') as f :
        f.write(text)
    yield fname
    os.remove(fname)



@pytest.mark.parametrize(
    write_file, 
    [("filename.txt", "Content\nTo\nWrite\n")],
    indirect=['write_file']
)
def test_write_file(monkeypatch, write_file):
    print(write_file)
    fname = write_file
    with open(fname,'r') as f:
        for line in f:
            print(line)

