def recursive_reverse_str(text: str) -> str:
    """Return the reversed string using recursion."""
    
    if len(text) <= 1:
        return text
        
    return recursive_reverse_str(text[1:]) + text[0]
    
if __name__ == "__main__":
    
    print(recursive_reverse_str("behruz"))