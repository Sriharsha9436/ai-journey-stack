from PIL import Image, ImageDraw
import io

def annotate_image(input_image_path: str, faces, output_path: str = "detected_faces.jpg"):
    """
    Original function: annotates an image from file path and saves to disk.
    """
    image = Image.open(input_image_path)
    draw = ImageDraw.Draw(image)

    for face in faces:
        rect = face.face_rectangle
        left, top, width, height = rect.left, rect.top, rect.width, rect.height

        # Draw bounding box
        draw.rectangle([(left, top), (left + width, top + height)], outline="red", width=2)

        # Add text (yaw + accessories)
        if hasattr(face, "face_attributes"):
            yaw = face.face_attributes.head_pose.yaw if face.face_attributes.head_pose else 0
            accessories = [a.type for a in face.face_attributes.accessories]
            text = f"Yaw: {yaw:.1f}, Acc: {','.join(accessories) if accessories else 'None'}"
            draw.text((left, top - 10), text, fill="red")

    image.save(output_path)
    return output_path


def annotate_image_bytes(image_bytes: bytes, faces) -> bytes:
    """
    New function: annotate image from bytes and return bytes (for Streamlit UI).
    """
    image = Image.open(io.BytesIO(image_bytes))
    draw = ImageDraw.Draw(image)

    for face in faces:
        rect = face.face_rectangle
        left, top, width, height = rect.left, rect.top, rect.width, rect.height

        # Draw bounding box
        draw.rectangle([(left, top), (left + width, top + height)], outline="red", width=2)

        # Add text (yaw + accessories)
        if hasattr(face, "face_attributes"):
            yaw = face.face_attributes.head_pose.yaw if face.face_attributes.head_pose else 0
            accessories = [a.type for a in face.face_attributes.accessories]
            text = f"Yaw: {yaw:.1f}, Acc: {','.join(accessories) if accessories else 'None'}"
            draw.text((left, top - 10), text, fill="red")

    # Save to in-memory bytes
    output_bytes = io.BytesIO()
    image.save(output_bytes, format="JPEG")
    output_bytes.seek(0)
    return output_bytes.getvalue()
