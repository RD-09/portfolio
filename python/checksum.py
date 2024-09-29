import codecs
import multiprocessing as multi
from cryptography.hazmat.primitives import hashes

try:
    try:
        path_input = input("Enter file path")
        path = open(path_input, mode='rb')

    except FileNotFoundError:
        print("No such file")

    else:
        content = path.read()

        def group_1():
            md5 = hashes.Hash(hashes.MD5())
            md5.update(content)
            md5_result = md5.finalize()
            sha1 = hashes.Hash(hashes.SHA1())
            sha1.update(content)
            sha1_result = sha1.finalize()

            md5_digest = codecs.encode(md5_result, 'hex')
            sha1_digest = codecs.encode(sha1_result, 'hex')

            print("\n")
            print('MD5 hash result:', md5_digest)
            print('SHA1 hash result:', sha1_digest),

        def group_2():
            sha256 = hashes.Hash(hashes.SHA256())
            sha256.update(content)
            sha256_result = sha256.finalize()
            sha512 = hashes.Hash(hashes.SHA512())
            sha512.update(content)
            sha512_result = sha512.finalize()

            sha256_digest = codecs.encode(sha256_result, 'hex')
            sha512_digest = codecs.encode(sha512_result, 'hex')

            print('SHA256 hash result:', sha256_digest)
            print('SHA512 hash result:', sha512_digest)

        p1 = multi.Process(target=group_1)
        p1.start()
        p2 = multi.Process(target=group_2)
        p2.start()

        path.close()

except Exception:
    print("Something went wrong")

