import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load trained model
model = load_model("medicine_model.keras")

# App title
st.title("💊 Counterfeit Medicine Detection")

# Upload image
uploaded_file = st.file_uploader(
    "Upload Medicine Image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:

    # Load and display image
    img = image.load_img(
        uploaded_file,
        target_size=(224, 224)
    )

    st.image(uploaded_file, caption="Uploaded Medicine Image")

    # Convert image to array
    img = image.img_to_array(img)

    # Add batch dimension
    img = np.expand_dims(img, axis=0)

    # Normalize pixel values
    img = img / 255.0

    # Make prediction
    pred = model.predict(img)

    # Classification
    if pred[0][0] > 0.5:
        st.success("Real Medicine")
    else:
        st.error("Fake Medicine")