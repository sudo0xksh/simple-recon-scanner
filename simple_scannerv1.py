import requests

print("=========================================")
print("Simple Scanner v1\n")

key = input("Shodan API key (enter to skip): ").strip()
target = input("Enter IP or domain: ").strip()

if key:
    print("\n--- Shodan Lookup ---")
    url = f"https://api.shodan.io/shodan/host/{target}?key={key}"
    try:
        r = requests.get(url)
        print("Status:", r.status_code)
        print(r.text[:500])
    except Exception as e:
        print("Shodan request failed:", e)
else:
    print("\nSkipping Shodan (no API key).")

print("\n--- Hackertarget Nmap ---")
url = f"https://api.hackertarget.com/nmap/?q={target}"
try:
    r = requests.get(url)
    print("Status:", r.status_code)
    print(r.text[:500])
except Exception as e:
    print("Nmap failed:", e)

print("\n--- IP-API Info ---")
url = f"http://ip-api.com/json/{target}"
try:
    r = requests.get(url)
    print("Status:", r.status_code)
    print(r.text)
except Exception as e:
    print("IP-API failed:", e)

print("\n=========================================")
print("Developed by sudo_0xksh")