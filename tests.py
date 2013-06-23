import unittest
import main 

class MainTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #-- Setup --
        pass

    def setUp(self):
        #-- Load fixtures --
        pass

    def tearDown(self):
        #-- Cleanup --
        pass 

    def test_creation_frames_per_game(self):
        #-- Test creation of frames per game --
        new_game = main.game(5)
        assert len(new_game)==5

    def test_count_pins(self):
        #-- Test counter --
        throws = [4,7,8]
        assert main.count_pins(throws) == 19

    def test_false_spare(self):
        #-- Test false spare --
        throw = [1,5]
        total_pins = 10
        assert not main.check_spare(throw, total_pins)

    def test_true_spare(self):
        #-- Test true spare --
        throws = [5,5]
        total_pins = 10
        assert main.check_spare(throws, total_pins)

    def test_true_strike(self):
        #-- Test true strike --
        throws = [10,0]
        total_pins = 10
        assert main.check_strike(throws, total_pins)

    def test_simple_update_score(self):
        previous_throws = [3,2]
        throws = [6,3]
        total_pins = 10
        assert main.update_score(previous_throws, throws, total_pins) == 9

    def test_additional_points_with_strike(self):
        previous_throws = [10,0]
        throws = [5,3]
        total_pins = 10
        assert main.get_additional_points(previous_throws, throws, total_pins) == 8

    def test_additional_points_with_spare(self):
        previous_throws = [4,6]
        throws = [1,3]
        total_pins = 10
        assert main.get_additional_points(previous_throws, throws, total_pins) == 1

    def test_strike_update_score(self):
        previous_throws = [10,0]
        throws = [6,3]
        total_pins = 10
        assert main.update_score(previous_throws, throws, total_pins) == 18

    def test_spare_update_score(self):
        previous_throws = [3,7]
        throws = [6,3]
        total_pins = 10
        assert main.update_score(previous_throws, throws, total_pins) == 15

    def test_perfect_throw(self):
        previous_throws = [10,0]
        throws = [10,0]
        total_pins = 10
        assert main.update_score(previous_throws, throws, total_pins) == 30

    def test_final_example01(self):
        game = [[1,4],[4,5],[6,4],[5,5],[10,0],[0,1],[7,3],[6,4],[10,0],[2,8]]
        total_pins = 10
        extra = 6

        score = 0
        for i in range(len(game)):
            previous_throws = game[i-1] if i > 0 else []
            new_points = main.update_score(previous_throws, game[i], total_pins)
            score += new_points

        assert score + extra == 133

    def test_final_example02(self):
        game = [[8,2],[8,0],[8,1],[7,3],[2,4],[9,0],[5,3],[7,3],[9,0],[6,3]]
        total_pins = 10
        extra = 0

        score = 0
        for i in range(len(game)):
            previous_throws = game[i-1] if i > 0 else []
            new_points = main.update_score(previous_throws, game[i], total_pins)
            score += new_points

        assert score + extra == 107

    def test_final_example03(self):
        game = [[0,10],[10,0],[9,1],[8,0],[10,0],[1,8],[6,0],[7,3],[7,1],[1,5]]
        total_pins = 10
        extra = 0

        score = 0
        for i in range(len(game)):
            previous_throws = game[i-1] if i > 0 else []
            new_points = main.update_score(previous_throws, game[i], total_pins)
            score += new_points

        assert score + extra == 131

    def test_final_example_solid(self):
        game = [[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0]]
        total_pins = 10
        extra = 20

        score = 0
        for i in range(len(game)):
            previous_throws = game[i-1] if i > 0 else []
            new_points = main.update_score(previous_throws, game[i], total_pins)
            print new_points
            score += new_points
            print "Score>> %s" % score

        assert score + extra == 300

        
    #--Advanced tests --
    def ttest_standard_game(self):
        #-- When we create and standard game should be 10 frames --
        new_game = main.game()
        assert len(new_game)==10

    def ttest_5_balls_per_frame(self):
        new_game = main.game(3,5)
        for frame in range(len(new_game)):
            assert len(new_game[frame]) >= 5

    #-- This test doesn't apply because now size is dynamic, so after an strike/spare we don't play anymore  --
    def ttest_balls_per_frame(self):
        #-- Test every frame has 2 played balls --
        new_game = main.game(3,2)
        for frame in range(len(new_game)):
            assert len(new_game[frame]) >= 2


