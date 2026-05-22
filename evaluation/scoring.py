import google.generativeai as genai

from utils.helpers import GEMINI_API_KEY
from prompts.prompt_templates import (
    AI_EVALUATION_PROMPT,
    PROMPT_OPTIMIZATION_TEMPLATE
)

# Configure Gemini API

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")


def calculate_total_score(scores):
    """
    Calculates total score from metric scores.
    """

    return sum(scores.values())


def get_best_response(response_totals):
    """
    Returns best-performing response.
    """

    best_response = max(response_totals, key=response_totals.get)

    return best_response


def get_weakest_response(response_totals):
    """
    Returns weakest-performing response.
    """

    weakest_response = min(response_totals, key=response_totals.get)

    return weakest_response


def generate_ai_feedback(prompt, response):

    evaluation_prompt = f"""
    Evaluate the following AI response.

    User Prompt:
    {prompt}

    AI Response:
    {response}

    Provide:
    1. Clarity Analysis
    2. Accuracy Analysis
    3. Completeness Analysis
    4. Improvement Suggestions
    """

    try:
        model = genai.GenerativeModel("gemini-2.0-flash")

        response = model.generate_content(evaluation_prompt)

        return response.text

    except Exception as e:

        fallback_feedback = f"""
AI Evaluation Service Temporarily Unavailable.

Fallback Evaluation Summary:
- Response appears structurally valid.
- Manual review recommended for factual accuracy.
- Consider improving clarity and completeness.
- Add more detailed examples and structured formatting.

System Note:
API quota or connectivity issue detected.
"""

        return fallback_feedback


def optimize_prompt(user_prompt):

    optimization_prompt = PROMPT_OPTIMIZATION_TEMPLATE.format(
        user_prompt=user_prompt
    )

    try:

        model = genai.GenerativeModel("gemini-2.0-flash")

        response = model.generate_content(optimization_prompt)

        return response.text

    except Exception as e:

        fallback_optimization = f"""
Prompt Optimization Summary:

Detected Issues:
- Prompt may be too broad or vague.
- Missing output constraints.
- Additional context may improve response quality.

Recommended Improvements:
- Specify desired output format.
- Add clearer instructions.
- Mention expected detail level.
- Define target audience if applicable.

Example Improved Prompt:
'Provide a detailed explanation about {user_prompt} for beginners using simple language, structured bullet points and practical examples.'
"""
        return fallback_optimization
