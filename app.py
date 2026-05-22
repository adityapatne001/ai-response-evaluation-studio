import streamlit as st
from evaluation.metrics import EVALUATION_METRICS
from evaluation.scoring import (
    calculate_total_score,
    get_best_response,
    get_weakest_response,
    generate_ai_feedback,
    optimize_prompt
)

from utils.helpers import (
    save_evaluation_history,
    display_evaluation_monitoring_panel,
    generate_evaluation_report
)

# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="AI Response Evaluation Studio",
    layout="wide"
)

# -----------------------------------
# MAIN TITLE
# -----------------------------------

st.title("AI Response Evaluation & Prompt Optimization Studio")
st.caption(
    "AI Evaluation | Prompt QA | LLM Review | Workflow Monitoring | Operational Reporting"
)

# -----------------------------------
# SIDEBAR NAVIGATION
# -----------------------------------

st.sidebar.title("AI Workflow Navigation")

st.sidebar.markdown("""
### Sections
- Prompt Input
- Response Evaluation
- AI Feedback
- Prompt Optimization
- Evaluation Monitoring
- Report Generation
""")

st.sidebar.markdown("---")

st.sidebar.subheader("Project Overview")

st.sidebar.info(
    """
    This application simulates AI evaluation workflows by:
    
    • Comparing AI-generated responses
    
    • Scoring outputs using structured metrics
    
    • Generating AI-assisted evaluation feedback
    
    • Optimizing prompt quality
    
    • Monitoring evaluation performance
    
    • Exporting operational reports
    """
)

# -----------------------------------
# WORKFLOW STATUS
# -----------------------------------

st.success("AI Evaluation Workflow System Active")

st.markdown(
    "Evaluate, compare and optimize AI-generated responses using structured scoring metrics."
)

# -----------------------------------
# USER PROMPT INPUT
# -----------------------------------

st.markdown("---")
st.header("Step 1: Enter Original Prompt")

user_prompt = st.text_area(
    "Enter the prompt/question given to the AI models:",
    height=120,
    placeholder="Example: Explain climate change in simple terms."
)

# -----------------------------------
# AI RESPONSE INPUTS
# -----------------------------------

st.markdown("---")
st.header("Step 2: Paste AI Responses")

response_1 = st.text_area(
    "AI Response 1",
    height=200,
    placeholder="Paste first AI-generated response here..."
)

response_2 = st.text_area(
    "AI Response 2",
    height=200,
    placeholder="Paste second AI-generated response here..."
)

response_3 = st.text_area(
    "AI Response 3",
    height=200,
    placeholder="Paste third AI-generated response here..."
)

# -----------------------------------
# DISPLAY EVALUATION METRICS
# -----------------------------------

st.markdown("---")
st.header("Step 3: Evaluation Metrics")

with st.expander("View Evaluation Metric Definitions"):

    st.markdown("""
    ### Evaluation Metrics Explained

    **Clarity**
    - Measures readability and understandability.

    **Accuracy**
    - Evaluates factual correctness.

    **Completeness**
    - Checks whether the response fully answers the prompt.

    **Structure**
    - Measures formatting and logical organization.

    **Relevance**
    - Evaluates alignment with the original prompt.
    """)

for metric in EVALUATION_METRICS:
    st.write(f"✅ {metric}")

# -----------------------------------
# RESPONSE 1 SCORING
# -----------------------------------

st.markdown("---")
st.header("Step 4: Score AI Response 1")

response_1_scores = {}

for metric in EVALUATION_METRICS:

    response_1_scores[metric] = st.slider(
        f"Response 1 - {metric}",
        min_value=1,
        max_value=5,
        value=3
    )

response_1_total = calculate_total_score(response_1_scores)

st.success(f"Response 1 Total Score: {response_1_total}")

# -----------------------------------
# RESPONSE 2 SCORING
# -----------------------------------

st.markdown("---")
st.header("Step 5: Score AI Response 2")

response_2_scores = {}

for metric in EVALUATION_METRICS:

    response_2_scores[metric] = st.slider(
        f"Response 2 - {metric}",
        min_value=1,
        max_value=5,
        value=3
    )

response_2_total = calculate_total_score(response_2_scores)

