AI_EVALUATION_PROMPT = """
You are an AI Response Evaluator.

Analyze the following AI-generated response.

Evaluate:
1. Clarity
2. Relevance
3. Completeness
4. Structure
5. Instruction Following

Provide:
- strengths
- weaknesses
- improvement suggestions

User Prompt:
{user_prompt}

AI Response:
{ai_response}
"""

PROMPT_OPTIMIZATION_TEMPLATE = """
You are a Prompt Optimization Specialist.

Analyze the following user prompt.

Evaluate:
1. Clarity
2. Specificity
3. Context Quality
4. Instruction Quality
5. Missing Constraints

Provide:
- Prompt weaknesses
- Suggested improvements
- Optimized version of the prompt

User Prompt:
{user_prompt}
"""
