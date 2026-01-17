# Owasp-Api-Audit (OAA) 🛡️ 🏹

![License](https://img.shields.io/badge/license-MIT-red.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Type](https://img.shields.io/badge/Offensive-Security-black.svg)

**OWASP-API-Audit** is a professional-grade offensive security tool designed to identify critical vulnerabilities within the **OWASP API Security Top 10** framework. It specializes in Out-of-Band (OOB) interactions, advanced header injections, and logic-based endpoint fuzzing.

> **Note:** Manual analysis starts where automated tools fail. This tool is built for researchers who live in the terminal.

---

## ⚡ Core Capabilities

* **OOB Interaction Hunting:** Native support for `Interactsh`, `Burp Collaborator`, and `Webhook.site`.
* **SSRF Parameter Fuzzing:** Automated testing of 30+ high-risk parameters (`?url=`, `?dest=`, `?api=`, etc.).
* **Host Header Poisoning:** Tests for Host, X-Forwarded-Host, and X-HTTP-Host-Override misconfigurations.
* **CORS Policy Audit:** Identifies unsafe Origin reflections and Null-origin vulnerabilities.
* **WAF Bypass Simulation:** Rotates between mobile (iOS/Android) and desktop (Windows/Mac) User-Agents to evade basic signature-based detection.

---

## 🛠️ Installation & Requirements

```bash
# Clone the repository
git clone https://github.com/can0x01/Owasp-Api-Audit

# Navigate to directory
cd Owasp-Api-Audit

# Install dependencies
pip3 install requirements.txt

🚀 Execution

The tool is interactive. It will request your OOB server address upon execution to ensure all out-of-band hits are tracked.

python3 api_audit.py -t [https://api.target-system.com](https://api.target-system.com)

📟 Terminal Output Preview

[!] OWASP-API-Audit Initialized.
[?] Enter your OOB Server (e.g. xxxxx.oast.fun): 7t2p...oast.fun

[*] Target: [https://api.target-system.com](https://api.target-system.com)
[*] OOB: 7t2p...oast.fun
----------------------------------------
[*] Testing SSRF/OOB Parameters...
[+] Tested Param: redirect -> Check OOB.
[+] Tested Param: callback -> Check OOB.
[*] Fuzzing Host Headers...
[+] Header Injected: X-Forwarded-Host
[*] Auditing CORS Policy...
[CRITICAL] CORS Misconfiguration Detected!

📂 Project Structure

    api_audit.py: The core engine for vulnerability scanning.

    payloads.json: A curated list of offensive payloads and parameters.

    requirements.txt: Project dependencies.


⚖️ Legal Disclaimer

Usage of Owasp-Api-Audit for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.

Contact: ahmetcan0x01@gmail.com

Profile: @canmitm
