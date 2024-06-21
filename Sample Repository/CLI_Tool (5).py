#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# tests/test_converter.py

import unittest
from dna_to_protein.converter import DNAtoProteinConverter

class TestDNAtoProteinConverter(unittest.TestCase):
    """
    Unit tests for the DNAtoProteinConverter class.
    """

    def test_conversion(self):
        """
        Test the conversion of a valid DNA sequence to a protein sequence.
        """
        self.assertEqual(DNAtoProteinConverter.convert("ATGTTTGGG"), "MFG")

    def test_invalid_length(self):
        """
        Test the handling of a DNA sequence whose length is not a multiple of 3.
        """
        with self.assertRaises(ValueError):
            DNAtoProteinConverter.convert("ATGTT")

    def test_invalid_codon(self):
        """
        Test the handling of a DNA sequence with an invalid codon.
        """
        with self.assertRaises(ValueError):
            DNAtoProteinConverter.convert("ATGXYZ")

if __name__ == '__main__':
    unittest.main()

