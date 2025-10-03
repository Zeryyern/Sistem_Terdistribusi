from minio import Minio  # type: ignore
import os

# Connect to MinIO server
client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

bucket_name = "mybucket"

# Create bucket if it doesn't exist
if not client.bucket_exists(bucket_name):
    client.make_bucket(bucket_name)
    print(f"Bucket '{bucket_name}' created.")
else:
    print(f"Bucket '{bucket_name}' already exists.")

print("\nChoose an action:")
print("1. Add (Upload) file")
print("2. Retrieve (Download) file")
print("3. Delete file")
print("4. List files in bucket")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    # --- ADD (Upload) a file ---
    local_file = input("Enter the local file name (e.g. Lenna_(test_image).png): ")
    object_name = input("Enter object name for bucket (e.g. lenna.png): ")
    
    if os.path.exists(local_file):
        client.fput_object(bucket_name, object_name, local_file)
        print(f"File '{local_file}' uploaded to bucket as '{object_name}'.")
    else:
        print(f"Local file '{local_file}' not found!")

elif choice == "2":
    # --- RETRIEVE (Download) file ---
    object_name = input("Enter object name to download (e.g. lenna.png): ")
    download_path = input("Enter local download name (e.g. downloaded.png): ")
    
    client.fget_object(bucket_name, object_name, download_path)
    print(f"File '{object_name}' downloaded as '{download_path}'.")

elif choice == "3":
    # --- DELETE file ---
    object_name = input("Enter object name to delete (e.g. lenna.png): ")
    client.remove_object(bucket_name, object_name)
    print(f"File '{object_name}' deleted from bucket.")

elif choice == "4":
    # --- LIST files ---
    print("\nFiles currently in the bucket:")
    for obj in client.list_objects(bucket_name):
        print("-", obj.object_name)

else:
    print("Invalid choice!")
