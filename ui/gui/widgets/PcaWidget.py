"""Module Documentation here

"""
#=========================================================================================
# Licence, Reference and Credits
#=========================================================================================
__copyright__ = "Copyright (C) CCPN project (http://www.ccpn.ac.uk) 2014 - 2017"
__credits__ = ("Wayne Boucher, Ed Brooksbank, Rasmus H Fogh, Luca Mureddu, Timothy J Ragan & Geerten W Vuister")
__licence__ = ("CCPN licence. See http://www.ccpn.ac.uk/v3-software/downloads/license",
               "or ccpnmodel.ccpncore.memops.Credits.CcpnLicense for licence text")
__reference__ = ("For publications, please use reference from http://www.ccpn.ac.uk/v3-software/downloads/license",
               "or ccpnmodel.ccpncore.memops.Credits.CcpNmrReference")
#=========================================================================================
# Last code modification
#=========================================================================================
__modifiedBy__ = "$modifiedBy: CCPN $"
__dateModified__ = "$dateModified: 2017-07-07 16:32:24 +0100 (Fri, July 07, 2017) $"
__version__ = "$Revision: 3.0.b3 $"
#=========================================================================================
# Created
#=========================================================================================
__author__ = "$Author: rhfogh $"
__date__ = "$Date: 2017-04-07 10:28:45 +0000 (Fri, April 07, 2017) $"
#=========================================================================================
# Start of code
#=========================================================================================

import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtWidgets

from ccpn.ui.gui.modules.CcpnModule import CcpnModule
from ccpn.ui.gui.widgets.Base import Base
from ccpn.ui.gui.widgets.Button import Button
from ccpn.ui.gui.widgets.CheckBox import CheckBox
from ccpn.ui.gui.widgets.Label import Label
from ccpn.ui.gui.widgets.LineEdit import LineEdit
from ccpn.ui.gui.widgets.ListWidget import ListWidget
from ccpn.ui.gui.widgets.PulldownList import PulldownList


