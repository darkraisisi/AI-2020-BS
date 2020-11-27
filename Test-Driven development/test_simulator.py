from unittest import TestCase
from Simulator import *


class TestSimulator(TestCase):
    """
    Tests for ``Simulator`` implementation.
    """
    def setUp(self):
        self.sim = Simulator()

    def test_update(self):
        """
        Tests that the update functions returns an object of World type.
        """
        self.assertIsInstance(self.sim.update(), World)

    def test_get_generation(self):
        """
        Tests whether get_generation returns the correct value:
            - Generation should be 0 when Simulator just created;
            - Generation should be 2 after 2 updates.
        """
        self.assertIs(self.sim.generation, self.sim.get_generation())
        self.assertEqual(self.sim.get_generation(), 0)
        self.sim.update()
        self.sim.update()
        self.assertEqual(self.sim.get_generation(), 2)

    def test_get_world(self):
        """
        Tests whether the object passed when get_world() is called is of World type, and has the required dimensions.
        When no argument passed to construction of Simulator, world is square shaped with size 20.
        """
        self.assertIs(self.sim.world, self.sim.get_world())
        self.assertEqual(self.sim.get_world().width, 20)
        self.assertEqual(self.sim.get_world().height, 20)

    def test_set_world(self):
        """
        Tests functionality of set_world function.
        """
        world = World(10)
        self.sim.set_world(world)
        self.assertIsInstance(self.sim.get_world(), World)
        self.assertIs(self.sim.get_world(), world)


    def test_evolve_generation(self):
        """
        Test the base rules of game of life.
        """
        # One cell with no neighbours: should die 'underpopulation'
        world = World(3)
        self.sim.set_world(world)
        self.sim.get_world().set(1,1,1)
        self.sim.update()
        self.assertEqual(self.sim.get_world().get(1, 1), 0)

        # One cell with 1 neighbours: should die
        world = World(3)
        self.sim.set_world(world)
        self.sim.get_world().set(1,1,1)
        self.sim.get_world().set(0,1,1)
        self.sim.update()
        self.assertEqual(self.sim.get_world().get(1, 1), 0)

        # One cell with 2 neighbours: cell should live 'survival'

        world = World(3)
        self.sim.set_world(world)
        self.sim.get_world().set(0,1,1)
        self.sim.get_world().set(1,1,1)
        self.sim.get_world().set(2,1,1)
        self.sim.update()
        self.assertEqual(self.sim.get_world().get(1, 1), 1)
        
        # One cell with 4 neighbours: Cell should die 'overpopulation'

        world = World(3)
        self.sim.set_world(world)
        self.sim.get_world().set(0,0,1)
        self.sim.get_world().set(0,1,1)
        self.sim.get_world().set(1,1,1)
        self.sim.get_world().set(2,1,1)
        self.sim.get_world().set(2,2,1)
        self.sim.update()
        self.assertEqual(self.sim.get_world().get(1, 1), 0)

        # One dead cell with 3 neighbours: cell should live 'birth'

        world = World(3)
        self.sim.set_world(world)
        self.sim.get_world().set(0,1,1)
        self.sim.get_world().set(1,1,0)
        self.sim.get_world().set(2,1,1)
        self.sim.get_world().set(2,2,1)
        self.sim.update()
        self.assertEqual(self.sim.get_world().get(1, 1), 1)

