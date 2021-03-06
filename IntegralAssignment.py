"""Module Documentation here

"""
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
__dateModified__ = "$dateModified: 2017-07-07 16:32:22 +0100 (Fri, July 07, 2017) $"
__version__ = "$Revision: 3.0.0 $"
#=========================================================================================
# Created
#=========================================================================================
__author__ = "$Author: rhfogh $"
__date__ = "$Date: 2017-04-07 10:28:45 +0000 (Fri, April 07, 2017) $"
#=========================================================================================
# Start of code
#=========================================================================================

from PyQt5 import QtGui, QtWidgets

from ccpn.ui.gui.widgets.Base import Base
from ccpn.ui.gui.widgets.Button import Button
from ccpn.ui.gui.widgets.Label import Label
from ccpn.ui.gui.widgets.PulldownList import PulldownList
from ccpn.ui.gui.widgets.Table import ObjectTable, Column


class IntegralAssignment(QtWidgets.QWidget):

  def __init__(self, parent=None):
    QtWidgets.QWidget.__init__(self, parent)


    self.integratedAreasLabel = Label(self, 'IntegratedAreas', grid=(0, 0), gridSpan=(1, 3))
    self.assignLabel = Label(self, 'Assign', grid=(1, 4))
    self.assignButton = Button(self, '<--', grid=(2, 4), callback=self.assignIntegral)
    self.assignAndMoveButton = Button(self, '<-- + A', grid=(3, 4), callback=self.assignAndMove)
    self.deassignLabel = Label(self, 'Deassign', grid=(1, 5))
    self.deassignButton = Button(self, 'X', grid=(2, 5), callback=self.deassignIntegral)
    self.deassignAndMoveButton = Button(self, '<-- + X', grid=(3, 5), callback=self.deassignAndMove)
    self.suggestionSourceLabel = Label(self, 'Suggestion Source ', grid=(0, 6), gridSpan=(1, 1))
    self.suggestionSourcePulldown = PulldownList(self, grid=(0, 7), gridSpan=(1, 2), callback=self.fillSubstanceTable)
    self.suggestionSourcePulldown.setData()
    self.integralTable = IntegralTable(self,  grid=(1, 0), gridSpan=(4, 3))
    self.substanceTable = SubstanceTable(self, grid=(1, 6), gridSpan=(4, 3))


  def fillSubstanceTable(self, value):
    source = value
    substances = [['1', '2', '3']]
    substanceList = [Substance[subs] for subs in substances]
    self.substanceTable.setObjects(substanceList)

  def assignIntegral(self):
    integralObject = self.integralTable.integralTable.getCurrentObject()
    substanceObject = self.substanceTable.substanceTable.getCurrentObject()
    integralObject.id = substanceObject.substance

  def deassignIntegral(self):
    integralObject = self.integralTable.integralTable.getCurrentObject()
    integralObject.id = ''

  def assignAndMove(self):
    self.assignIntegral()
    if self.integralTable.integralTable.getCurrentRow() == 0:
      currentRow = 1
    else:
      currentRow = self.integralTable.integralTable.getCurrentRow()
    print('currentRow', currentRow)
    self.integralTable.integralTable.selectRow(currentRow)

  def deassignAndMove(self):
    self.deassignIntegral()
    if self.integralTable.integralTable.getCurrentRow() == 0:
      currentRow = 1
    else:
      currentRow = self.integralTable.integralTable.getCurrentRow()
    print('currentRow', currentRow)
    self.integralTable.integralTable.selectRow(currentRow)




class IntegralTable(QtWidgets.QWidget):

  def __init__(self, parent=None, project=None, **kwds):
    QtWidgets.QWidget.__init__(self, parent)

    integralTableColumns = [Column('ID', 'id'), Column('range', 'range'), Column('slope', 'slope'), Column('bias','bias'),
                 Column('area', 'area')]

    integralList = [Integral('1', '2', '3', '4', '5'), Integral('qr', '2', '3', '4', '5'), Integral('8', '2', '3', '4', '5'),
                    Integral('a', '2', '3', '4', '5'), Integral('b', '2', '3', '4', '5'), Integral('d', '2', '3', '4', '5')]
    self.integralLists = [integralList]
    self.integralTable = ObjectTable(self, callback=self.integralCallback, columns=integralTableColumns, objects=integralList, grid=(1, 0), gridSpan=(2, 2))

  def integralCallback(self):
    pass


class SubstanceTable(QtWidgets.QWidget, Base):
  def __init__(self, parent=None, **kwds):

    super().__init__(parent)
    Base._init(self, **kwds)

    substanceTableColumns = [Column('substance', 'name', setEditValue=lambda substance, value: self.setSubstanceName(substance, value)),
                             Column('atom', 'atom'), Column('cs', 'cs')]

    tipTexts2 = ['substance Id', 'substance atom', 'substance cs']
    substanceList = [Substance('load', '2', '3'), Substance('1', '2', '3'), Substance('1', '2', '3')]
    self.substanceLists = [substanceList]

    self.substanceTable = ObjectTable(self, columns=substanceTableColumns,
                              callback=self.substanceCallback,
                              objects=substanceList)

  def setSubstancename(self, substance, value):
    substance.name = value

  def substanceCallback(self):
    pass


class Integral(object):

  def __init__(self, integralId, range, slope, bias, area):
    self.id = integralId
    self.range = range
    self.slope = slope
    self.bias = bias
    self.area = area

class Substance(object):
  def __init__(self, name, atom, cs):
    self.name = name
    self.atom = atom
    self.cs = cs