# class PcaModule(CcpnModule, Base):
#
#   def __init__(self, project, **kw):
#
#     super(PcaModule, self)
#     CcpnModule.__init__(self, name='PCA')
#     Base.__init__(self, **kw)
#     self.project = project
#     self.mDict = MetabolomicsPersistenceDict()
#
#     self.decomposeLabel = Label(self, 'Decompose Method ')
#
#     self.layout.addWidget(self.decomposeLabel, 0, 0, 1, 1)
#     self.decomposePulldown = PulldownList(self, grid=(0, 1), gridSpan=(1, 1))
#     self.decomposePulldown.setData(['PCA'])
#     self.sourceLabel = Label(self, 'Source', grid=(0, 2), gridSpan=(1, 1))
#     self.sourcePulldown = PulldownList(self, grid=(0, 3), gridSpan=(1, 1))
#     # self.sourcePulldown.setData([group.pid for group in project.spectrumGroups])
#     self.sourcePulldown.setData(list(self.mDict['Pipelines'].keys()))
#
#     self.goButton = Button(self, 'GO', grid=(0, 5), gridSpan=(1, 1))
#     self.goButton.clicked.connect(self.runPca)
#
#     self.plottingWidget = QtWidgets.QWidget()
#     self.plottingWidgetLayout = QtWidgets.QGridLayout()
#     self.plottingWidget.setLayout(self.plottingWidgetLayout)
#
#     self.layout.addWidget(self.plottingWidget, 1, 0, 4, 6)
#
#     self.scoresPlot = PlotWidget(self, appBase=project._appBase)
#     self.scoresPlot.plotItem.axes['left']['item'].show()
#     self.scoresPlot.plotItem.axes['right']['item'].hide()
#     self.scoresWidget = QtWidgets.QWidget(self)
#     self.scoresWidgetLayout = QtWidgets.QGridLayout()
#     self.scoresWidgetLayout.addWidget(self.scoresPlot, 0, 0, 1, 7)
#     self.scoresXLabel = Label(self, 'x ')
#     self.scoresXBox = PulldownList(self)
#     self.scoresYLabel = Label(self, 'y ')
#     self.scoresYBox = PulldownList(self)
#     self.scoresColourLabel = Label(self, 'Colour')
#     self.scoresColourPulldown = PulldownList(self)
#     self.scoresWidgetLayout.addWidget(self.scoresXLabel, 1, 0, 1, 1)
#     self.scoresWidgetLayout.addWidget(self.scoresXBox, 1, 2, 1, 1)
#     self.scoresWidgetLayout.addWidget(self.scoresYLabel, 1, 3, 1, 1)
#     self.scoresWidgetLayout.addWidget(self.scoresYBox, 1, 4, 1, 1)
#     self.scoresWidgetLayout.addWidget(self.scoresColourLabel, 1, 5, 1, 1)
#     self.scoresWidgetLayout.addWidget(self.scoresColourPulldown, 1, 6, 1, 1)
#     self.scoresWidget.setLayout(self.scoresWidgetLayout)
#     self.plottingWidget.layout().addWidget(self.scoresWidget, 1, 0, 2, 2)
#
#     self.evPlot = PlotWidget(self, appBase=project._appBase)
#     self.evPlot.plotItem.axes['left']['item'].show()
#     self.evPlot.plotItem.axes['right']['item'].hide()
#     self.evPlotWidgetLayout = QtWidgets.QGridLayout()
#     self.evPlotWidget = QtWidgets.QWidget(self)
#     self.evPlotXLabel = Label(self, 'x ')
#     self.evPlotXBox = PulldownList(self)
#     self.evPlotXBox.setData([]) # list of text that can be used to call stuff.
#     self.evPlotYLabel = Label(self, 'y ')
#     self.evPlotYBox = PulldownList(self)
#     self.evPlotColourLabel = Label(self, 'Colour')
#     self.evPlotColourPulldown = PulldownList(self)
#     self.evPlotWidgetLayout.addWidget(self.evPlot, 0, 0, 1, 7)
#     self.evPlotWidgetLayout.addWidget(self.evPlotXLabel, 1, 0, 1, 1)
#     self.evPlotWidgetLayout.addWidget(self.evPlotXBox, 1, 2, 1, 1)
#     self.evPlotWidgetLayout.addWidget(self.evPlotYLabel, 1, 3, 1, 1)
#     self.evPlotWidgetLayout.addWidget(self.evPlotYBox, 1, 4, 1, 1)
#     self.evPlotWidgetLayout.addWidget(self.evPlotColourLabel, 1, 5, 1, 1)
#     self.evPlotWidgetLayout.addWidget(self.evPlotColourPulldown, 1, 6, 1, 1)
#     self.evPlotWidget.setLayout(self.evPlotWidgetLayout)
#     self.plottingWidget.layout().addWidget(self.evPlotWidget, 1, 2, 2, 2)
#
#   def setSpectrumDisplay(self, spectrumDisplay):
#     self.spectrumDisplay = spectrumDisplay
#
#   def runPca(self):
#     params = {'method': self.decomposePulldown.currentText(),
#               'source': self.sourcePulldown.currentText()}
#     preProcessedData = self.mDict['Pipelines'][self.sourcePulldown.currentText()]['output']
#
#     self.pca = PCA(preProcessedData)
#
#     scores = self.pca.scores
#     xValues, yValues = 'PC1', 'PC2'
#     x = scores[xValues].values
#     y = scores[yValues].values
#     self.scoresPlot.plot(x, y, pen=None, symbol='o')
#     self.scoresYLabel = yValues
#
#     ev = self.pca.explainedVariance
#     xValues = list(range(1, 1+len(ev)))
#     self.evPlot.plot(xValues, ev, symbol='o')
#
#     if self.spectrum:
#       spectrumDisplay = self.createSpectrumDisplay(spectrum=None)
#       self.setSpectrumDisplay(spectrumDisplay)
#       if self.project._appBase.ui.mainWindow is not None:
#         mainWindow = self.project._appBase.ui.mainWindow
#       else:
#         mainWindow = self.project._appBase._mainWindow
#       mainWindow.moduleArea.moveModule(spectrumDisplay.module, position='bottom', neighbor=self)

class PcaWidget(CcpnModule):
  def __init__(self, presenter, parent, **kwargs):
    CcpnModule.__init__(self, name='PCA')
    self.presenter = presenter

    self.settings = PcaSettings(self, presenter=self.presenter)
    self.pcaPlotLeft = PcaPlot(self, presenter=self.presenter)
    self.pcaPlotRight = PcaPlot(self, presenter=self.presenter)
    self.pcaOutput = PcaOutput(self, presenter=self.presenter)

    self.layout.addWidget(self.settings, 0, 0, 1, 2)
    self.layout.addWidget(self.pcaPlotLeft, 1, 0, 2, 1)
    self.layout.addWidget(self.pcaPlotRight, 1, 1, 2, 1)
    self.layout.addWidget(self.pcaOutput, 3, 0, 1, 2)


