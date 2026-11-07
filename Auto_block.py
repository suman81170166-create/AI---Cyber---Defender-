# Level 2 - Auto Blocker
def auto_block(ip, failed_count):
    if failed_count > 3:
        print(f"BLOCKED: {ip} is a hacker!")
        return True
    else:
        print(f"SAFE: {ip}")
        return False

# Test
auto_block("45.33.22.101", 5)
auto_block("10.2.3.4", 1)
