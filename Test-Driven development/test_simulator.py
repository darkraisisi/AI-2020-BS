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
        # One cell with no neighbours & life force 1: should die 'underpopulation'
        world = World(3)
        self.sim.set_world(world)
        self.sim.get_world().set(1,1,1)
        self.sim.update()
        self.assertEqual(self.sim.get_world().get(1, 1), 0)

        # One cell with no neighbours & life force 1: should weaken
        world = World(3)
        self.sim.set_world(world)
        self.sim.get_world().set(1,1,2)
        self.sim.update()
        self.assertEqual(self.sim.get_world().get(1, 1), 1)

        # One cell with 1 neighbour: should die
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
        self.sim.get_world().set(1,1,3)
        self.sim.get_world().set(2,1,1)
        self.sim.update()
        self.assertEqual(self.sim.get_world().get(1, 1), 3)
        
        # One cell with 4 neighbours & life force 5: Cell should weaken 'overpopulation'

        world = World(3)
        self.sim.set_world(world)
        self.sim.get_world().set(0,0,1)
        self.sim.get_world().set(0,1,1)
        self.sim.get_world().set(1,1,5)
        self.sim.get_world().set(2,1,1)
        self.sim.get_world().set(2,2,1)
        self.sim.update()
        self.assertEqual(self.sim.get_world().get(1, 1), 4)

        # One dead cell with 3 weak neighbours: cell should not get revived 'birth'

        world = World(3)
        self.sim.set_world(world)
        self.sim.get_world().set(0,1,1)
        self.sim.get_world().set(1,1,0)
        self.sim.get_world().set(2,1,1)
        self.sim.get_world().set(2,2,1)
        self.sim.update()
        self.assertEqual(self.sim.get_world().get(1, 1), 0)

        # One dead cell with 3 vertile neighbours: cell should not get born 'birth'

        world = World(3)
        self.sim.set_world(world)
        self.sim.get_world().set(0,1,4)
        self.sim.get_world().set(1,1,0)
        self.sim.get_world().set(2,1,4)
        self.sim.get_world().set(2,2,4)
        self.sim.update()
        self.assertEqual(self.sim.get_world().get(1, 1), 6)

    def test_generate_rules(self):
        """
        Test if the optional paramater for a new rule set gets parsed propperly
        """

        b,s = self.sim.generate_rules('B3/S23')
        self.assertEqual([b,s], [[3],[2,3]])
        
        b,s = self.sim.generate_rules('B23/S2')
        self.assertEqual([b,s], [[2,3],[2]])

        b,s = self.sim.generate_rules('B3/S234567')
        self.assertEqual([b,s], [[3],[2,3,4,5,6,7]])

    
    def test_check_vertility(self):
        """
        Check if a cell is still vertile
        """
        
        self.assertEqual(self.sim.check_vertility(0),False)
        self.assertEqual(self.sim.check_vertility(3),True)
        self.assertEqual(self.sim.check_vertility(4),True)
        self.assertEqual(self.sim.check_vertility(100),False)

