# 3D Ecosystem Simulation

A 3D ecosystem simulation built with Python, Pygame and OpenGL that models animal and plant interactions in a procedurally generated world.

## Features

- **3D Visualization**: Rendered using OpenGL with lighting effects
- **Dynamic Ecosystem**: 
  - Multiple animal types (Deer, Rabbit, Bear, Bird)
  - Multiple plant types (Grass, Flower, Tree)
  - Basic food chain simulation (hunting/eating behaviors)
- **Procedural World**:
  - Random terrain generation using Perlin noise
  - Day/night cycle
  - Weather system (clear, rain, storm)
- **Entity Behaviors**:
  - Animals have energy levels and different states (idle, eating, hunting, fleeing)
  - Plants grow over time

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ecosystem-simulation.git
cd ecosystem-simulation
```

2. Install dependencies:
```bash
pip install -r ecosystem_game/requirements.txt
```

## Usage

Run the simulation:
```bash
python ecosystem_game/src/main.py
```

Controls:
- `ESC` - Quit the simulation

## Project Structure

```
ecosystem_game/
├── src/
│   ├── main.py         # Main game loop and rendering
│   ├── world.py        # World generation and rendering
│   ├── ecosystem.py    # Ecosystem simulation logic
│   ├── entities.py     # Animal and plant classes
├── assets/             # Asset files (textures, models etc)
├── requirements.txt    # Python dependencies
```

## Dependencies

- Python 3.x
- Pygame 2.6.1
- PyOpenGL 3.1.9
- NumPy 2.2.4
- Pandas 2.2.3

## Screenshots

(Add screenshots of the simulation here)

## Future Improvements

- Add more complex animal behaviors
- Implement proper predator-prey interactions
- Add reproduction mechanics
- Improve graphics with textures and models
- Add user interaction (camera control, speed adjustment)
