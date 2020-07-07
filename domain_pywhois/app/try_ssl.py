import ssl
import OpenSSL
from datetime import datetime

def get_SSL_Expiry_Date(host, port):
    cert = ssl.get_server_certificate((host, 443))
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    return x509.get_notAfter()

def ssl_end_date(A):
    #byte to str
    B = A.decode()
    C = datetime.strptime(B[0:8], "%Y%m%d")
    return C
    
if __name__ == '__main__':
    print(ssl_end_date(get_SSL_Expiry_Date('google.com', 443)))
#    get_SSL_Expiry_Date('yihedongman.com', 443)