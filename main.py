from loaders.registry import DatasetRegistry

# Initialize the registry using the local datasets.csv
reg = DatasetRegistry("datasets.csv")

# 1. Print a human-readable summary of a specific dataset
print(reg.pretty(1))

# 2. Access specific links and metadata
url = reg.link(1)    # main download link
meta = reg.get(31)   # ExDark metadata

print(f"Dataset URL: {url}")
print(f"Dataset Name: {meta['NAME']}")
print(f"Dataset Description: {meta['DESCRIPTION']}")
print(f"Dataset Size: {meta['SIZE']}")

print("-" * 30)

# 3. Demonstrate the new Search Feature (Your addition!)
print("Searching for 'underwater' datasets...")
underwater_results = reg.search("underwater")
for ds in underwater_results:
    print(f"Found: {ds['NAME']} (Index: {ds['INDEX']})")