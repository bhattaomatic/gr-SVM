INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_SVM SVM)

FIND_PATH(
    SVM_INCLUDE_DIRS
    NAMES SVM/api.h
    HINTS $ENV{SVM_DIR}/include
        ${PC_SVM_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    SVM_LIBRARIES
    NAMES gnuradio-SVM
    HINTS $ENV{SVM_DIR}/lib
        ${PC_SVM_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(SVM DEFAULT_MSG SVM_LIBRARIES SVM_INCLUDE_DIRS)
MARK_AS_ADVANCED(SVM_LIBRARIES SVM_INCLUDE_DIRS)

