import sys
import argparse
from concurrent.futures import ThreadPoolExecutor
import requests

requests.packages.urllib3.disable_warnings()

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def check_parameter(url, param, base_length):
    test_url = f"{url}?{param}=test_value_123" if "?" not in url else f"{url}&{param}=test_value_123"
    try:
        response = requests.get(test_url, headers=HEADERS, timeout=5, verify=False)
        # If the response length changes significantly compared to the base URL, the parameter might be valid
        if len(response.text) != base_length:
            print(f"[+] Found potential parameter: {test_url} (Length: {len(response.text)} vs Base: {base_length})")
            return param
    except Exception as e:
        pass
    return None

def main():
    parser = argparse.ArgumentParser(description="BountyParamScanner - Hidden Parameter Brute-forcer for Web Bug Bounty")
    parser.add_argument("-u", "--url", required=True, help="Target URL to scan (e.g., https://example.com)")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to the parameter wordlist file")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Number of concurrent threads (Default: 10)")
    
    args = parser.parse_args()

    print(f"[*] Getting base response from: {args.url}")
    try:
        base_response = requests.get(args.url, headers=HEADERS, timeout=5, verify=False)
        base_length = len(base_response.text)
        print(f"[+] Base Response Length: {base_length}")
    except Exception as e:
        print(f"[-] Cannot connect to the target URL: {str(e)}")
        sys.exit(1)

    try:
        with open(args.wordlist, "r") as f:
            parameters = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"[-] Error reading wordlist: {str(e)}")
        sys.exit(1)

    print(f"[+] Loaded {len(parameters)} parameters from wordlist.")
    print("[+] Scanning started... Please wait.")

    discovered_params = []
    
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = [executor.submit(check_parameter, args.url, param, base_length) for param in parameters]
        for future in futures:
            result = future.result()
            if result:
                discovered_params.append(result)

    print("\n" + "="*40)
    print(f"[+] SCAN FINISHED. Total discovered parameters: {len(discovered_params)}")
    print("="*40)
    for p in discovered_params:
        print(f"- {p}")

if __name__ == "__main__":
    main()
