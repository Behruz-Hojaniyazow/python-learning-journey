names = [' behrUz', '  mahmuT ', 'NuRiya ']
clean_names = [name.strip().title() for name in names]
print(', '.join(clean_names))