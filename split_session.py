import base64

def split_session_for_railway():
    # Read the encoded session
    with open("session_encoded.txt", "r") as f:
        session_b64 = f.read().strip()
    
    # Split into chunks of 30,000 characters (under Railway's limit)
    chunk_size = 30000
    chunks = []
    
    for i in range(0, len(session_b64), chunk_size):
        chunk = session_b64[i:i + chunk_size]
        chunks.append(chunk)
    
    print(f"Session split into {len(chunks)} chunks:")
    print()
    
    # Print environment variables to set in Railway
    for i, chunk in enumerate(chunks):
        print(f"SESSION_PART_{i + 1}_VI={chunk}")
        print()
    
    # Also create a script to reconstruct
    with open("reconstruct_session.py", "w") as f:
        f.write("""import os
import base64

def reconstruct_session():
    # Get all session parts
    parts = []
    i = 1
    while True:
        part = os.getenv(f"SESSION_PART_{i}_VI")
        if not part:
            break
        parts.append(part)
        i += 1
    
    if not parts:
        print("❌ No session parts found in environment variables")
        return False
    
    # Reconstruct the full session
    full_session = "".join(parts)
    
    try:
        # Decode and save
        session_data = base64.b64decode(full_session)
        with open("session.session", "wb") as f:
            f.write(session_data)
        print(f"✅ Session reconstructed from {len(parts)} parts")
        return True
    except Exception as e:
        print(f"❌ Failed to reconstruct session: {e}")
        return False

if __name__ == "__main__":
    reconstruct_session()
""")
    
    print(f"Created reconstruct_session.py to rebuild the session file")

if __name__ == "__main__":
    split_session_for_railway()
