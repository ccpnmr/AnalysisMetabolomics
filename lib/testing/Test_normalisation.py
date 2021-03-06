#=========================================================================================
# Licence, Reference and Credits
#=========================================================================================
__copyright__ = "Copyright (C) CCPN project (http://www.ccpn.ac.uk) 2014 - 2019"
__credits__ = ("Ed Brooksbank, Luca Mureddu, Timothy J Ragan & Geerten W Vuister")
__licence__ = ("CCPN licence. See http://www.ccpn.ac.uk/v3-software/downloads/license")
__reference__ = ("Skinner, S.P., Fogh, R.H., Boucher, W., Ragan, T.J., Mureddu, L.G., & Vuister, G.W.",
                 "CcpNmr AnalysisAssign: a flexible platform for integrated NMR analysis",
                 "J.Biomol.Nmr (2016), 66, 111-124, http://doi.org/10.1007/s10858-016-0060-y")
#=========================================================================================
# Last code modification
#=========================================================================================
__modifiedBy__ = "$modifiedBy: CCPN $"
__dateModified__ = "$dateModified: 2017-07-07 16:32:23 +0100 (Fri, July 07, 2017) $"
__version__ = "$Revision: 3.0.0 $"
#=========================================================================================
# Created
#=========================================================================================
__author__ = "$Author: TJ Ragan $"
__date__ = "$Date: 2017-04-07 10:28:45 +0000 (Fri, April 07, 2017) $"
#=========================================================================================
# Start of code
#=========================================================================================

import unittest
import numpy as np
import numpy.testing as npt

from ccpn.AnalysisMetabolomics.lib import normalisation
from ccpn.AnalysisMetabolomics.lib import centering
from ccpn.AnalysisMetabolomics.lib import scaling


class TestNormalisation(unittest.TestCase):

    def test_TSA(self):
        rawSpectra = np.array([[0, 1, 0],
                               [0, 2, 0]])

        targetSpectra = np.array([[0, 1, 0],
                                  [0, 1, 0]])

        normalizedSpectra = normalisation.tsa(rawSpectra)
        npt.assert_array_equal(normalizedSpectra, targetSpectra)

    def test_PQN(self):
        rawSpectra = np.ones([2, 3])
        rawSpectra[0, 1] = 2

        normalizedSpectra = normalisation.pqn(rawSpectra)
        self.assertEqual(normalizedSpectra[0, 0], normalizedSpectra[1, 0])
        self.assertNotEqual(normalizedSpectra[0, 1], normalizedSpectra[1, 1])
        self.assertEqual(normalizedSpectra[0, 2], normalizedSpectra[1, 2])


if __name__ == '__main__':
    unittest.main()
