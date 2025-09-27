import os
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
