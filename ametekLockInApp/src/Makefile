TOP=../..

include $(TOP)/configure/CONFIG

# -------------------------------
# Build an Diamond Support Module
# -------------------------------

LIBRARY_IOC += ametekLockIn

# xxxRecord.dbd will be installed into <top>/dbd
DBD += ametekLockIn.dbd

ametekLockIn_DBD += base.dbd
ametekLockIn_DBD += stream.dbd

# The following are compiled and added to the support library
ametekLockIn_LIBS += asyn
ametekLockIn_LIBS += stream
ametekLockIn_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
