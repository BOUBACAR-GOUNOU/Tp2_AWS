
##-----------------------------------------------------------#
#   Partie 2 :  Manipulation DynamoDb
#   boto3
##------------------------------------------------------------#

# #-----------------------------------------------------------#
# # Suppression de tables
# #------------------------------------------------------------#
#
# import boto3
#
# def delete_devices_table(dynamodb=None):
#     dynamodb = boto3.resource('dynamodb')
#
#     devices_table = dynamodb.Table('Etudiant')
#     devices_table.delete()
#
# if __name__ == '__main__':
#     delete_devices_table()
#     print("Table supprimée.")
#


#
# #-----------------------------------------------------------#
# #Suppression de données dans la tables
# #------------------------------------------------------------#
#

# from botocore.exceptions import ClientError
# from pprint import pprint
# import boto3  # import Boto3
#
#
# def delete_device(matricule, filiere, info_timestamp, dynamodb=None):
#
#     dynamodb = boto3.resource('dynamodb')
#
#     etudiant_table = dynamodb.Table('Etudiant')
#
#     try:
#         response = etudiant_table.delete_item(
#             Key={
#                 'matricule': matricule,
#                 'filiere': filiere
#             },
#             # Condition
#             ConditionExpression="info.info_timestamp <= :value",
#             ExpressionAttributeValues={
#                 ":value": info_timestamp
#             }
#         )
#     except ClientError as er:
#         if er.response['Error']['Code'] == "ConditionalCheckFailedException":
#             print(er.response['Error']['Message'])
#         else:
#             raise
#     else:
#         return response
#
#
# if __name__ == '__main__':
#     print("DynamoBD  Suppression")
#     # Provide device_id, datacount, info_timestamp
#     delete_response = delete_device("10001","SI", "1712519200")
#     if delete_response:
#         print("Etudiant supprimé:")
#         # response
#         pprint(delete_response)




# #-----------------------------------------------------------#
# # Mise à jour de données dans la tables
# #------------------------------------------------------------#
#
#
# from pprint import pprint  # import pprint, a module that enable to “pretty-print”
# import boto3
#
# def update_etudiant(matricule, filiere, info_timestamp,nom,prenom, dynamodb=None):
#
#     dynamodb = boto3.resource('dynamodb')
#
#     etudiant_table = dynamodb.Table('Etudiant')
#
#     response = etudiant_table.update_item(
#         Key={
#             'matricule': matricule,
#             'filiere': filiere
#         },
#         UpdateExpression="set info.info_timestamp=:time, info.nom=:n, info.prenom=:p",
#         ExpressionAttributeValues={
#             ':time': info_timestamp,
#             ':n': nom,
#             ':p': prenom,
#         }
#     )
#     return response
#
#
# if __name__ == '__main__':
#     update_response = update_etudiant( "10001", "SI", "1612522870", "nom_modifie", "prenom_modif")
#     print("Données étudiant modifiée")
#     # Print response
#     pprint(update_response)

#
#
# # #-----------------------------------------------------------#
# # # Lecture de données dans la tables
# # #------------------------------------------------------------#
#
# # import Boto3 exceptions and error handling module
# from botocore.exceptions import ClientError
# import boto3
#
#
# def get_device(matricule, filiere, dynamodb=None):
#     dynamodb = boto3.resource('dynamodb')
#
#     # nom de la table
#     etudiant_table = dynamodb.Table('Etudiant')
#
#     try:
#         response = etudiant_table.get_item(
#             Key={'matricule': matricule, 'filiere': filiere})
#     except ClientError as e:
#         print(e.response['Error']['Message'])
#     else:
#         return response['Item']
#
#
# if __name__ == '__main__':
#     etudiant = get_device("10001", "SI",)
#     if etudiant:
#         print("Les données etudiant:")
#         # Print the data read
#         print(etudiant)



# #-----------------------------------------------------------#
# # Insertions des données dans la tables
# #------------------------------------------------------------#
#
# import json  # module de convertion Python objects à JSON
# from decimal import Decimal
# import boto3
#
#
# def load_data(etudiants, dynamodb=None):
#     dynamodb = boto3.resource('dynamodb')
#
#     etudiant_table = dynamodb.Table('Etudiant')
#     # Loop through all the items and load each
#     for etudiant in etudiants:
#         matricule = (etudiant['matricule'])
#         filiere = etudiant['filiere']
#         # Print device info
#         print("Chargement des données", matricule, filiere)
#         etudiant_table.put_item(Item=etudiant)
#
#
# if __name__ == '__main__':
#     # open file and read all the data in it
#     with open("data.json") as json_file:
#         etudiant_list = json.load(json_file, parse_float=Decimal)
#     load_data(etudiant_list)




# #-----------------------------------------------------------#
# #  Création de table sur dynamo
# #------------------------------------------------------------#
#
# import boto3
#
# def create_devices_table(dynamodb=None): #fonction de création d'une table
#     dynamodb = boto3.resource('dynamodb')
#     # Table defination
#     table = dynamodb.create_table(
#         TableName='Etudiant',
#         KeySchema=[
#             {
#                 'AttributeName': 'matricule',
#                 'KeyType': 'HASH'  # clé de partition
#             },
#             {
#                 'AttributeName': 'filiere',
#                 'KeyType': 'RANGE'  # Sort key
#             },
#         ],
#         AttributeDefinitions=[
#             {
#                 'AttributeName': 'matricule',
#                 # AttributeType  'S' est pour les string type and 'N' pour les nombres
#                 'AttributeType': 'S'
#             },
#             {
#                 'AttributeName': 'filiere',
#                 'AttributeType': 'S'
#             },
#         ],
#         ProvisionedThroughput={
#             # ReadCapacityUnits défini sur 10 lectures fortement cohérentes par seconde
#             'ReadCapacityUnits': 10,
#             'WriteCapacityUnits': 10  # WriteCapacityUnits défini à 10
#         }
#     )
#     return table
#
#
# if __name__ == '__main__':
#
#     device_table = create_devices_table()
#
#     # Afficher le statut de création
#     print("Status:", device_table.table_status)


