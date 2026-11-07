# My First AI - Blocks Hackers
logs = ["FAILED login from 45.33.22.101", "SUCCESS login from 10.2.3.4", "FAILED login from 45.33.22.101"]
for log in logs:
    if "FAILED" in log and "45.33.22.101" in log:
        print("ALERT: Hacker Found! Blocking IP")
