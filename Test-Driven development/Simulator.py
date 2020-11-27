from World import *
import copy
import sys

class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world = None):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        print(sys.argv)
        if len(sys.argv) == 2:
            b, s = self.generate_rules(sys.argv[1])
            self.rule_b = b
            self.rule_s = s
        else:
            self.rule_b = [3]
            self.rule_s = [2, 3]

        self.generation = 0
        self.vertility = {'min':0, 'max':6}

        if world == None:
            self.world = World(20)
        else:
            self.world = world

    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """
        self.generation += 1

        self.evolve_generation()

        return self.world

    def get_generation(self):
        """
        Returns the value of the current generation of the simulated Game of Life.

        :return: generation of simulated Game of Life.
        """
        return self.generation

    def get_world(self):
        """
        Returns the current version of the ``World``.

        :return: current state of the world.
        """
        return self.world

    def set_world(self, world: World) -> None:
        """
        Changes the current world to the given value.

        :param world: new version of the world.

        """
        self.world = world


    def evolve_generation(self) -> None:
        """
        Check the current cell against the rules to determine the next state.

        Uses an instace of World.
        """
        # We need to make a deep copy so we can evaluate the current state of the game before writing a new status to it.
        new_world = copy.deepcopy(self.world)

        for x in range(self.world.width):
            for y in range(self.world.height):
                cell = self.world.get(x,y) # Current cell
                neighbours = self.world.get_neighbours(x,y) # All neighbours of current cell
                n = neighbours.count(1) # amount of neighbours
                if cell == 1:
                    if n not in self.rule_s:
                        # Cell dies under/over-population
                        new_world.set(x,y,0)
                else:
                    # Cell is dead
                    if n in self.rule_b:
                        # Cell is born
                        new_world.set(x,y,1)

        self.set_world(new_world)


    def check_vertility(self,cell:int) -> bool:
        print(self.vertility)
        if (cell > self.vertility['min'] + 2 
        and cell < self.vertility['max'] - 2):
            return True
        return False

    
    def generate_rules(self, rule_str) -> [str, str]:
        """
        Parse a string to fit as rules for the sumulation.

        :param rule_str: Rule string to be parsed
        :return: B, S strings: Births and Survival
        """
        rule_str = rule_str.lower().split('b')
        rule_str = rule_str[1].split('/s')
        b = rule_str[0]
        s = rule_str[1]
        return  [int(x) for x in b],  [int(y) for y in s]
        
        
