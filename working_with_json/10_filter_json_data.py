import json
import logging

logging.basicConfig(level=logging.ERROR)

def create_auto_cars():
  """Function that return cars dict"""
  
  cars_info = {
    'camry' : {
      'color' : 'black',
      'price' : 15000,
      'type' : 'gasoline'
    },
    'corolla' : {
      'color' : 'white',
      'price' : 8000,
      'type' : 'electric'
    },
    'sienna' : {
      'color' : 'blue',
      'price' : 20000,
      'type' : 'gasoline'
    },
    'tacoma' : {
      'color' : 'green',
      'price' : 17000,
      'type' : 'electric'
    }
  }
  
  return cars_info
  
def save_cars(cars):
  """Function that saves cars info to the file"""
  
  if not cars:
    print(f"\nNothing found to save file")
    return
  
  filename = 'cars.json'
  
  with open(filename, 'w', encoding='utf-8') as file:
    json.dump(cars, file, indent=4)
    
    print(f"\n'{filename}' file saved successfully!")
    
def read_cars_info(cars):
  """Function that reads the car info from the file"""
  
  filename = 'cars.json'
  
  try:
    
    with open(filename, 'r', encoding='utf-8') as file:
      auto_cars = json.load(file)
    
  except FileNotFoundError:
    print(f"\n'{filename}' file not found, Please run the writer script first")
    
  except json.JSONDecodeError as e:
    logging.error(f"\nInvalid JSON format - {e}")
    
    auto_cars = cars
    
  except IOError as e:
    print(f"\nFile Error - {e}")
    
  except Exception as e:
    print(f"\nUnexpected Error occured - {e}")
    auto_cars = cars
    
  return auto_cars
  
def filter_cars(cars):
  """Function that filters the cars"""
  
  
  if not cars:
    print(f"\nNo car found to filter")
    return
  
  filtered_cars = {
    car: info for car, info in cars.items() if info["type"] == 'electric' and info['price'] <= 15000
  }
  
  for car, info in filtered_cars.items():
    print(f"Car: {car.upper()}")
    print(f" - Color: {info['color']}")
    print(f" - Price: {info['price']}")
    print(f" - Type: {info['type']}")
    print("-" * 20)
    
if __name__ == '__main__':
  print(f"\n--- The Program has started ---")
  
  # 1. We create car data in the form of a dictionary (dict)
  new_cars = create_auto_cars()
  
  # 2. We save the generated data to the 'cars.json' file
  save_cars(new_cars)
  
  # 3. We re-read the data from the file (if the file doesn't exist, 'new_cars' will be passed as a backup)
  file_streaming_cars = read_cars_info(new_cars)
  
  # 4. We filter the read data (Electric and Price <= 15000) and display it on the screen
  print(f"\n--- The pre-filter process is complete, Filtering... ---")
  filter_cars(file_streaming_cars)