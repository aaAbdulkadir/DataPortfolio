def ingest_to_azure(local_file_path, conn_string, container_name, csv_name):

    from azure.storage.blob import BlobServiceClient
    
    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(conn_string)

    print('Connection to Azure established.')

    # Create a blob client using the local file name as the name for the blob
    for csv in csv_name:
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=csv)

        print(f"\nUploading to Azure Storage as blob: {csv}\n\t")

        # Upload the created file
        with open(f"{local_file_path}/output/{csv}", "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

    print('File uploaded sucessfully!')
