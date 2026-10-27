# BountyParamScanner

A fast, multithreaded Python command-line tool designed for Web Bug Bounty hunters and Ptesters to discover hidden URL parameters. 

By sending concurrent requests and analyzing changes in response length, this tool helps identify hidden inputs that could lead to vulnerabilities like IDOR, SSRF, XSS, or Privilege Escalation.

## Features
- **Multithreaded Speed:** Powered by Python's `ThreadPoolExecutor` for high-performance concurrent scanning.
- **Smart Detection:** Compares request results directly with the base URL response length to minimize false positives.
- **Customizable:** Easily adjust thread counts and supply your own parameter wordlists.

## Installation

Clone the repository to your local machine:
```bash
git clone https://github.com
cd BountyParamScanner
```

Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```

## Setup Wordlist

Before running the tool, make sure you have a parameter wordlist file (e.g., `params.txt`) in the same directory. You can create one with sensitive parameters like:
```text
debug
admin
test
dev
bypass
config
```

## Usage

Run the scanner by providing the target URL and the path to your parameter wordlist:

```bash
python run.py -u https://example.com -w params.txt
```

### Advanced Options

Increase the speed by changing the default thread count (e.g., using 20 threads):
```bash
python eun.py -u https://example.com -w params.txt -t 20
```

## Argument Details

- `-u`, `--url`: **(Required)** The target web URL you want to test.
- `-w`, `--wordlist`: **(Required)** Path to the text file containing the list of parameters.
- `-t`, `--threads`: *(Optional)* Number of concurrent threads to use (Default: 10).

## Documentation & Use Cases
For practical bug-hunting workflows, case studies, and advanced tips, visit our official tool documentation site: **https://yourdomain.com**

## License
This project is licensed under the MIT License - see the LICENSE file for details.
