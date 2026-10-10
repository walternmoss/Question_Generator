import os
import streamlit as st
from generator import generate_batch_assessments

st.set_page_config(
    page_title="ISU Academic Assessment Generator",
    page_icon="📚",
    layout="centered"
)

st.title("📚 ISU AI Assessment & Tagged Question Bank Generator")
st.markdown("Upload lecture slide decks or study guides to generate granular, difficulty-tagged question banks for automated Socratic AI ingestion.")

# Sidebar Configurations
st.sidebar.header("Configuration Panel")
api_key_input = st.sidebar.text_input("Gemini API Key", type="password", help="Optional override if not defined in Streamlit secrets.")

st.markdown("---")

# Main Interface Fields supporting batch upload
uploaded_files = st.file_uploader(
    "1. Upload Source Documents (Queue multiple PDF, PPTX, TXT, MD files)",
    type=["pdf", "pptx", "txt", "md"],
    accept_multiple_files=True
)

st.markdown("### 2. Granular Difficulty Distribution")
col_e, col_m, col_h = st.columns(3)
with col_e:
    easy_count = st.number_input("Easy Questions", min_value=0, max_value=20, value=5, step=1)
with col_m:
    med_count = st.number_input("Medium Questions", min_value=0, max_value=20, value=5, step=1)
with col_h:
    hard_count = st.number_input("Hard Questions", min_value=0, max_value=20, value=5, step=1)

total_q = easy_count + med_count + hard_count
st.info(f"Total Questions per Document: **{total_q}**")

col1, col2 = st.columns(2)

with col1:
    q_type = st.selectbox(
        "3. Question Type",
        ["Short Answer", "Multiple Choice", "True/False", "Fill in the Blank"]
    )
    
    num_choices = 4
    if q_type == "Multiple Choice":
        num_choices = st.slider("Number of Answer Choices", min_value=3, max_value=6, value=4)

with col2:
    output_format = st.selectbox(
        "4. Output Format", 
        ["Markdown (.md) with Tags", "Structured XML (.xml)", "Plain Text"]
    )
    include_answer_key = st.checkbox("5. Include Answer Key", value=True)

st.markdown("---")

generate_btn = st.button("Process Question Bank Queue", type="primary", use_container_width=True)

if generate_btn:
    if not uploaded_files:
        st.error("Please upload at least one source document before processing the queue.")
    elif total_q == 0:
        st.error("Please configure at least one question across the difficulty tiers.")
    else:
        if api_key_input:
            os.environ["GEMINI_API_KEY"] = api_key_input
            
        try:
            status_text = st.empty()
            progress_bar = st.progress(0)
            
            def update_progress(current, total, filename):
                percent = int((current / total) * 100)
                progress_bar.progress(percent)
                status_text.text(f"Processing file {current + 1} of {total}: {filename}...")

            zip_bytes = generate_batch_assessments(
                uploaded_files=uploaded_files,
                easy_count=easy_count,
                med_count=med_count,
                hard_count=hard_count,
                q_type=q_type,
                num_choices=num_choices,
                include_answer_key=include_answer_key,
                output_format=output_format,
                progress_callback=update_progress
            )
            
            progress_bar.progress(100)
            status_text.text("Batch queue processing complete!")
            st.success(f"Successfully generated tagged question banks for {len(uploaded_files)} documents!")
            
            file_ext = "xml" if output_format == "Structured XML (.xml)" else ("txt" if output_format == "Plain Text" else "md")
            
            st.download_button(
                label="Download All Tagged Question Banks (.zip)",
                data=zip_bytes,
                file_name="tagged_question_banks.zip",
                mime="application/zip",
                use_container_width=True
            )
            
        except Exception as e:
            st.error(f"An error occurred during batch processing: {e}")
