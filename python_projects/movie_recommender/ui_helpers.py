"""
Console presentation helpers for the Movie Recommender application.

This module contains small, single-purpose functions responsible only
for how information is displayed in the terminal (headers, sections,
error/warning/info messages, and separators). By isolating all print
formatting here, the UI-flow modules (e.g., `main.py`) can focus on
control flow and user interaction logic, while any future changes to
the visual style of the application (icons, borders, spacing) only
need to be made in this single module.

None of the functions in this module return a value; they exist purely
for their side effect of writing formatted output to standard output.
"""

def print_header(title: str, icon: str = "🎬") -> None:
    """
    Print a bordered, boxed header for a major screen or section.

    Renders the given title inside a fixed-width box drawn with
    Unicode box-drawing characters, preceded by an icon. Intended for
    top-level screens such as the main menu or a feature's entry point
    (e.g., "ADD MOVIE", "RECOMMEND MOVIE").

    Args:
        title (str): The header text to display.
        icon (str, optional): An emoji or symbol shown before the
            title. Defaults to "🎬".

    Returns:
        None
    """
    
    print("╔" + "═" * 42 + "╗")
    print(f"║ {icon} {title:<37}║")
    print("╚" + "═" * 42 + "╝")
    
def print_section(title: str, icon: str = "📋") -> None:
    """
    Print a lightweight, single-line section divider with a title.

    Used to introduce a sub-part of a screen (e.g., a list of genres,
    a group of search results) without the visual weight of a full
    `print_header` box.

    Args:
        title (str): The section title to display.
        icon (str, optional): An emoji or symbol shown before the
            title. Defaults to "📋".

    Returns:
        None
    """
    
    print()
    print(f"┌─ {icon} {title} " + "─" * max(1, 34 - len(title)) + "┐")
    
def print_error(message: str) -> None:
    """
    Print a message indicating an invalid or failed operation.

    Args:
        message (str): The error message to display to the user.

    Returns:
        None
    """
    
    print(f"\n❌️ {message}")
    
def print_warning(message: str) -> None:
    """
    Print a message indicating a non-critical, cautionary condition.

    Args:
        message (str): The warning message to display to the user.

    Returns:
        None
    """
    
    print(f"\n⚠️ {message}")
    
def print_info(message: str) -> None:
    """
    Print a neutral, informational message to the user.

    Args:
        message (str): The informational message to display.

    Returns:
        None
    """
    
    print(f"ℹ️ {message}")
    
def print_separator() -> None:
    """
    Print a horizontal divider line used to visually separate content.

    Returns:
        None
    """
    
    print("─" * 42)
    
def print_back_msg() -> None:
    """
    Print a standard message indicating a return to the main menu.

    Displayed whenever the user chooses to exit a sub-menu (e.g., by
    entering '0' or 'stop') rather than completing an action.

    Returns:
        None
    """
    
    print("\n⬅️ Returning to the main menu...")