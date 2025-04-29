## <---------- Import Dependencies and Configuration ---------->
import streamlit as st
from pathlib import Path
import google.generativeai as genai

from api_key import api_key  # Importing API key from a separate module
genai.configure(api_key=api_key)  # Configuring the API key

# Setting the Streamlit app page config
st.set_page_config(page_title = "Vital Image Analytics", page_icon = ":robot:")


## <---------- Generation Configuration and Safety Settings ---------->
# Configuration for how the model generates responses
generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
}

# Content moderation and safety settings
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

## <---------- System Prompt for Medical Image Analysis ---------->
# Instructional prompt for the AI model with clear analysis structure
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


## <---------- Initialize Generative Model ---------->  
# Loading the Gemini model with config and safety settings
model = genai.GenerativeModel(model_name = "models/gemini-1.5-pro-latest",
                              generation_config = generation_config,
                              safety_settings = safety_settings)


## <---------- UI Elements: Logo, Title, Subheader ---------->

st.image("logo.png", width=150)  # Display hospital or app logo
st.title("Med Detect AI: Vital Image Analysis")  # Main Title
st.subheader("An application that can help users to identify medical images")  # Subtitle

## <---------- Image Upload UI and Display ---------->
# File uploader for users to upload medical images
uploaded_file = st.file_uploader("Upload an image", type = ["png", "jpg", "jpeg"])
if uploaded_file: 
    st.image(uploaded_file, width=300, caption = "Uploaded Medical Image")

# Button to trigger the AI analysis
submit_button = st.button("Generate the Analysis")

## <---------- Analysis Logic and AI Integration ---------->
if submit_button:
    ## process the uploaded image 
    image_data = uploaded_file.getvalue()  # Get image data in bytes

    ## making our image ready
    image_parts = [
        {
            "mime_type": "image/jpeg",  # Mime type
            "data": image_data  # Image data
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
        st.title("Here is the analysis based on your image: ")  # Display result heading
        st.write(response.text)  # Show model's analysis

