import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Load TFLite model
interpreter = tf.lite.Interpreter(
    model_path="medicine_model_float16.tflite"
)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

st.title("💊 Counterfeit Medicine Detection")

uploaded_file = st.file_uploader(
    "Upload Medicine Image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:

    img = image.load_img(
        uploaded_file,
        target_size=(224, 224)
    )

    st.image(
        uploaded_file,
        caption="Uploaded Medicine Image"
    )

    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    # TFLite prediction
    interpreter.set_tensor(
        input_details[0]["index"],
        img_array.astype(np.float32)
    )

    interpreter.invoke()

    prediction = interpreter.get_tensor(
        output_details[0]["index"]
    )

    score = float(prediction[0][0])

    # Prediction and confidence
    if score > 0.5:
        confidence = score
        st.success(
            f"✅ Real Medicine — Confidence: {confidence:.2%}"
        )
    else:
        confidence = 1 - score
        st.error(
            f"❌ Fake Medicine — Confidence: {confidence:.2%}"
        )