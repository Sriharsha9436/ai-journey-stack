import streamlit as st
from src.detector import detect_faces
from src.annotator import annotate_image_bytes
import io

st.set_page_config(page_title="Face Analyzer", layout="wide")
st.title("🟢 Face Analyzer")

# Multi-image uploader
uploaded_files = st.file_uploader(
    "Upload one or more images", type=["jpg", "jpeg", "png"], accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        st.subheader(f"Image: {uploaded_file.name}")
        image_bytes = uploaded_file.read()

        # Detect faces
        faces = detect_faces(image_bytes)
        st.success(f"Detected {len(faces)} face(s).")

        # Display attributes
        st.markdown("**Face Attributes:**")
        for i, face in enumerate(faces, start=1):
            st.markdown(f"**Face {i}:**")
            if face.face_attributes:
                st.markdown(f"- Yaw: {face.face_attributes.head_pose.yaw:.1f}")
                st.markdown(f"- Accessories: {[a.type for a in face.face_attributes.accessories]}")
                st.markdown(f"- Occlusion: {face.face_attributes.occlusion.__dict__}")

        # Annotate image in-memory
        annotated_bytes = annotate_image_bytes(image_bytes, faces)

        # Show annotated image
        st.image(annotated_bytes, caption=f"Annotated: {uploaded_file.name}", use_container_width=True)

        # Provide download button
        st.download_button(
            label="Download Annotated Image",
            data=annotated_bytes,
            file_name=f"annotated_{uploaded_file.name}",
            mime="image/jpeg"
        )
