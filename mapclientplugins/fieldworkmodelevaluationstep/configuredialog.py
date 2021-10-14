from PySide2 import QtWidgets
from mapclientplugins.fieldworkmodelevaluationstep.ui_configuredialog import Ui_Dialog

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''


class ConfigureDialog(QtWidgets.QDialog):
    """
    Configure dialog to present the user with the options to configure this step.
    """

    def __init__(self, parent=None):
        """
        Constructor
        """
        QtWidgets.QDialog.__init__(self, parent)

        self._ui = Ui_Dialog()
        self._ui.setupUi(self)

        self._makeConnections()

    def _makeConnections(self):
        pass

    def accept(self):
        """
        Override the accept method so that we can confirm saving an
        invalid configuration.
        """
        result = QtWidgets.QMessageBox.Yes
        if not self.validate():
            result = QtWidgets.QMessageBox.warning(self, 'Invalid Configuration',
                                                   'This configuration is invalid.  Unpredictable behaviour may result if you choose \'Yes\', are you sure you want to save this configuration?)',
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes:
            QtWidgets.QDialog.accept(self)

    def validate(self):
        """
        Validate the configuration dialog fields.  For any field that is not valid
        set the style sheet to the INVALID_STYLE_SHEET.  Return the outcome of the
        overall validity of the configuration.
        """
        # Currently it's not possible for the configuration to be invalid. We may want to update this.
        return True

    def getConfig(self):
        """
        Get the current value of the configuration from the dialog.
        """
        config = {}
        config['discretisation'] = self._ui.lineEdit1.text()
        config['node coordinates'] = self._ui.lineEdit2.text() == 'True'
        config['elements'] = self._ui.lineEdit3.text()
        return config

    def setConfig(self, config):
        """
        Set the current value of the configuration for the dialog.
        """
        self._ui.lineEdit1.setText(config['discretisation'])
        self._ui.lineEdit2.setText(str(config['node coordinates']))
        self._ui.lineEdit3.setText(config['elements'])
