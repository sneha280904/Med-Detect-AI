# import streamlit as st 
# from pathlib import Path
# import google.generativeai as genai

# from api_key import api_key
# genai.configure(api_key=api_key)

# st.set_page_config(page_title = "Vital Image Analytics", page_icon = ":robot:")

# generation_config = {
#     "temperature": 0.4,
#     "top_p": 1,
#     "top_k": 32,
#     "max_output_tokens": 4096,
# }

# safety_settings = [
#     {
#         "category": "HARM_CATEGORY_HARASSMENT",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#     },
#     {
#         "category": "HARM_CATEGORY_HATE_SPEECH",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#     },
#     {
#         "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#     },
#     {
#         "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#     }
# ]


# system_prompt="""
# As a highly skilled medical practitioner specializing in image analysis, you are tasked with examining medical images for a reowned hospital. Your expertise is crucial in identifying any anomalies, diseases, or health issues that may be present in the images.

# Your Responsibilities includes:
# 1. Detailed Analysis: Throughly analyze each image, focusing on identifying any abnormal findings.
# 2. Findings Report: Document all observed anamolies or signs of disease. Clearly articulate these findings in a structured format.
# 3. Recommendations and Next Steps: Based on this analysis, suggest potential next steps, including further tests or treatments as applicable.
# 4. Treatment Suggestion: If appropriate, recommend possible treatment options or interventions.


# Important Note:

# 1. Scope of Response: Only respond if the image pertains to human health issues.
# 2. Clarity of Image: In cases where the image quality impedes clear analysis, note that certain aspects are 'Unable to be determined based on the provided image.'
# 3. Disclaimer: Accompany your analysis with the disclaimer: "Consult a doctor before making any decisions."

# 4. Your insights are invaluable in guiding clinical decisions. Please procees with the analysis, adhering to the structured approach outlined above.

# Please respond me in these 4 headlines: Detailed Analysis, Findings Report, Recommendations and Next Steps, Treatment Suggestion, Disclaimer.

# """

# model = genai.GenerativeModel(model_name = "models/gemini-1.5-pro-latest",
#                               generation_config = generation_config,
#                               safety_settings = safety_settings)


# st.image("logo.png", width =150)
# st.title("Med Detect AI: Vital Image Analysis")
# st.subheader("An application that can help users to identify medical images")

# uploaded_file = st.file_uploader("Upload an image", type = ["png", "jpg", "jpeg"])
# if uploaded_file: 
#     st.image(uploaded_file, width=300, caption = "Uploaded Medical Image")

# submit_button = st.button("Generate the Analysis")

# if submit_button:
#     ## process the uploaded image 
#     image_data = uploaded_file.getvalue()

#     ## making our image ready
#     image_parts = [
#         {
#             "mime_type": "image/jpeg",
#             "data": image_data
#         },
#     ]

#     ## making our prompt ready
#     prompt_parts = [
#         image_parts[0],
#         system_prompt,
#     ]

#     ## Generate a response based on prompt and image 
#     response = model.generate_content(prompt_parts)
#     if response:
#         st.title("Here is the analysis based on your image: ")
#         st.write(response.text)












import streamlit as st
import base64
import google.generativeai as genai
from api_key import api_key

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Med-Detect-AI", page_icon="🧠", layout="centered")

# # Set page config
# st.set_page_config(page_title="Vital Image Analytics", page_icon=":robot:")

# Gemini API setup
genai.configure(api_key=api_key)

generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]


model = genai.GenerativeModel(
    model_name="models/gemini-1.5-pro-latest",
    generation_config=generation_config,
    safety_settings=safety_settings
)

system_prompt = """
As a highly skilled medical practitioner specializing in image analysis, you are tasked with examining medical images for a reowned hospital. Your expertise is crucial in identifying any anomalies, diseases, or health issues that may be present in the images.cal images...

# Please respond in these 5 headlines: 
# 1. Detailed Analysis 
# 2. Findings Report 
# 3. Recommendations and Next Steps 
# 4. Treatment Suggestion 
# 5. Disclaimer: Consult a doctor before making any decisions.

Your Responsibilities includes:
1. Detailed Analysis: Throughly analyze each image, focusing on identifying any abnormal findings.
2. Findings Report: Document all observed anamolies or signs of disease. Clearly articulate these findings in a structured format.
3. Recommendations and Next Steps: Based on this analysis, suggest potential next steps, including further tests or treatments as applicable.
4. Treatment Suggestion: If appropriate, recommend possible treatment options or interventions.
5. Disclaimer: Consult a doctor before making any decisions.

Important Note:
1. Scope of Response: Only respond if the image pertains to human health issues.
2. Clarity of Image: In cases where the image quality impedes clear analysis, note that certain aspects are 'Unable to be determined based on the provided image.'
3. Disclaimer: Accompany your analysis with the disclaimer: "Consult a doctor before making any decisions."
4. Your insights are invaluable in guiding clinical decisions. Please procees with the analysis, adhering to the structured approach outlined above.

Please respond me in these 4 headlines: Detailed Analysis, Findings Report, Recommendations and Next Steps, Treatment Suggestion, Disclaimer.
"""

