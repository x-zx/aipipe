# AIPipe

AIPipe is a powerful command-line tool for processing pipeline data through AI prompts. It supports both multi-line and line-by-line data processing, allows specifying prompts via parameters or files, and supports configuring AI model parameters.

## Installation

```bash
pip install aipipe
```

## Usage

### Basic Usage

```bash
# Specify prompt via command line parameter
cat input.txt | aipipe "Translate the following text to English"

# Use prompt file
cat input.txt | aipipe --prompt-file prompt.txt

# Specify AI model
cat input.txt | aipipe --model "gpt-4" --prompt "Summarize the following text"
```

### Configuration

You can configure the OpenAI API key in the following ways:

1. Environment Variables:
```bash
# Set directly in terminal
export OPENAI_API_KEY=your_api_key

# Set permanently in .bashrc or .zshrc
echo 'export OPENAI_API_KEY=your_api_key' >> ~/.bashrc
source ~/.bashrc
```

2. `.env` file:
The program automatically looks for `.env` files in:
- Current working directory
- User home directory (`~/.env`)

Create a `.env` file in any of these locations with the following content:
```
OPENAI_API_KEY=your_api_key
```

3. Other configurable environment variables:
- `OPENAI_BASE_URL`: OpenAI API base URL (default: "https://api.openai.com/v1")
- `AIPIPE_MODEL`: Default AI model to use (default: "gpt-4o-mini")
- `AIPIPE_TEMPERATURE`: Default temperature setting for model outputs (default: 0.7)
- `AIPIPE_MAX_TOKENS`: Default maximum number of tokens in model responses (default: 2000)
- `AIPIPE_SYSTEM_PROMPT`: Default system prompt for the AI model

### Parameters

- `--prompt`: Directly specify the prompt
- `--prompt-file`: Specify a file containing the prompt
- `--model`: Specify the AI model to use (default: "gpt-3.5-turbo")
- `--temperature`: Control output randomness (0-1, default: 0.7)
- `--max-tokens`: Control maximum output length
- `--batch`: Enable batch mode for line-by-line data processing (default: false)

## Examples

### Line-by-line Processing

```bash
echo -e "First line\nSecond line" | aipipe --prompt "Translate the following text to English"
```

### Batch Processing

```bash
echo -e "First line\nSecond line\nThird line" | aipipe --prompt "Summarize the following text" --batch
```

## License

MIT 