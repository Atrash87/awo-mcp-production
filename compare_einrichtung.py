import pandas as pd
from pathlib import Path
from rdflib import Graph, Namespace, URIRef

# 1. Load CSV
csv_path = Path("data/einrichtungSchema.csv")
df = pd.read_csv(csv_path, encoding="utf-8")
csv_iris = set(df["iri"].dropna().astype(str))

# 2. Parse Turtle and collect all org:OrganizationalUnit IRIs
g = Graph()
g.parse("directory.ttl", format="turtle")

# Use the exact IRI for the type
org_type = URIRef("http://www.w3.org/ns/org#OrganizationalUnit")

org_iris = set()
# Find all subjects that have the type org:OrganizationalUnit
for s, p, o in g.triples((None, None, org_type)):
    # Now s is a subject that has the type org:OrganizationalUnit
    org_iris.add(str(s))

print(f"Found {len(org_iris)} org:OrganizationalUnit records in Turtle")

# 3. Normalise to fragments
def fragment(iri):
    return iri.split("#")[-1] if "#" in iri else iri

csv_fragments = {fragment(iri) for iri in csv_iris}
org_fragments = {fragment(iri) for iri in org_iris}

# 4. Find differences
only_in_csv = csv_fragments - org_fragments
only_in_ttl = org_fragments - csv_fragments

print(f"CSV count: {len(csv_iris)}")
print(f"Turtle count: {len(org_iris)}")

if only_in_csv:
    print(f"\nOnly in CSV (should be exactly 2):")
    for frag in sorted(only_in_csv):
        print(f"  {frag}")

if only_in_ttl:
    print(f"\nOnly in Turtle (should be 0):")
    for frag in sorted(only_in_ttl):
        print(f"  {frag}")

# 5. If only_in_csv has exactly 2 items, show their full rows
if len(only_in_csv) == 2:
    print("\n🔍 The two extra CSV entries:")
    for frag in sorted(only_in_csv):
        # Try to find the full IRI in CSV
        matching_rows = df[df["iri"].str.contains(frag, regex=False)]
        print(f"\n{frag}:")
        if not matching_rows.empty:
            print(matching_rows[["iri", "schema:name", "schema:category"]].to_string(index=False))
        else:
            print("  (not found in CSV)")