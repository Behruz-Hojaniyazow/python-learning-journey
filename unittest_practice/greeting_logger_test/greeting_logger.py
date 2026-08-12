def log_greeting(name, file_path="greetings.txt"):
    """Write a greeting message for the given name to a file."""
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(f"Hello, {name}!\n")
    return True