# #-----------------------------------------------------------#
# # Configuration préable
# #------------------------------------------------------------#
#
# Pour cette partie vous devez installer boto3
# commande : pip install boto3
# Et aussi CRT
# commande : pip install boto3[crt]
# Avant d'utiliser Boto3 proprement dit,
# Vous devez configurer les identifiants d'authentification pour votre compte AWS à l'aide de de l'AWS CLI




# #-----------------------------------------------------------#
# # Suppression de compartiment non vide
# #------------------------------------------------------------#
#
# import boto3
#
# AWS_REGION = "eu-west-3"
# S3_BUCKET_NAME = "ingi2022-bouback"
#
# def cleanup_s3_bucket():
#
#     # suppression d'objet
#     for s3_object in s3_bucket.objects.all():
#         s3_object.delete()
#     # Deleting objects versions if S3 versioning enabled
#     for s3_object_ver in s3_bucket.object_versions.all():
#         s3_object_ver.delete()
#     print("S3 objet supprimé ")
#
# s3_resource = boto3.resource("s3", region_name=AWS_REGION)
# s3_bucket = s3_resource.Bucket(S3_BUCKET_NAME)
#
# cleanup_s3_bucket()
#
# s3_bucket.delete()
#
# print("S3 compartiment supprimé")




# #-----------------------------------------------------------#
# # Importation de fichier de bucket
# #------------------------------------------------------------#
#
# import boto3
# from pathlib import Path
#
#
# AWS_REGION = "eu-west-3"
# S3_BUCKET_NAME = "ingi2022-bouback"
#
# s3_resource = boto3.resource("s3", region_name=AWS_REGION)
#
# s3_object = s3_resource.Object(S3_BUCKET_NAME, 'latex.pdf')
# path = Path("file_")
# path.mkdir(parents=True, exist_ok=True)
# s3_object.download_file('file_/latex.pdf')
#
# print('S3 object téléchargé')



# #-----------------------------------------------------------#
# # Supression de fichier dans le compartiment.
# #------------------------------------------------------------#
#
# import boto3
#
# AWS_REGION = "eu-west-3"
# S3_BUCKET_NAME = "ingi2022-bouback"
#
# s3_resource = boto3.resource("s3", region_name=AWS_REGION)
#
# s3_object = s3_resource.Object(S3_BUCKET_NAME, 'aws.png')
#
# s3_object.delete()
#
# print('aws.png est supprimé avec success')



#-----------------------------------------------------------#
# Afficher d'objet contenu dans le compartiment.
#------------------------------------------------------------#

# import boto3
#
# AWS_REGION = "eu-west-3"
# S3_BUCKET_NAME = "ingi2022-bouback"
#
# s3_resource = boto3.resource("s3", region_name=AWS_REGION)
#
# s3_bucket = s3_resource.Bucket(S3_BUCKET_NAME)
#
# print('Liste des fichiers contenus dans la bucket:')
#
# for obj in s3_bucket.objects.all():
#     print(f'-- {obj.key}')



# #-----------------------------------------------------------#
# # Création d'objets et insertion dans les dans le compartiment.
# #------------------------------------------------------------#
# import pathlib
# import boto3
# from glob import glob
# import os
#
#

#
# BASE_DIR = pathlib.Path(__file__).parent.resolve()
# FILE_DIR =  os.path.join(BASE_DIR, 'files')
#
# AWS_REGION = "eu-west-3"
# bucket_name = "ingi2022-bouback"
#
# #fonction de techargement d'un fichier sur le bucket
# def upload_files(file_name, bucket, object_name=None, args=None):
#     client = boto3.client("s3", region_name=AWS_REGION)
#     if object_name is None:
#         object_name = file_name
#     client.upload_file(file_name, bucket, object_name)
#     print(f"'{file_name}' Téléchargé dans '{bucket_name}'")
#
#
# if __name__ == '__main__':
#
#     # fil_name = os.path.join(FILE_DIR, 'aws.png' )
#     # upload_files(file_name=fil_name, bucket=bucket_name, object_name='aws.png')
#
#     files = glob(f'{FILE_DIR}/*')
#     for f in files:
#         f_name = os.path.basename(f)
#         upload_files(file_name=f, bucket=bucket_name, object_name=f'files/{f_name}')
#

#-----------------------------------------------------------#
# vérification de compartiment
#------------------------------------------------------------#

# import boto3
# client = boto3.client('s3')
# response = client.list_buckets()
#
#
# if not response['Buckets']:
#     print('Pas de compartiment')
# else:
#     for bucket in response['Buckets']:
#         print('Compartiments disponibles:')
#         print(f'  {bucket["Name"]}')


#-----------------------------------------------------------#
# création de compartiment
#------------------------------------------------------------#

#import boto3
# AWS_REGION = "eu-west-3"
# client = boto3.client("s3", region_name=AWS_REGION)
#
# bucket_name = "ingi2022-bouback"
# location = {'LocationConstraint': AWS_REGION}
#
# response = client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
#
# print("Amazon S3 bucket est créé")

# import boto3
#
# AWS_REGION = "eu-west-3"
# resource = boto3.resource("s3", region_name=AWS_REGION)
#
# bucket_name = "ingi2022-bouback"
# location = {'LocationConstraint': AWS_REGION}
#
# response = resource.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
#
# print("Amazon S3 ressource bucket est créé")

