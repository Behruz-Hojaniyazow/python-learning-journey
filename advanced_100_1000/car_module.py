def car_info(name: str, color: str, cost: int) -> str:
  """Return formatted car information"""
  return (
      f"Brand name: {name.title()}\n"
      f"Car's color is {color.title()}\n"
      f"{name.title()} costs ${cost}\n"
  )