import ssl
import socket
from datetime import datetime, timedelta
import warnings

def check_cert(host):
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET),
                               server_hostname=host)
    conn.connect((host, 443))
    cert = conn.getpeercert()
    conn.close()

    print(cert)

    expires = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
    assert expires - datetime.now() > timedelta(days=14)
    if expires - datetime.now() < timedelta(days=30):
        warnings.warn(f"Certificate for {host} expiring in {expires - datetime.now()}")
