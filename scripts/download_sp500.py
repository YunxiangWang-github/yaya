from fredapi import Fred
import pandas as pd
import hashlib
from pathlib import Path

API_KEY = "3df2eebc0e5c86669deee55302bd4d12"
DATA_PATH = Path("data/sp500_raw.csv")
HASH_PATH = Path("data/sp500_raw.sha256")

def compute_sha256(file_path: Path) -> str:
    """Compute SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def save_hash(hash_value: str):
    """Save hash value to .sha256 file."""
    HASH_PATH.write_text(f"{hash_value}  {DATA_PATH.name}\n")

def verify_hash() -> bool:
    """Verify current file's hash matches saved hash."""
    saved_hash = HASH_PATH.read_text().split()[0]
    current_hash = compute_sha256(DATA_PATH)
    
    print("Saved hash:  ", saved_hash)
    print("Current hash:", current_hash)
    
    if saved_hash == current_hash:
        print("Integrity check PASSED")
        return True
    else:
        print("Integrity check FAILED")
        return False

def main():
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

    print("Downloading S&P 500 data from FRED...")
    fred = Fred(api_key=API_KEY)
    sp500 = fred.get_series("SP500")

    df = sp500.reset_index()
    df.columns = ["date", "close"]

    df.to_csv(DATA_PATH, index=False)
    print(f"Saved data to {DATA_PATH}")

    file_hash = compute_sha256(DATA_PATH)
    save_hash(file_hash)
    print(f"Computed SHA-256: {file_hash}")
    print(f"Saved hash to {HASH_PATH}")

    print("\nVerifying integrity...")
    verify_hash()

if __name__ == "__main__":
    main()