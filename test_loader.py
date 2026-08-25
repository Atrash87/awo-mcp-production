from src.data_loader import DataLoader


loader = DataLoader("data")

datasets = loader.load_all()

for name, dataframe in datasets.items():
    print("=" * 70)
    print(name)
    print("=" * 70)

    print(f"Rows: {len(dataframe)}")
    print(f"Columns: {len(dataframe.columns)}")
    print()

    print("Columns:")
    for column in dataframe.columns:
        print(f"  - {column}")

    print()

    print("First row:")
    print(dataframe.iloc[0].to_dict())

    print()