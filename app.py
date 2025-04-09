import streamlit as st 
from pathlib import Path
import google.generativeai as genai

from api_key import api_key
genai.configure(api_key=api_key)

st.set_page_config(page_title = "Vital Image Analytics", page_icon = ":robot:")

generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    }
]


system_prompt="""
As a highly skilled medical practitioner specializing in image analysis, you are tasked with examining medical images for a reowned hospital. Your expertise is crucial in identifying any anomalies, diseases, or health issues that may be present in the images.

Your Responsibilities includes:
1. Detailed Analysis: Throughly analyze each image, focusing on identifying any abnormal findings.
2. Findings Report: Document all observed anamolies or signs of disease. Clearly articulate these findings in a structured format.
3. Recommendations and Next Steps: Based on this analysis, suggest potential next steps, including further tests or treatments as applicable.
4. Treatment Suggestion: If appropriate, recommend possible treatment options or interventions.


Important Note:

1. Scope of Response: Only respond if the image pertains to human health issues.
2. Clarity of Image: In cases where the image quality impedes clear analysis, note that certain aspects are 'Unable to be determined based on the provided image.'
3. Disclaimer: Accompany your analysis with the disclaimer: "Consult a doctor before making any decisions."

4. Your insights are invaluable in guiding clinical decisions. Please procees with the analysis, adhering to the structured approach outlined above.

Please respond me in these 4 headlines: Detailed Analysis, Findings Report, Recommendations and Next Steps, Treatment Suggestion, Disclaimer.

"""

model = genai.GenerativeModel(model_name = "models/gemini-1.5-pro-latest",
                              generation_config = generation_config,
                              safety_settings = safety_settings)


st.image("logo.png", width =150)
st.title("Vital Image Analysis")
st.subheader("An application that can help users to identify medical images")

uploaded_file = st.file_uploader("Upload an image", type = ["png", "jpg", "jpeg"])
if uploaded_file: 
    st.image(uploaded_file, width=300, caption = "Uploaded Medical Image")

submit_button = st.button("Generate the Analysis")

if submit_button:
    ## process the uploaded image 
    image_data = uploaded_file.getvalue()

    ## making our image ready
    image_parts = [
        {
            "mime_type": "image/jpeg",
            "data": image_data
        },
    ]

    ## making our prompt ready
    prompt_parts = [
        image_parts[0],
        system_prompt,
    ]

    ## Generate a response based on prompt and image 
    response = model.generate_content(prompt_parts)
    if response:
        st.title("Here is the analysis based on your image: ")
        st.write(response.text)
