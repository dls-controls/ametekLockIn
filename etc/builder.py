from iocbuilder import AutoSubstitution
from iocbuilder.modules.streamDevice import AutoProtocol

class ametekLockIn(AutoSubstitution, AutoProtocol):
    TemplateFile = 'ametekLockIn.template'
    ProtocolFiles = ['ametekLockIn.proto']
