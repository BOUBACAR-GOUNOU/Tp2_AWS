
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

