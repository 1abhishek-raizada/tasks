import subprocess

def call_llama(prompt: str) -> str:
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3"],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=120  # increased timeout for longer prompts
        )
        if result.returncode != 0:
            return f"Error: Ollama failed with code {result.returncode}: {result.stderr.strip()}"
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "Error: LLaMA model timed out. Please try again."
    except FileNotFoundError:
        return "Error: Ollama CLI not found. Please ensure it's installed and in your PATH."
    except Exception as e:
        return f"Unexpected error: {str(e)}"

def zero_shot_urgency(message: str) -> str:
    prompt = f"""
Classify the urgency of the following customer support ticket as 'low', 'medium', or 'high'.
Only respond with one word: low, medium, or high.

Message: {message}
Urgency:
"""
    return call_llama(prompt)

def few_shot_routing(message: str) -> str:
    prompt = f"""
Classify the department for the following support ticket.

Respond with one of the following: 'Shipping', 'Technical Support', 'Billing', or 'Other'.
Only respond with one of these values.

Message: {message}
Department:
"""
    return call_llama(prompt)

def cot_analysis(message: str) -> str:
    prompt = f"""
Analyze the following support ticket and explain whether it should be considered urgent or not. Give a step-by-step reasoning.

Message: {message}
Reasoning:
"""
    return call_llama(prompt)

def run_all_prompts(message: str) -> dict:
    return {
        "urgency": zero_shot_urgency(message),
        "department": few_shot_routing(message),
        "chain_of_thought": cot_analysis(message)
    }