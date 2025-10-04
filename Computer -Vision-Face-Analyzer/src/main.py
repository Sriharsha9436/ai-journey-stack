import sys
from .detector import detect_faces
from .annotator import annotate_image

def main():
    if len(sys.argv) != 2:
        print("Usage: python -m src.main <image-path>")
        sys.exit(1)

    img_path = sys.argv[1]
    with open(img_path, "rb") as f:
        img_bytes = f.read()

    faces = detect_faces(img_bytes)
    print(f"{len(faces)} faces detected.")

    for i, face in enumerate(faces, start=1):
        print(f"\nFace {i}:")
        if face.face_attributes:
            print(f"  Yaw: {face.face_attributes.head_pose.yaw:.1f}")
            print(f"  Accessories: {[a.type for a in face.face_attributes.accessories]}")
            print(f"  Occlusion: {face.face_attributes.occlusion.__dict__}")

    out = annotate_image(img_path, faces)
    print("Annotated image saved to:", out)

if __name__ == "__main__":
    main()
