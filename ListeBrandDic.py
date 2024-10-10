import json
# import boto3
# from botocore.exceptions import NoCredentialsError, PartialCredentialsError

class ListeBrandDic:
    def __init__(self, file_path="combined_sorted"):
        self.file_path = f"results/ListBrandDic/{file_path}.json"
        
        # Try to read the existing data from the JSON file
        try:
            with open(self.file_path, 'r', encoding='utf-8-sig') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            # If file doesn't exist, initialize an empty list
            self.data = []

    def insert_liste_brand_dic(self, liste_brand_dic):
        # Append the new parts to the data list
        self.data.extend(liste_brand_dic)
        
        # Write the updated data list back to the JSON file
        with open(self.file_path, 'w', encoding='utf-8-sig') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)
            
    def load_data(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8-sig') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            # If file doesn't exist, initialize an empty list
            self.data = []
        return self.data

    ################################################################# for AWS S3 ####################################################################
    # def __init__(self, file_name='liste_brand_dic_1'):
    #     self.bucket_name = "test-s3-650251706104"
    #     self.file_key = f"results/ListBrandDic/{file_name}.json"
    #     self.s3_client = boto3.client('s3')
        
    #     # Try to read the existing data from the S3 bucket
    #     try:
    #         response = self.s3_client.get_object(Bucket=self.bucket_name, Key=self.file_key)
    #         self.data = json.loads(response['Body'].read().decode('utf-8-sig'))
    #     except self.s3_client.exceptions.NoSuchKey:
    #         # If file doesn't exist, initialize an empty list
    #         self.data = []
    #     except NoCredentialsError:
    #         raise Exception("AWS credentials not found.")
    #     except PartialCredentialsError:
    #         raise Exception("Incomplete AWS credentials.")
    #     except Exception as e:
    #         raise Exception(f"An error occurred: {e}")

    # def insert_liste_brand_dic(self, liste_brand_dic):
    #     # Append the new parts to the data list
    #     self.data.extend(liste_brand_dic)
        
    #     # Write the updated data list back to the S3 bucket
    #     try:
    #         self.s3_client.put_object(
    #             Bucket=self.bucket_name,
    #             Key=self.file_key,
    #             Body=json.dumps(self.data, ensure_ascii=False, indent=4).encode('utf-8-sig'),
    #             ContentType='application/json'
    #         )
    #     except NoCredentialsError:
    #         raise Exception("AWS credentials not found.")
    #     except PartialCredentialsError:
    #         raise Exception("Incomplete AWS credentials.")
    #     except Exception as e:
    #         raise Exception(f"An error occurred: {e}")

    # def load_data(self):
    #     try:
    #         response = self.s3_client.get_object(Bucket=self.bucket_name, Key=self.file_key)
    #         self.data = json.loads(response['Body'].read().decode('utf-8-sig'))
    #     except self.s3_client.exceptions.NoSuchKey:
    #         # If file doesn't exist, initialize an empty list
    #         self.data = []
    #     except NoCredentialsError:
    #         raise Exception("AWS credentials not found.")
    #     except PartialCredentialsError:
    #         raise Exception("Incomplete AWS credentials.")
    #     except Exception as e:
    #         raise Exception(f"An error occurred: {e}")
    #     return self.data
    
    # def merge_json_files(self, prefix='results/ListBrandDic/'):
    #     s3_client = boto3.client('s3')
    
    #     try:
    #         # List objects in the specified S3 path
    #         response = s3_client.list_objects_v2(Bucket=self.bucket_name, Prefix=prefix)
    #         if 'Contents' not in response:
    #             raise Exception("No files found in the specified S3 path.")
    
    #         merged_data = []
    
    #         # Iterate over the files and merge them
    #         for obj in response['Contents']:
    #             key = obj['Key']
    #             if key.endswith('.json') and key != self.file_key:
    #                 print(f"Processing file: {key}")
    #                 response = s3_client.get_object(Bucket=self.bucket_name, Key=key)
    #                 data = json.loads(response['Body'].read().decode('utf-8-sig'))
    #                 if isinstance(data, list):
    #                     merged_data.extend(data)
    #                 else:
    #                     print(f"Warning: File {key} does not contain a list of JSON objects.")
    
    #         # Save the merged data back to S3
    #         s3_client.put_object(
    #             Bucket=self.bucket_name,
    #             Key=self.file_key,
    #             Body=json.dumps(merged_data, ensure_ascii=False, indent=4).encode('utf-8-sig'),
    #             ContentType='application/json'
    #         )
    #         print(f"Merged JSON saved to: {self.file_key}")
    
    #     except NoCredentialsError:
    #         print("AWS credentials not found.")
    #     except PartialCredentialsError:
    #         print("Incomplete AWS credentials.")
    #     except Exception as e:
    #         print(f"An error occurred: {e}")