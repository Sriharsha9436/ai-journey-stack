from .face_client_wrapper import get_face_client
from azure.ai.vision.face.models import FaceDetectionModel, FaceRecognitionModel, FaceAttributeTypeDetection01

def detect_faces(image_bytes: bytes):
    client = get_face_client()

    features = [
        FaceAttributeTypeDetection01.HEAD_POSE,
        FaceAttributeTypeDetection01.OCCLUSION,
        FaceAttributeTypeDetection01.ACCESSORIES
    ]

    faces = client.detect(
        image_content=image_bytes,
        detection_model=FaceDetectionModel.DETECTION01,
        recognition_model=FaceRecognitionModel.RECOGNITION01,
        return_face_id=False,
        return_face_attributes=features
    )

    return faces
