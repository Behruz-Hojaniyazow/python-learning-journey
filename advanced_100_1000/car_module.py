def car_info(name: str, color: str, cost: int) -> str:
  """Return formatted car information"""
  return (
      f"Brand name: {name.title()}\n"
      f"Color: {color.title()}\n"
      f"Price: ${cost}\n"
  )