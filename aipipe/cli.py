import os
import sys
import click
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)

def process_batch(text, prompt, model, temperature, max_tokens):
    """Process a batch of text data"""
    try:
        system_prompt = os.getenv("AIPIPE_SYSTEM_PROMPT", "You are a data processing assistant. Process data only. No explanations.")
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"{prompt}\n\n{text}"}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        click.echo(f"Processing error: {str(e)}", err=True)
        return None

@click.command()
@click.argument("prompt_arg", required=False)
@click.option("--prompt", "-p", help="Prompt for processing text")
@click.option("--prompt-file", "-f", type=click.Path(exists=True), help="Path to file containing the prompt")
@click.option("--model", "-m", default=lambda: os.getenv("AIPIPE_MODEL", "gpt-4o-mini"), help="AI model to use")
@click.option("--temperature", "-t", type=float, default=lambda: float(os.getenv("AIPIPE_TEMPERATURE", "0.7")), help="Output randomness (0-1)")
@click.option("--max-tokens", type=int, default=lambda: int(os.getenv("AIPIPE_MAX_TOKENS", "2000")), help="Maximum output length")
@click.option("--batch", "-b", is_flag=True, help="Enable batch processing mode")
def main(prompt_arg, prompt, prompt_file, model, temperature, max_tokens, batch):
    """AI Pipeline Processing Tool"""
    # Use positional argument as prompt if provided
    if prompt_arg:
        prompt = prompt_arg
    
    if not prompt and not prompt_file:
        click.echo("Error: Must provide a prompt or prompt file", err=True)
        sys.exit(1)

    if prompt_file:
        with open(prompt_file, "r") as f:
            prompt = f.read().strip()

    if not prompt:
        click.echo("Error: Prompt cannot be empty", err=True)
        sys.exit(1)

    # Read from standard input
    input_text = sys.stdin.read().strip()
    if not input_text:
        click.echo("Error: No input data", err=True)
        sys.exit(1)

    # Split input by lines
    lines = input_text.split("\n")
    
    # Batch processing
    if batch:
        # Process line by line in batch mode
        for line in lines:
            if line.strip():  # Skip empty lines
                result = process_batch(line, prompt, model, temperature, max_tokens)
                if result:
                    click.echo(result)
    else:
        # Process entire input in non-batch mode
        result = process_batch(input_text, prompt, model, temperature, max_tokens)
        if result:
            click.echo(result)

if __name__ == "__main__":
    main() 