import ssl

def create_ssl_context():

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

    context.minimum_version = ssl.TLSVersion.TLSv1_2

    # certificat serveur
    context.load_cert_chain(
        certfile="certs/server-cert.pem",
        keyfile="certs/server-key.pem"
    )

    # CA pour vérifier clients
    context.load_verify_locations(
        cafile="certs/ca-cert.pem"
    )

    # 🔐 mTLS activé
    context.verify_mode = ssl.CERT_REQUIRED

    return context