# ---------------- STYLE ----------------
def load_logo_base64(path="logo.png"):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo_base64 = load_logo_base64()

st.markdown(f"""
<style>
/* Background Animation */
body {{
    background: linear-gradient(120deg, #f7f9fc, #ffffff);
    font-family: 'Segoe UI', sans-serif;
}}

.title-section {{
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    margin-top: 15px;
}}

.logo {{
    width: 70px;
    height: 70px;
    border-radius: 50%;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
}}

.main-title {{
    font-size: 40px;
    font-weight: 700;
    color: #2c3e50;
}}

.subheader {{
    text-align: center;
    font-size: 18px;
    color: #7f8c8d;
    margin-bottom: 60px;
}}

.uploadbox {{
    background-color: #ecf0f1;
    padding: 15px;
    border-radius: 10px;
    margin-top: 60px;
    margin-bottom: 20px;
    border: 2px dashed #bdc3c7;
    text-align: center;
}}

.stButton > button {{
    background-color: #27ae60;
    color: white;
    padding: 14px 30px;
    font-size: 20px;
    border-radius: 12px;
    border: none;
    transition: background-color 0.3s ease, transform 0.2s ease;
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
    display: block;
    margin: 0 auto; /* Centers the button */
    cursor: pointer;
}}

.stButton > button:hover {{
    background-color: #1e8449;
    transform: translateY(-4px); /* Adds hover effect for more interactivity */
}}


.image-preview {{
    display: flex;
    justify-content: center;
    margin-top: 20px;
    margin-bottom: 10px;
}}

.result-title {{
    font-size: 26px;
    font-weight: bold;
    color: #2980b9;
    margin-top: 30px;
}}

footer {{
    visibility: hidden;
}}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown(f"""
<div class="title-section">
    <img src="data:image/png;base64,{logo_base64}" class="logo" alt="Logo">
    <div class="main-title">Med Detect AI: Vital Image Analysis</div>
</div>
<div class="subheader">An intelligent assistant for identifying medical image patterns</div>
""", unsafe_allow_html=True)

# ---------------- UPLOAD IMAGE ----------------
# uploaded_file = st.file_uploader("Upload a medical image (JPEG, PNG)", type=["png", "jpg", "jpeg"], label_visibility="collapsed")

# # # File uploader
# if uploaded_file:
#     st.markdown('<div class="image-preview">', unsafe_allow_html=True)
#     st.markdown('<h4 style="text-align:center;">Uploaded Image -</h4>', unsafe_allow_html=True)
#     st.image(uploaded_file, width=70, caption="Uploaded Medical Image")  # Reduced from 350 to 250
#     st.markdown('</div>', unsafe_allow_html=True)

#     # st.image(uploaded_file, width=150)  # Adjusted width smaller
#     # st.markdown('</div>', unsafe_allow_html=True)

# ---------------- UPLOAD IMAGE ----------------
uploaded_file = st.file_uploader("Upload a medical image (JPEG, PNG)", type=["png", "jpg", "jpeg"], label_visibility="collapsed")

if uploaded_file:
    st.markdown("""
    <div style="display: flex; align-items: center; justify-content: space-between; margin-top: 20px; margin-bottom: 20px;">
        <h5 style="margin: 0;">Uploaded Image -</h5>
        <img src="data:image/jpeg;base64,{}" style="width: 70px; height: auto; border-radius: 10px; box-shadow: 0px 0px 8px rgba(0,0,0,0.1);" />
    </div>
    """.format(base64.b64encode(uploaded_file.getvalue()).decode()), unsafe_allow_html=True)


# ---------------- SUBMIT + ANALYSIS ----------------
st.markdown('<div style="display: flex; justify-content: center; margin-top: 20px;">', unsafe_allow_html=True)
submit = st.button("🔍 Generate the Analysis")
st.markdown('</div>', unsafe_allow_html=True)

if submit:
    if uploaded_file:
        image_data = uploaded_file.getvalue()
        image_parts = [{"mime_type": "image/jpeg", "data": image_data}]
        prompt_parts = [image_parts[0], system_prompt]

        with st.spinner("Analyzing image with AI..."):
            response = model.generate_content(prompt_parts)

        if response:
            st.markdown('<div class="result-title">🩺 Analysis Report:</div>', unsafe_allow_html=True)
            st.success(response.text)

            # Auto-scroll to bottom after displaying response
            st.markdown("""
                <script>
                window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});
                </script>
            """, unsafe_allow_html=True)
    else:
        st.warning("Please upload an image before generating the analysis.")