st.success(f"Response 2 Total Score: {response_2_total}")

# -----------------------------------
# RESPONSE 3 SCORING
# -----------------------------------

st.markdown("---")
st.header("Step 6: Score AI Response 3")

response_3_scores = {}

for metric in EVALUATION_METRICS:

    response_3_scores[metric] = st.slider(
        f"Response 3 - {metric}",
        min_value=1,
        max_value=5,
        value=3
    )

response_3_total = calculate_total_score(response_3_scores)

st.success(f"Response 3 Total Score: {response_3_total}")

# -----------------------------------
# RESPONSE COMPARISON SUMMARY
# -----------------------------------

st.markdown("---")
st.header("Step 7: AI Response Comparison Summary")

response_totals = {
    "Response 1": response_1_total,
    "Response 2": response_2_total,
    "Response 3": response_3_total
}

best_response = get_best_response(response_totals)

weakest_response = get_weakest_response(response_totals)

# -----------------------------------
# DISPLAY RESPONSE SCORES
# -----------------------------------

st.subheader("Response Score Overview")

for response_name, total_score in response_totals.items():

    st.write(f"{response_name}: {total_score}")

# -----------------------------------
# BEST RESPONSE
# -----------------------------------

st.success(
    f"🏆 Best Performing Response: {best_response}"
)

# -----------------------------------
# WEAKEST RESPONSE
# -----------------------------------

st.warning(
    f"⚠️ Weakest Performing Response: {weakest_response}"
)

# -----------------------------------
# SAVE EVALUATION HISTORY
# -----------------------------------

if st.button("Save Evaluation History"):

    save_evaluation_history(
        user_prompt,
        response_1_total,
        response_2_total,
        response_3_total,
        best_response,
        weakest_response
    )

    st.success("Evaluation history saved successfully.")

# -----------------------------------
# AI-ASSISTED EVALUATION FEEDBACK
# -----------------------------------

st.markdown("---")
st.header("Step 8: AI-Assisted Evaluation Feedback")

if st.button("Generate AI Evaluation Feedback"):

    with st.spinner("Generating AI evaluation feedback..."):

        feedback_1 = generate_ai_feedback(
            user_prompt,
            response_1
        )

        feedback_2 = generate_ai_feedback(
            user_prompt,
            response_2
        )

        feedback_3 = generate_ai_feedback(
            user_prompt,
            response_3
        )

    # -----------------------------------
    # DISPLAY FEEDBACK
    # -----------------------------------

    st.subheader("AI Feedback for Response 1")

    st.write(feedback_1)

    st.subheader("AI Feedback for Response 2")

    st.write(feedback_2)

    st.subheader("AI Feedback for Response 3")

    st.write(feedback_3)

# -----------------------------------
# PROMPT OPTIMIZATION ENGINE
# -----------------------------------

st.markdown("---")
st.header("Step 9: Prompt Optimization Engine")

if st.button("Analyze & Optimize Prompt"):

    with st.spinner("Analyzing prompt quality..."):

        optimized_prompt_feedback = optimize_prompt(user_prompt)

    st.subheader("Prompt Optimization Feedback")

    st.write(optimized_prompt_feedback)

# -----------------------------------
# AI EVALUATION MONITORING PANEL
# -----------------------------------

st.markdown("---")
st.header("Step 10: AI Evaluation Monitoring Panel")

if st.button("Show Evaluation Monitoring Panel"):

    display_evaluation_monitoring_panel()

# -----------------------------------
# EXPORT & REPORT GENERATION
# -----------------------------------

st.markdown("---")
st.header("Step 11: Export & Report Generation")

if st.button("Generate Evaluation Report"):

    report = generate_evaluation_report()

    st.subheader("Evaluation Report")

    st.text(report)

    # -----------------------------------
    # DOWNLOAD REPORT
    # -----------------------------------

    st.download_button(
        label="Download Evaluation Report",
        data=report,
        file_name="evaluation_report.txt",
        mime="text/plain"
    )

# -----------------------------------
# FOOTER
# -----------------------------------

st.markdown("---")

st.caption(
    "Built using Python, Streamlit, Pandas and Gemini API for AI workflow evaluation and prompt optimization."
)
