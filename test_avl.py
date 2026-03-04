# DO NOT MODIFY THIS FILE
# Run me via: python3 -m unittest test_avl_tree

import unittest
import time
from avl import AVLTree


class TestBinarySearchTree(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        An AVLTree exists.
        """
        try:
            AVLTree()
        except NameError:
            self.fail("Could not instantiate AVLTree.")

    # def test_initial_attributes_default_empty_tree(self):
    #     """
    #     A new AVL tree has left, right, and key each None, and balance_factor = 0.
    #     """
    #     avl = AVLTree()
    #     self.assertIsNone(avl.left)
    #     self.assertIsNone(avl.right)
    #     self.assertIsNone(avl.key)
    #     self.assertEqual(0, avl.balance_factor)

    # def test_initial_attributes_accepts_key_parameter(self):
    #     """
    #     An AVL tree can accept a key parameter.
    #     """
    #     avl = AVLTree(10)
    #     self.assertEqual(10, avl.key)

    # """
    # Test helper methods
    # """

    # def test_is_leaf_true_no_children(self):
    #     """
    #     A node with no children is a leaf.
    #     """
    #     avl = AVLTree(10)
    #     self.assertTrue(avl._is_leaf())

    # def test_is_leaf_false_right_child_only(self):
    #     """
    #     A node with one right child is not a leaf.
    #     """
    #     avl = AVLTree(10)
    #     avl.insert(AVLTree(20))
    #     self.assertFalse(avl._is_leaf())

    # def test_is_leaf_false_left_child_only(self):
    #     """
    #     A node with one left child is not a leaf.
    #     """
    #     avl = AVLTree(10)
    #     avl.insert(AVLTree(5))
    #     self.assertFalse(avl._is_leaf())

    # def test_is_leaf_false_two_children(self):
    #     """
    #     A node with two children is not a leaf.
    #     """
    #     avl = AVLTree(10)
    #     avl.insert(AVLTree(5))
    #     avl.insert(AVLTree(20))
    #     self.assertFalse(avl._is_leaf())

    # def test_has_left_child_true(self):
    #     """
    #     Node has a left child.
    #     """
    #     avl = AVLTree(10)
    #     avl.insert(AVLTree(5))
    #     self.assertTrue(avl._has_left_child())

    # def test_has_left_child_false(self):
    #     """
    #     Node does not have a left child.
    #     """
    #     avl = AVLTree(10)
    #     self.assertFalse(avl._has_left_child())

    # def test_has_right_child_true(self):
    #     """
    #     Node has a right child.
    #     """
    #     avl = AVLTree(10)
    #     avl.insert(AVLTree(20))
    #     self.assertTrue(avl._has_right_child())

    # def test_has_right_child_false(self):
    #     """
    #     Node does not have a right child.
    #     """
    #     avl = AVLTree(10)
    #     self.assertFalse(avl._has_right_child())

    # def test_has_left_child_only_true(self):
    #     """
    #     Node has only a left child.
    #     """
    #     avl = AVLTree(10)
    #     avl.insert(AVLTree(5))
    #     self.assertTrue(avl._has_left_child_only())

    # def test_has_left_child_only_false_two_children(self):
    #     """
    #     Node with two children does not have only a left child.
    #     """
    #     avl = AVLTree(10)
    #     avl.insert(AVLTree(5))
    #     avl.insert(AVLTree(20))
    #     self.assertFalse(avl._has_left_child_only())

    # def test_has_right_child_only_true(self):
    #     """
    #     Node has only a right child.
    #     """
    #     avl = AVLTree(10)
    #     avl.insert(AVLTree(20))
    #     self.assertTrue(avl._has_right_child_only())

    # def test_has_right_child_only_false_two_children(self):
    #     """
    #     Node with two children does not have only a right child.
    #     """
    #     avl = AVLTree(10)
    #     avl.insert(AVLTree(5))
    #     avl.insert(AVLTree(20))
    #     self.assertFalse(avl._has_right_child_only())

    # def test_height_single_node(self):
    #     """
    #     Height of a single node is 0.
    #     """
    #     avl = AVLTree(10)
    #     self.assertEqual(0, avl._height())

    # def test_height_two_levels_right_child_only(self):
    #     """
    #     Height is 1 when there is one right child.
    #     """
    #     avl = AVLTree(10)
    #     avl.insert(AVLTree(20))
    #     self.assertEqual(1, avl._height())

    # def test_height_two_levels_left_child_only(self):
    #     """
    #     Height is 1 when there is one left child.
    #     """
    #     avl = AVLTree(10)
    #     avl.insert(AVLTree(5))
    #     self.assertEqual(1, avl._height())

    # def test_height_two_levels_two_children(self):
    #     """
    #     Height is 1 when there are two children at depth 1.
    #     """
    #     avl = AVLTree(10)
    #     avl.insert(AVLTree(5))
    #     avl.insert(AVLTree(20))
    #     self.assertEqual(1, avl._height())

    # def test_height_multilevel_right_chain(self):
    #     """
    #     Height is 2 in a tree with an extra right level.
    #     """
    #     avl = AVLTree(10)
    #     avl.insert(AVLTree(5))
    #     avl.insert(AVLTree(20))
    #     avl.insert(AVLTree(30))
    #     self.assertEqual(2, avl._height())

    # """
    # Find the minimum node in the tree
    # """

    # def test_minimum_single_node(self):
    #     """
    #     Minimum of a single node is itself.
    #     """
    #     avl = AVLTree(10)
    #     self.assertEqual(avl, avl._minimum())

    # def test_minimum_with_left_children(self):
    #     """
    #     Minimum is the leftmost node.
    #     """
    #     avl = AVLTree(10)
    #     avl = avl.insert(AVLTree(5))
    #     smallest_node = AVLTree(1)
    #     avl = avl.insert(smallest_node)
    #     self.assertEqual(smallest_node, avl._minimum())

    # """
    # Calculating the balance factor of each node
    # """

    # def test_calculate_balance_factor_depth1_right(self):
    #     """
    #     BF is left_height - right_height (depth 1 right-heavy case).
    #     """
    #     avl = AVLTree(10)
    #     avl.insert(AVLTree(20))
    #     self.assertEqual(-1, avl._calculate_balance_factor())
    #     self.assertEqual(0, avl.right._calculate_balance_factor())

    # def test_calculate_balance_factor_depth1_left(self):
    #     """
    #     BF is left_height - right_height (depth 1 left-heavy case).
    #     """
    #     avl = AVLTree(10)
    #     avl.insert(AVLTree(5))
    #     self.assertEqual(1, avl._calculate_balance_factor())
    #     self.assertEqual(0, avl.left._calculate_balance_factor())

    # def test_calculate_balance_factor_depth2_right_heavy(self):
    #     """
    #     BF values computed for a depth-2 right-heavy structure.
    #     """
    #     avl = AVLTree(10)
    #     avl.insert(AVLTree(5))
    #     avl.insert(AVLTree(20))
    #     avl.insert(AVLTree(30))
    #     self.assertEqual(-1, avl._calculate_balance_factor())
    #     self.assertEqual(0, avl.left._calculate_balance_factor())
    #     self.assertEqual(-1, avl.right._calculate_balance_factor())
    #     self.assertEqual(0, avl.right.right._calculate_balance_factor())

    # def test_calculate_balance_factor_depth2_left_heavy(self):
    #     """
    #     BF values computed for a depth-2 left-heavy structure.
    #     """
    #     avl = AVLTree(10)
    #     avl.insert(AVLTree(5))
    #     avl.insert(AVLTree(20))
    #     avl.insert(AVLTree(1))
    #     self.assertEqual(1, avl._calculate_balance_factor())
    #     self.assertEqual(1, avl.left._calculate_balance_factor())
    #     self.assertEqual(0, avl.left.left._calculate_balance_factor())
    #     self.assertEqual(0, avl.right._calculate_balance_factor())

    # """
    # Balance factor updates on insertion
    # """

    # def test_balance_factor_on_insertion_right(self):
    #     """
    #     Inserting a right child updates balance_factors.
    #     """
    #     avl = AVLTree(10)
    #     avl.insert(AVLTree(20))
    #     self.assertEqual(-1, avl.balance_factor)
    #     self.assertEqual(0, avl.right.balance_factor)

    # def test_balance_factor_on_insertion_left(self):
    #     """
    #     Inserting a left child updates balance_factors.
    #     """
    #     avl = AVLTree(10)
    #     avl.insert(AVLTree(5))
    #     self.assertEqual(1, avl.balance_factor)
    #     self.assertEqual(0, avl.left.balance_factor)

    # def test_balance_factor_on_insertion_depth2_right(self):
    #     """
    #     Inserting to depth 2 on right updates balance_factors.
    #     """
    #     avl = AVLTree(10)
    #     avl.insert(AVLTree(5))
    #     avl.insert(AVLTree(20))
    #     avl.insert(AVLTree(30))
    #     self.assertEqual(-1, avl.balance_factor)
    #     self.assertEqual(0, avl.left.balance_factor)
    #     self.assertEqual(-1, avl.right.balance_factor)
    #     self.assertEqual(0, avl.right.right.balance_factor)

    # def test_balance_factor_on_insertion_depth2_left(self):
    #     """
    #     Inserting to depth 2 on left updates balance_factors.
    #     """
    #     avl = AVLTree(10)
    #     avl.insert(AVLTree(5))
    #     avl.insert(AVLTree(20))
    #     avl.insert(AVLTree(1))
    #     self.assertEqual(1, avl.balance_factor)
    #     self.assertEqual(1, avl.left.balance_factor)
    #     self.assertEqual(0, avl.left.left.balance_factor)
    #     self.assertEqual(0, avl.right.balance_factor)

    # """
    # Rotations
    # """

    # def test_rotation_left_RR_imbalance(self):
    #     """
    #     Inserting 30 into 10->20 causes RR imbalance; left rotate around 10.
    #     """
    #     avl = AVLTree(10)
    #     avl = avl.insert(AVLTree(20))
    #     avl = avl.insert(AVLTree(30))
    #     self.assertEqual(20, avl.key)
    #     self.assertEqual(10, avl.left.key)
    #     self.assertEqual(30, avl.right.key)

    # def test_rotation_left_recalculates_balance_factors(self):
    #     """
    #     After RR left rotation example, all nodes have BF 0.
    #     """
    #     avl = AVLTree(10)
    #     avl = avl.insert(AVLTree(20))
    #     avl = avl.insert(AVLTree(30))
    #     self.assertEqual(0, avl.balance_factor)
    #     self.assertEqual(0, avl.left.balance_factor)
    #     self.assertEqual(0, avl.right.balance_factor)

    # def test_rotation_right_LL_imbalance(self):
    #     """
    #     Inserting 1 into 10<-5 causes LL imbalance; right rotate around 10.
    #     """
    #     avl = AVLTree(10)
    #     avl = avl.insert(AVLTree(5))
    #     avl = avl.insert(AVLTree(1))
    #     self.assertEqual(5, avl.key)
    #     self.assertEqual(1, avl.left.key)
    #     self.assertEqual(10, avl.right.key)

    # def test_rotation_right_recalculates_balance_factors(self):
    #     """
    #     After LL right rotation example, all nodes have BF 0.
    #     """
    #     avl = AVLTree(10)
    #     avl = avl.insert(AVLTree(5))
    #     avl = avl.insert(AVLTree(1))
    #     self.assertEqual(0, avl.balance_factor)
    #     self.assertEqual(0, avl.left.balance_factor)
    #     self.assertEqual(0, avl.right.balance_factor)

    # def test_rotation_right_left_RL_imbalance(self):
    #     """
    #     Insert 15 into 10->20 with 20's left child causes RL imbalance.
    #     """
    #     avl = AVLTree(10)
    #     avl = avl.insert(AVLTree(20))
    #     avl = avl.insert(AVLTree(15))
    #     self.assertEqual(15, avl.key)
    #     self.assertEqual(10, avl.left.key)
    #     self.assertEqual(20, avl.right.key)

    # def test_rotation_right_left_recalculates_balance_factors(self):
    #     """
    #     After RL rotation example, all nodes have BF 0.
    #     """
    #     avl = AVLTree(10)
    #     avl = avl.insert(AVLTree(20))
    #     avl = avl.insert(AVLTree(15))
    #     self.assertEqual(0, avl.balance_factor)
    #     self.assertEqual(0, avl.left.balance_factor)
    #     self.assertEqual(0, avl.right.balance_factor)

    # def test_rotation_left_right_LR_imbalance(self):
    #     """
    #     Insert 7 into 10<-5 with 5's right child causes LR imbalance.
    #     """
    #     avl = AVLTree(10)
    #     avl = avl.insert(AVLTree(5))
    #     avl = avl.insert(AVLTree(7))
    #     self.assertEqual(7, avl.key)
    #     self.assertEqual(5, avl.left.key)
    #     self.assertEqual(10, avl.right.key)

    # def test_rotation_left_right_recalculates_balance_factors(self):
    #     """
    #     After LR rotation example, all nodes have BF 0.
    #     """
    #     avl = AVLTree(10)
    #     avl = avl.insert(AVLTree(5))
    #     avl = avl.insert(AVLTree(7))
    #     self.assertEqual(0, avl.balance_factor)
    #     self.assertEqual(0, avl.left.balance_factor)
    #     self.assertEqual(0, avl.right.balance_factor)

    # def test_larger_tree_LL_imbalance_structure(self):
    #     """
    #     Larger example: inserting 1 causes LL imbalance; rotation around 5.
    #     """
    #     avl = AVLTree(10)
    #     avl = avl.insert(AVLTree(5))
    #     avl = avl.insert(AVLTree(20))
    #     avl = avl.insert(AVLTree(3))
    #     avl = avl.insert(AVLTree(1))
    #     self.assertEqual(10, avl.key)
    #     self.assertEqual(20, avl.right.key)
    #     self.assertEqual(3, avl.left.key)
    #     self.assertEqual(1, avl.left.left.key)
    #     self.assertEqual(5, avl.left.right.key)

    # def test_larger_tree_LL_imbalance_balance_factors(self):
    #     """
    #     Larger example: validate balance factors after LL rebalance.
    #     """
    #     avl = AVLTree(10)
    #     avl = avl.insert(AVLTree(5))
    #     avl = avl.insert(AVLTree(20))
    #     avl = avl.insert(AVLTree(3))
    #     avl = avl.insert(AVLTree(1))
    #     self.assertEqual(1, avl.balance_factor)
    #     self.assertEqual(0, avl.right.balance_factor)
    #     self.assertEqual(0, avl.left.balance_factor)
    #     self.assertEqual(0, avl.left.left.balance_factor)
    #     self.assertEqual(0, avl.left.right.balance_factor)

    # """
    # Search
    # """

    # def test_search_root(self):
    #     """
    #     Search for the root node.
    #     """
    #     avl = AVLTree(10)
    #     result = avl.search(10)
    #     self.assertIsNotNone(result)
    #     self.assertEqual(10, result.key)

    # def test_search_left_child(self):
    #     """
    #     Search for a node in the left subtree.
    #     """
    #     avl = AVLTree(10)
    #     avl = avl.insert(AVLTree(5))
    #     avl = avl.insert(AVLTree(20))
    #     result = avl.search(5)
    #     self.assertIsNotNone(result)
    #     self.assertEqual(5, result.key)

    # def test_search_right_child(self):
    #     """
    #     Search for a node in the right subtree.
    #     """
    #     avl = AVLTree(10)
    #     avl = avl.insert(AVLTree(5))
    #     avl = avl.insert(AVLTree(20))
    #     result = avl.search(20)
    #     self.assertIsNotNone(result)
    #     self.assertEqual(20, result.key)

    # def test_search_deep_left(self):
    #     """
    #     Search for a node deep in the left subtree.
    #     """
    #     avl = AVLTree(10)
    #     avl = avl.insert(AVLTree(5))
    #     avl = avl.insert(AVLTree(20))
    #     avl = avl.insert(AVLTree(1))
    #     avl = avl.insert(AVLTree(3))
    #     avl = avl.insert(AVLTree(0))
    #     result = avl.search(0)
    #     self.assertIsNotNone(result)
    #     self.assertEqual(0, result.key)

    # def test_search_deep_right(self):
    #     """
    #     Search for a node deep in the right subtree.
    #     """
    #     avl = AVLTree(10)
    #     avl = avl.insert(AVLTree(5))
    #     avl = avl.insert(AVLTree(20))
    #     avl = avl.insert(AVLTree(30))
    #     avl = avl.insert(AVLTree(40))
    #     avl = avl.insert(AVLTree(50))
    #     result = avl.search(50)
    #     self.assertIsNotNone(result)
    #     self.assertEqual(50, result.key)

    # def test_search_nonexistent(self):
    #     """
    #     Search for a key that doesn't exist.
    #     """
    #     avl = AVLTree(10)
    #     avl = avl.insert(AVLTree(5))
    #     avl = avl.insert(AVLTree(20))
    #     result = avl.search(999)
    #     self.assertIsNone(result)

    # def test_search_not_found_in_single_node_tree(self):
    #     """
    #     Search in a tree with only root (no children) for a missing key.
    #     """
    #     avl = AVLTree(10)
    #     result = avl.search(5)
    #     self.assertIsNone(result)

    # def test_search_after_rotations(self):
    #     """
    #     Search for nodes after tree has been rebalanced via rotations.
    #     """
    #     avl = AVLTree(10)
    #     avl = avl.insert(AVLTree(5))
    #     avl = avl.insert(AVLTree(7))  # Causes LR rotation
    #     self.assertEqual(7, avl.search(7).key)
    #     self.assertEqual(5, avl.search(5).key)
    #     self.assertEqual(10, avl.search(10).key)

    # """
    # Delete
    # Note: A delete method is provided in avl.py for you to uncomment and modify.
    # """

    # def test_delete_after_RR_insertion_inbalance(self):
    #     """
    #     Delete a node after an insertion imbalance.
    #     """
    #     avl = AVLTree(10)
    #     avl = avl.insert(AVLTree(20))
    #     avl = avl.insert(AVLTree(30))
    #     avl = avl.delete(30)
    #     self.assertIsNone(avl.search(30))
    #     self.assertEqual(20, avl.key)
    #     self.assertEqual(10, avl.left.key)

    # def test_delete_causes_RR_imbalance(self):
    #     """
    #     Delete causes RR imbalance requiring left rotation.
    #     """
    #     avl = AVLTree(10)
    #     avl = avl.insert(AVLTree(5))
    #     avl = avl.insert(AVLTree(20))
    #     avl = avl.insert(AVLTree(30))

    #     avl = avl.delete(5)

    #     self.assertEqual(20, avl.key)
    #     self.assertEqual(10, avl.left.key)
    #     self.assertEqual(30, avl.right.key)
    #     self.assertIsNone(avl.search(5))
    #     self.assertTrue(abs(avl.balance_factor) <= 1)
    #     self.assertTrue(abs(avl.left.balance_factor) <= 1)
    #     self.assertTrue(abs(avl.right.balance_factor) <= 1)

    # def test_delete_causes_LL_imbalance(self):
    #     """
    #     Delete causes LL imbalance requiring right rotation.
    #     """
    #     avl = AVLTree(30)
    #     avl = avl.insert(AVLTree(10))
    #     avl = avl.insert(AVLTree(40))
    #     avl = avl.insert(AVLTree(5))

    #     avl = avl.delete(40)

    #     self.assertEqual(10, avl.key)
    #     self.assertEqual(5, avl.left.key)
    #     self.assertEqual(30, avl.right.key)
    #     self.assertIsNone(avl.search(40))
    #     self.assertTrue(abs(avl.balance_factor) <= 1)
    #     self.assertTrue(abs(avl.left.balance_factor) <= 1)
    #     self.assertTrue(abs(avl.right.balance_factor) <= 1)

    # def test_delete_causes_RL_imbalance(self):
    #     """
    #     Delete causes RL imbalance requiring right then left rotation.
    #     """
    #     avl = AVLTree(10)
    #     avl = avl.insert(AVLTree(5))
    #     avl = avl.insert(AVLTree(30))
    #     avl = avl.insert(AVLTree(20))

    #     avl = avl.delete(5)

    #     self.assertEqual(20, avl.key)
    #     self.assertEqual(10, avl.left.key)
    #     self.assertEqual(30, avl.right.key)
    #     self.assertIsNone(avl.search(5))
    #     self.assertTrue(abs(avl.balance_factor) <= 1)
    #     self.assertTrue(abs(avl.left.balance_factor) <= 1)
    #     self.assertTrue(abs(avl.right.balance_factor) <= 1)

    # def test_delete_causes_LR_imbalance(self):
    #     """
    #     Delete causes LR imbalance requiring left then right rotation.
    #     """
    #     avl = AVLTree(30)
    #     avl = avl.insert(AVLTree(10))
    #     avl = avl.insert(AVLTree(40))
    #     avl = avl.insert(AVLTree(20))

    #     avl = avl.delete(40)

    #     self.assertEqual(20, avl.key)
    #     self.assertEqual(10, avl.left.key)
    #     self.assertEqual(30, avl.right.key)
    #     self.assertIsNone(avl.search(40))
    #     self.assertTrue(abs(avl.balance_factor) <= 1)
    #     self.assertTrue(abs(avl.left.balance_factor) <= 1)
    #     self.assertTrue(abs(avl.right.balance_factor) <= 1)


if __name__ == "__main__":
    unittest.main()
