TOP=../..

include $(TOP)/configure/CONFIG

# -------------------------------
# Build a Diamond Support Module
# -------------------------------

LIBRARY_IOC += thorlabsMcls1

# xxxRecord.dbd will be installed into <top>/dbd
DBD += thorlabsMcls1.dbd

thorlabsMcls1_DBD += base.dbd
thorlabsMcls1_DBD += stream.dbd

# The following are compiled and added to the support library
thorlabsMcls1_LIBS += asyn
thorlabsMcls1_LIBS += stream
thorlabsMcls1_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