class PcaSettings(QtWidgets.QWidget, Base):
  def __init__(self, parent=None, presenter=None, **kwargs):
    QtWidgets.QWidget.__init__(self, parent)
    Base.__init__(self, **kwargs)
    self.presenter = presenter

    self.setLayout(QtWidgets.QHBoxLayout())
    column1Layout = QtWidgets.QVBoxLayout()
    self.layout().addLayout(column1Layout)

    column1Layout.addWidget(Label(self, 'Method:'))
    self.decompMethodPulldown = PulldownList(self, callback=presenter.setMethod)
    column1Layout.addWidget(self.decompMethodPulldown)
    # self.goButton = Button(self, 'GO!', hPolicy='fixed', callback=presenter.go)
    # column1Layout.addWidget(self.goButton)
    column1Layout.addStretch()

    column2Layout = QtWidgets.QGridLayout()
    self.layout().addLayout(column2Layout)
    column2Layout.addWidget(Label(self, '1. Normalization:'), 0, 0, 1, 1)
    self.normMethodPulldown = PulldownList(self, callback=presenter.setNormalization)
    column2Layout.addWidget(self.normMethodPulldown, 0, 1, 1, 1)

    column2Layout.addWidget(Label(self, '2. Centering:'), 1, 0, 1, 1)
    self.centMethodPulldown = PulldownList(self, callback=presenter.setCentering)
    column2Layout.addWidget(self.centMethodPulldown, 1, 1, 1, 1)

    column2Layout.addWidget(Label(self, '3. Scaling:'), 2, 0, 1, 1)
    self.scalingMethodPulldown = PulldownList(self, callback=presenter.setScaling)
    column2Layout.addWidget(self.scalingMethodPulldown, 2, 1, 1, 1)

    self.layout().addWidget(Label(self, 'Source:'))
    self.sourceList = ListWidget(self, callback=presenter.setSourcesSelection)
    self.sourceList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

    self.layout().addWidget(self.sourceList)

    self.setMaximumHeight(100)



class PcaPlot(QtWidgets.QWidget):
  def __init__(self, parent=None, presenter=None, **kwargs):
    QtWidgets.QWidget.__init__(self, parent)
    self.setLayout(QtWidgets.QVBoxLayout())
    self.presenter = presenter

    self.plottingWidget = pg.PlotWidget(self)
    self.plotItem = self.plottingWidget.getPlotItem()
    self.plotItem.getAxis('left').setWidth(36)
    self.plotItem.getAxis('bottom').setHeight(24)

    self.layout().addWidget(self.plottingWidget)
    selectorLayout = QtWidgets.QHBoxLayout()

    selectorLayout.addWidget(Label(self, 'x:'))
    self.xAxisSelector = PulldownList(self, callback=self.plot)
    selectorLayout.addWidget(self.xAxisSelector)
    selectorLayout.addWidget(Label(self, 'y:'))
    self.yAxisSelector = PulldownList(self, callback=self.plot)
    selectorLayout.addWidget(self.yAxisSelector)
    selectorLayout.addStretch()

    self.layout().addLayout(selectorLayout)


  def plot(self, *args):

    self.presenter.plot(self, self.xAxisSelector.currentData()[0],
                        self.yAxisSelector.currentData()[0])

  def addXOriginLine(self):
    self.plotItem.addItem(pg.InfiniteLine(angle=0, pos=0,
                          pen=pg.functions.mkPen('w', width=1, style=QtCore.Qt.DashLine)))

  def addYOriginLine(self):
    self.plotItem.addItem(pg.InfiniteLine(angle=90, pos=0,
                          pen=pg.functions.mkPen('w', width=1, style=QtCore.Qt.DashLine)))



class PcaOutput(QtWidgets.QWidget, Base):
  def __init__(self, parent=None, presenter=None, **kwargs):
    QtWidgets.QWidget.__init__(self, parent)
    Base.__init__(self, **kwargs)
    self.presenter = presenter

    self.setLayout(QtWidgets.QHBoxLayout())

    self.sgNameEntryBox = LineEdit(self, text='pca_001')
    self.descaleCheck = CheckBox(self, checked=True, text='Descale Components')
    self.saveButton = Button(self, 'save', callback=self.presenter.saveOutput)

    self.layout().addWidget(Label(self, 'Output spectrum group:'))
    self.layout().addWidget(self.sgNameEntryBox)
    self.layout().addWidget(self.descaleCheck)
    self.layout().addStretch()
    self.layout().addWidget(self.saveButton)



    self.setMaximumHeight(45)

