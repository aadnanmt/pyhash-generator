import hashlib

def generate_sha3_224():
  
    try:
        
        print(" // code by @aadnanmt //")
        print("")
        text_to_hash = input("Masukkan teks yang mau di-hash: ")
        encoded_text = text_to_hash.encode("utf-8")
        hasher = hashlib.sha3_224(encoded_text)
        hex_hash = hasher.hexdigest()

        print("==== HASIL HASHING SHA3-224====")
        print("\n-----------------------------")
        print(f"Ini Teks Asli darimu: {text_to_hash}")
        print("-----------------------------\n")
        print(f"Hasil dari Hash SHA3-224: {hex_hash}")
        
        print("\n")
        print("===Terimakasih sudah berkunjung dan menggunakan source code dari @aadnanmt===\n")

    except Exception as e:
        print(f"Oops, terjadi error: {e}")

if __name__ == "__main__":
    generate_sha3_224()