"""
Triple threat simulation game for AP Computer Science Principles.
Monarch High School - Boulder Valley School District
Yoav Cohen - November 2024
"""

import random

def main() -> None:
    # set variables for cost to play and base prize
    cost: int = 1
    base_prize: int = 10
    mega_number: int = 6
    mega_multiplier: int = 10
    # roll three dice
    roll1: int = random.randint(1, 6)
    roll2: int = random.randint(1, 6)
    roll3: int = random.randint(1, 6)
    # check if they are equal   
    prize: int = 0
    if roll1 == roll2 and roll1 == roll3:
        if roll1 == mega_number:
            prize = base_prize * mega_multiplier
        else:
            prize = base_prize * roll1
      
    # output results
    print(f"Casino collects: ${cost}")
    print(f"Player rolls: {roll1}-{roll2}-{roll3}")
    print(f"Casino pays out: ${prize}")
    print(f"Profit: ${cost -prize}")
if __name__ == "__main__":
    main()