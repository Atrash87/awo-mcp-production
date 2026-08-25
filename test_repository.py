from src.data_loader import DataLoader
from src.data_repository import DataRepository


loader = DataLoader("data")
datasets = loader.load_all()

repository = DataRepository(datasets)


print("=" * 70)
print("1. COUNT FACILITIES")
print("=" * 70)

count = repository.count_facilities("Berlin")

print(f"Facilities in Berlin: {count}")


print("\n" + "=" * 70)
print("2. SEARCH FACILITIES")
print("=" * 70)

facilities = repository.search_facilities("Berlin")

for facility in facilities[:5]:
    print(facility)


print("\n" + "=" * 70)
print("3. FACILITY DETAILS")
print("=" * 70)

details = repository.get_facility_details(
    "Drehscheibe Kinder"
)

for facility in details:
    print(facility)


print("\n" + "=" * 70)
print("4. SEARCH SERVICES")
print("=" * 70)

services = repository.search_services("Suchtberatung")

for service in services[:10]:
    print(service)