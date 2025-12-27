import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha1(password.encode()).hexdigest().upper()


def check_breach(password: str) -> bool:
    common_hashes = [
        "5BAA61E4C9B93F3F0682250B6CF8331B7EE68FD8"  # password
    ]

    hashed = hash_password(password)
    return hashed in common_hashes
