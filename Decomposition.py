# NOT IN USE. ALL merged into PcaModule


# #=========================================================================================
# # Licence, Reference and Credits
# #=========================================================================================
# __copyright__ = "Copyright (C) CCPN project (http://www.ccpn.ac.uk) 2014 - 2017"
# __credits__ = ("Wayne Boucher, Ed Brooksbank, Rasmus H Fogh, Luca Mureddu, Timothy J Ragan & Geerten W Vuister")
# __licence__ = ("CCPN licence. See http://www.ccpn.ac.uk/v3-software/downloads/license",
#                "or ccpnmodel.ccpncore.memops.Credits.CcpnLicense for licence text")
# __reference__ = ("For publications, please use reference from http://www.ccpn.ac.uk/v3-software/downloads/license",
#                "or ccpnmodel.ccpncore.memops.Credits.CcpNmrReference")
# #=========================================================================================
# # Last code modification
# #=========================================================================================
# __modifiedBy__ = "$modifiedBy: CCPN $"
# __dateModified__ = "$dateModified: 2017-07-07 16:32:22 +0100 (Fri, July 07, 2017) $"
# __version__ = "$Revision: 3.0.0 $"
# #=========================================================================================
# # Created
# #=========================================================================================
# __author__ = "$Author: TJ Ragan $"
# __date__ = "$Date: 2017-04-07 10:28:45 +0000 (Fri, April 07, 2017) $"
# #=========================================================================================
# # Start of code
# #=========================================================================================
#
# from collections import OrderedDict
# import os
# import shutil
# import numpy as np
# import pandas as pd
#
# from ccpn.AnalysisMetabolomics.lib import normalisation
# from ccpn.AnalysisMetabolomics.lib import centering
# from ccpn.AnalysisMetabolomics.lib import scaling
# from ccpn.AnalysisMetabolomics.lib import decomposition
# from ccpn.AnalysisMetabolomics.lib.persistence import spectraDicToBrukerExperiment
# from ccpn.core.lib.Cache import cached
#
# from ccpn.core.lib.SpectrumLib import get1DdataInRange
# METABOLOMICS_SAVE_LOCATION = os.path.join('internal','metabolomics')
#
# class Decomposition:
#   """
#   Get the scores from console as dataframe: application.decomposition.model.scores_
#   """
#
#   def __init__(self, application, presenter=None):
#     self.project = application.project
#     self.__presenter = None
#     self.presenter = presenter
#
#     self.__sources = []
#     self.__normalization = None
#     self.__centering = None
#     self.__scaling = None
#     self.__decomp = None
#     self.__data = None
#
#     self.__sourcesChanged = True
#     self.__normChanged = True
#     self.__centChanged = True
#     self.__scalingChanged = True
#     self.__deScaleFunc = lambda x: x
#
#     self.availablePlotData = OrderedDict()
#
#     self.registerNotifiers()
#
#     self.method = 'PCA'
#     self.model = None
#     self.auto = False
#
#
#   # def __del__(self):
#   #   self.deRegisterNotifiers()
#
#
#   def registerNotifiers(self):
#     self.project.registerNotifier('Spectrum', 'create', self.refreshSourceDataOptions)
#     self.project.registerNotifier('Spectrum', 'change', self.refreshSourceDataOptions)
#     self.project.registerNotifier('Spectrum', 'rename', self.refreshSourceDataOptions)
#     self.project.registerNotifier('Spectrum', 'delete', self.refreshSourceDataOptions)
#     self.project.registerNotifier('SpectrumGroup', 'create', self.refreshSpectrumGroupFilter)
#     self.project.registerNotifier('SpectrumGroup', 'change', self.refreshSpectrumGroupFilter)
#     self.project.registerNotifier('SpectrumGroup', 'rename', self.refreshSpectrumGroupFilter)
#     self.project.registerNotifier('SpectrumGroup', 'delete', self.refreshSpectrumGroupFilter)
#
#
#   # def deRegisterNotifiers(self):
#   #   self.project._unregisterNotify(self.refreshSourceDataOptions, 'ccp.nmr.Nmr.DataSource', 'postInit')
#   #   self.project._unregisterNotify(self.refreshSourceDataOptions, 'ccp.nmr.Nmr.DataSource', 'delete')
#   #   self.project._unregisterNotify(self.refreshSourceDataOptions, 'ccp.nmr.Nmr.DataSource', 'setName')
#
#
#   @property
#   def presenter(self):
#     return self.__presenter
#
#   @presenter.setter
#   def presenter(self, value):
#     self.__presenter = value
#     if value is not None:
#       self.refreshSourceDataOptions()
#       self.refreshSpectrumGroupFilter()
#
#   @property
#   def method(self):
#     return self.__decomp
#
#   @method.setter
#   def method(self, value):
#     if value.upper() == 'PCA':
#       self.__decomp = value.upper()
#     else:
#       raise NotImplementedError('PCA is the only currently implemented decomposition method.')
#
#   # def reg(self):
#   #   project.allSpectra.register(self.refreshSourceDataOptions, 'new')
#
#   def refreshSourceDataOptions(self, *args):
#     if self.presenter is not None:
#       self.presenter.setSourceDataOptions(self.getSpectra())
#
#   def refreshSpectrumGroupFilter(self, *args):
#     if self.presenter is not None:
#       self.presenter.setSpectrumGroups(self.getSpectrumGroups())
#
#   def getSpectrumGroups(self):
#     sg = [s for s in self.project.spectrumGroups]
#     return sg
#
#   def getSpectra(self):
#     sd = []
#     sd += [s for s in self.project.spectra if
#               (len(s.axisCodes) == 1) and (s.axisCodes[0].startswith('H'))]
#     # if self.project.spectra:
#     #   raise Exception
#     # print(self.project.spectra)
#     # print(list([s.axisCodes for s in self.project.spectra]))
#     # print(sd)
#
#     return sd
#
#   def _getRawData(self):
#     return self.__data
#
#   @property
#   def normalization(self):
#     return self.__normalization
#
#   @normalization.setter
#   def normalization(self, value):
#     self.__normalization = value
#     # self.__normChanged = True
#     # self.__centChanged = True
#     # self.__scalingChanged = True
#     if self.auto:
#       self.decompose()
#
#   @property
#   def centering(self):
#     return self.__centering
#
#   @centering.setter
#   def centering(self, value):
#     self.__centering = value
#     # self.__centChanged = True
#     # self.__scalingChanged = True
#     if self.auto:
#       self.decompose()
#
#   @property
#   def scaling(self):
#     return self.__scaling
#
#   @scaling.setter
#   def scaling(self, value):
#     self.__scaling = value
#     # self.__scalingChanged = True
#     if self.auto:
#       self.decompose()
#
#   @property
#   def sources(self):
#     return self.__sources
#
#   @sources.setter
#   def sources(self, value):
#     self.__sources = value
#     # self.__sourcesChanged = True
#     # self.__normChanged = True
#     # self.__centChanged = True
#     # self.__scalingChanged = True
#     if self.auto:
#       self.decompose()
#
#   @cached('_buildSourceData', maxItems=256, debug=False)
#   def buildSourceData(self, sources, xRange=[-1,9]):
#     self.__sourcesChanged = False
#     sd = OrderedDict()
#
#     for d in sources:
#       spectrum = self.project.getByPid('SP:{}'.format(d))
#       x,y = get1DdataInRange(spectrum.positions, spectrum.intensities, xRange)
#       data = np.array([x,y])
#       sd[d] = data
#     l = [pd.Series(sd[name][1], name=name) for name in sorted(sd.keys())]
#     data = pd.concat(l, axis=1).T
#     data = data.replace(np.nan, 0)
#     self.__data =  data
#     return sources
#
#   def normalize(self):
#     if self.normalization.upper() == 'PQN':
#       self.__data = normalisation.pqn(self.__data)
#     elif self.normalization.upper() == 'TSA':
#       self.__data = normalisation.tsa(self.__data)
#     elif self.normalization.lower() == 'none':
#       pass
#     else:
#       raise NotImplementedError("Only PQN, TSA and 'none' type normalizations currently supported.")
#     # self.__normChanged = False
#
#
#   def center(self):
#     if self.centering.lower() == 'mean':
#       self.__data = centering.meanCenter(self.__data)
#     elif self.centering.lower() == 'median':
#       self.__data = centering.medianCenter(self.__data)
#     elif self.centering.lower() == 'none':
#       pass
#     else:
#       raise NotImplementedError("Only mean, median and 'none' type centerings currently supported.")
#     # self.__centChanged = False
#
#
#   def scale(self):
#     if self.scaling.lower() == 'pareto':
#       self.__data, self.__deScaleFunc = scaling.paretoScale(self.__data)
#     elif self.scaling.lower() == 'unit variance':
#       self.__data, self.__deScaleFunc = scaling.unitVarianceScale(self.__data)
#     elif self.scaling.lower() == 'none':
#       pass
#     else:
#       raise NotImplementedError("Only pareto, unit variance and 'none' type scalings currently supported.")
#     # self.__scalingChanged = False
#
#
#   def decompose(self):
#     if len(self.__sources) > 1:
#       # if self.__sourcesChanged:
#       #   self.buildSourceData()
#       # if self.__normChanged:
#       #   self.normalize()
#       # if self.__centChanged:
#       #   self.center()
#       # if self.__scalingChanged:
#       #   self.scale()
#       self.buildSourceData(self.__sources)
#       self.normalize()
#       self.center()
#       self.scale()
#       # self.__decomp -->   PCA decomposition
#       # decomposition -->  module 'ccpn.AnalysisMetabolomics.lib.decomposition
#       # self.__data --> intensities as array
#
#       data = self.__data.replace(np.nan, 0)
#
#       self.model = getattr(decomposition, self.__decomp)(data)
#       self.setAvailablePlotData()
#
#
#   def setAvailablePlotData(self):
#     defaults = OrderedDict()
#     if self.method == 'PCA':
#       self.availablePlotData = OrderedDict()
#       self.availablePlotData['Component #'] = list(range(len(self.model.scores_)))
#       self.availablePlotData['Explained Vairance'] = self.model.explainedVariance_
#       for score in self.model.scores_:
#         self.availablePlotData[score] = self.model.scores_[score].values
#
#
#       defaults['xDefaultLeft'] = 'Component'
#       defaults['yDefaultLeft'] = 'Explained Vairance'
#       defaults['xDefaultRight'] = 'PC1'
#       defaults['yDefaultRight'] = 'PC2'
#     else:
#       raise NotImplementedError('Only PCA output is currently supported.')
#     self.presenter.setAvailablePlotData(list(self.availablePlotData.keys()),
#                                         **defaults)
#
#
#   def saveLoadingsToSpectra(self, prefix='test_pca', descale=True, components=None):
#     saveLocation = os.path.join(self.project.path, METABOLOMICS_SAVE_LOCATION, 'pca', prefix)
#
#     sgNames = [sg.name for sg in self.project.spectrumGroups]
#     if prefix in sgNames:
#       g = self.project.getByPid('SG:' + prefix)
#     else:
#       g = self.project.newSpectrumGroup(prefix)
#       # TODO: Wayne: deleted spectra should be removed from spectrum groups!
#
#     toDeleteSpectra = [s for s in self.project.spectra if s.name.endswith(prefix)]
#     for s in toDeleteSpectra:
#       s.delete()
#     try:
#       shutil.rmtree(saveLocation)
#     except FileNotFoundError:
#       pass
#
#     if components is None:
#       # TODO: Generalize beyond PCA
#       components = self.model.loadings_
#
#     if descale:
#       components = components.apply(self.__deScaleFunc, axis=1)
#
#     spectraDicToBrukerExperiment(components, saveLocation)
#
#     loadingsSpectra = []
#     for d in next(os.walk(saveLocation))[1]:
#       loadedSpectrum = self.project.loadData(os.path.join(saveLocation, d))[0]
#       loadingsSpectra.append(loadedSpectrum)
#       newSpectrumName = loadedSpectrum.pid.split('-')[0][3:] + '-' + prefix
#       loadedSpectrum.rename(newSpectrumName)
#     g.spectra = loadingsSpectra
#
#
#   @property
#   def loadings(self):
#     return None
#
#   @property
#   def scores(self):
#     return None
