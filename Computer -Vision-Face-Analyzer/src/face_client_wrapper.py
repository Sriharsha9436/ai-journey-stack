from azure.ai.vision.face import FaceClient
from azure.core.credentials import AzureKeyCredential
from .config import get_face_config

def get_face_client():
    endpoint, key = get_face_config()
    return FaceClient(endpoint=endpoint, credential=AzureKeyCredential(key))
