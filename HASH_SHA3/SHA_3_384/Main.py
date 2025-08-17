import hashlib

def generate_sha3_384():
    
    try:
        
        print(" // code by @aadnanmt //")
        print("")
        text_to_hash = input("Masukkan teks yang mau di-hash: ")
        encoded_text = text_to_hash.encode("utf-8")
        hasher = hashlib.sha3_384(encoded_text) 
        hex_hash = hasher.hexdigest()

        print("\n==== HASIL HASHING SHA3-384 (Keluarga SHA-3) ====")
        print(f"Ini Teks Asli darimu: {text_to_hash}")
        print(f"Hasil dari Hash SHA3-384: {hex_hash}\n")
        
        print("===Terimakasih sudah berkunjung dan menggunakan source code dari @aadnanmt===\n")
    
    except Exception as e:
        print(f"Oops, terjadi error: {e}")

if __name__ == "__main__":
    generate_sha3_384()