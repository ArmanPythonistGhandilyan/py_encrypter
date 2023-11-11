import pyAesCrypt
import os

def encrypter(file, password):

    buffer_size = 512 * 1024

    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    print("[File '" + str(os.path.splitext(file)[0]) + "' was encrypted]")

    os.remove(file)

# subdirs scaner
def walking_by_dirs(dir, password):

    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        if os.path.isfile(path):
            try:
                encrypter(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(path, password)


password = input("Enter the encryption password: ")
walking_by_dirs(r"C:\Users\User\Desktop\test", password)
