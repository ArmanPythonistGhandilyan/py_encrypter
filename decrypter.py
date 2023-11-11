import pyAesCrypt
import os

def decrypter(file, password):

    buffer_size = 512 * 1024

    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    print("[File '" + str(os.path.splitext(file)[0]) + "' was decrypted]")

    os.remove(file)

# subdirs scaner
def walking_by_dirs(dir, password):

    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        if os.path.isfile(path):
            try:
                decrypter(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(path, password)


password = input("Enter the decryption password: ")
walking_by_dirs(r"C:\Users\User\Desktop\test", password)