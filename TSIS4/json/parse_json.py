import os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))

json_path = os.path.join(current_dir, "sample-data.json")

with open(json_path) as file:
    data = json.load(file)

interfaces = data.get("imdata", [])

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<5}")
print("-" * 80)

for item in interfaces:
    attributes = item.get("l1PhysIf", {}).get("attributes", {})
    dn = attributes.get("dn", "")
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "inherit")
    mtu = attributes.get("mtu", "")
    print(f"{dn:<50} {description:<20} {speed:<7} {mtu:<5}")
