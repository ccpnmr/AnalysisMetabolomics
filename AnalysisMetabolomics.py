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
__author__ = "$Author: TJ $"
__date__ = "$Date: 2017-04-07 10:28:45 +0000 (Fri, April 07, 2017) $"
#=========================================================================================
# Start of code
#=========================================================================================

from ccpn.AnalysisAssign.AnalysisAssign import Assign


class Metabolomics(Assign):
    """Root class for Metabolomics application"""

    def __init__(self, applicationName, applicationVersion, commandLineArguments):
        Assign.__init__(self, applicationName, applicationVersion, commandLineArguments)

    def setupMenus(self):
        super().setupMenus()
        menuSpec = ('Metabolomics', [("Decomposition (PCA)", self.showDecompositionModule), [('shortcut', 'de')],
                                     (),
                                     ("Pipeline", self.showMetabolomicsPipeline,),
                                     ])
        self.addApplicationMenuSpec(menuSpec)

    #   self._patchInIntegrals()
    #
    #
    # def _patchInIntegrals(self):
    #   spectrumMenuPos = [i[0] for i in self._menuSpec].index('Spectrum')
    #   self._menuSpec[spectrumMenuPos][1].insert(4,
    #                                             ("Integrate",
    #                                              self.showIntegrationModule,
    #                                              [('shortcut', 'in'), ('enabled', False)]
    #                                             ))
    #
    #   viewMenuPos = [i[0] for i in self._menuSpec].index('View')
    #   self._menuSpec[viewMenuPos][1].insert(5,
    #                                         ("Integral Table",
    #                                          self.showIntegralTable,
    #                                          [('shortcut', 'it'),('enabled', False)])
    #                                         )
    #
    # from ccpn.ui.gui.widgets.Module import CcpnModule
    # def showIntegrationModule(self, position:str='bottom', relativeTo:CcpnModule=None):
    #   spectrumDisplay = self.ui.mainWindow.createSpectrumDisplay(self.project.spectra[0])
    #   from ccpn.AnalysisMetabolomics.Integration import IntegrationTable, IntegrationWidget
    #   spectrumDisplay.integrationWidget = IntegrationWidget(spectrumDisplay.module,
    #                                                         mainWindow=self.ui.mainWindow, grid=(2, 0), gridSpan=(1, 4))
    #   spectrumDisplay.integrationTable = IntegrationTable(spectrumDisplay.module,
    #                                                       project=self.project, grid=(0, 4), gridSpan=(3, 1))
    #   self.current.strip = spectrumDisplay.strips[0]
    #   if self.ui.mainWindow.blankDisplay:
    #     self.ui.mainWindow.blankDisplay.setParent(None)
    #     self.ui.mainWindow.blankDisplay = None
    #
    #
    # from ccpn.core.IntegralList import IntegralList
    # def showIntegralTable(self, position:str='bottom', relativeTo:CcpnModule=None, selectedList:IntegralList=None):
    #   logParametersString = "position={position}, relativeTo={relativeTo}, selectedList={selectedList}".format(
    #     position="'"+position+"'" if isinstance(position, str) else position,
    #     relativeTo="'"+relativeTo+"'" if isinstance(relativeTo, str) else relativeTo,
    #     selectedList="'" + selectedList + "'" if isinstance(selectedList, str) else selectedList,)
    #
    #   self._startCommandBlock('application.showIntegralTable({})'.format(logParametersString))
    #   try:
    #     self.ui.showIntegralTable(position=position, relativeTo=relativeTo, selectedList=selectedList)
    #   finally:
    #     self._endCommandBlock()

    def showMetabolomicsPipeline(self, position='bottom', relativeTo=None):
        from ccpn.ui.gui.modules.PipelineModule import GuiPipeline

        pipes = None
        mainWindow = self.ui.mainWindow
        guiPipeline = GuiPipeline(mainWindow=mainWindow, pipes=pipes)

        mainWindow.moduleArea.addModule(guiPipeline, position='bottom')
        mainWindow.pythonConsole.writeConsoleCommand("application.showMetabolomicsPipeline()")
        self.project._logger.info("application.showMetabolomicsPipeline()")

    def showDecompositionModule(self):
        """Opens the PCA module. if you need to get the PCA module or the Decomposition base class:
        get the specific instance from the current ccpnModules. This allows to have multiple PCA modules at the same time"""
        from ccpn.AnalysisMetabolomics.ui.gui.modules.PcaModule import PcaModule

        pcaModule = PcaModule(mainWindow=self.ui.mainWindow)
        self.ui.mainWindow.moduleArea.addModule(pcaModule, position='bottom')

    # This has not been implemented.
    # def showPeakFittingModule(self):
    #   from ccpn.AnalysisMetabolomics.PeakFitting import PeakFitting
    #   from ccpn.AnalysisMetabolomics.ui.gui.modules.PeakFittingModule import PeakFittingModule
    #
    #   self.peakFitting = PeakFitting(application=self)
    #   self.ui.peakFittingModule = PeakFittingModule(application=self,
    #                                                     interactor=self.peakFitting,
    #                                                     parent=self.ui)
    #   self.peakFitting.presenter = self.ui.peakFittingModule
    #   self.ui.mainWindow.moduleArea.addModule(self.ui.peakFittingModule.widget, position='bottom')
    #
    #   print('Interactive peak demo')
    #   # from application.metabolomics.presenters.peaks import InteractiveDemoPresenter
    #   from ccpn.AnalysisMetabolomics.ui.gui.modules.PeakFittingModule import InteractiveDemoPresenter
    #   self.peakDemoModule = InteractiveDemoPresenter(interactor=None,
    #                                                  parent=self,
    #                                                  project=self.project)
    #   self.ui.mainWindow.moduleArea.addModule(self.peakDemoModule.widget, position='bottom')
