
# Medical Image Detection with Vital Image Analytics

This application leverages Google’s generative AI model to analyze medical images and provide insights into potential health issues, including anomalies and diseases. It helps users upload medical images for analysis, offering detailed reports and suggestions based on the content of the images. 

## Features:
- **Image Upload**: Users can upload medical images (e.g., PNG, JPG, JPEG).
- **Medical Image Analysis**: The app processes the uploaded image using the `gemini-1.5-pro-latest` AI model.
- **Structured Analysis**: The system generates a detailed report in four structured sections: 
  - **Detailed Analysis**
  - **Findings Report**
  - **Recommendations and Next Steps**
  - **Treatment Suggestions**
- **Safety**: Implements safety settings to ensure that harmful content, such as hate speech, harassment, or explicit material, is blocked.

## How It Works:
1. **Image Upload**: Upload a medical image.
2. **Generate Analysis**: After uploading, press the "Generate the Analysis" button.
3. **AI Analysis**: The system uses the Google generative AI model to process the image and produce a medical report.
4. **Display Results**: The generated analysis is displayed with clear headings and recommendations.

## Technologies Used:
- **Streamlit**: For building the web application interface.
- **Google Generative AI**: For analyzing and generating content based on the uploaded medical image.
- **Python**: The backend logic, including image processing and AI interaction.
- **API Key**: Secure integration with Google's generative AI using an API key (to be stored in `api_key.py`).

## Setup:
1. Clone the repository.
2. Install required packages: 
   ```
   pip install -r requirements.txt
   ```
3. Set up your Google Generative AI API key in the `api_key.py` file.
4. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Disclaimer:
- This tool is intended to assist in medical image analysis but **should not replace professional medical advice**. Always consult with a doctor before making any decisions.

## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
