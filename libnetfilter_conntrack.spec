#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD55D978A8A1420E4 (coreteam@netfilter.org)
#
Name     : libnetfilter_conntrack
Version  : 1.0.9
Release  : 22
URL      : https://www.netfilter.org/projects/libnetfilter_conntrack/files/libnetfilter_conntrack-1.0.9.tar.bz2
Source0  : https://www.netfilter.org/projects/libnetfilter_conntrack/files/libnetfilter_conntrack-1.0.9.tar.bz2
Source1  : https://www.netfilter.org/projects/libnetfilter_conntrack/files/libnetfilter_conntrack-1.0.9.tar.bz2.sig
Summary  : netfilter userspace conntrack access library
Group    : Development/Tools
License  : GPL-2.0
Requires: libnetfilter_conntrack-lib = %{version}-%{release}
Requires: libnetfilter_conntrack-license = %{version}-%{release}
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32libmnl)
BuildRequires : pkgconfig(32libnfnetlink)
BuildRequires : pkgconfig(libmnl)
BuildRequires : pkgconfig(libnfnetlink)

%description
libnetfilter_conntrack - userspace library for the connection tracking system
(C) 2005-2011 Pablo Neira Ayuso <pablo@netfilter.org>
=============================================================================

%package dev
Summary: dev components for the libnetfilter_conntrack package.
Group: Development
Requires: libnetfilter_conntrack-lib = %{version}-%{release}
Provides: libnetfilter_conntrack-devel = %{version}-%{release}
Requires: libnetfilter_conntrack = %{version}-%{release}

%description dev
dev components for the libnetfilter_conntrack package.


%package dev32
Summary: dev32 components for the libnetfilter_conntrack package.
Group: Default
Requires: libnetfilter_conntrack-lib32 = %{version}-%{release}
Requires: libnetfilter_conntrack-dev = %{version}-%{release}

%description dev32
dev32 components for the libnetfilter_conntrack package.


%package lib
Summary: lib components for the libnetfilter_conntrack package.
Group: Libraries
Requires: libnetfilter_conntrack-license = %{version}-%{release}

%description lib
lib components for the libnetfilter_conntrack package.


%package lib32
Summary: lib32 components for the libnetfilter_conntrack package.
Group: Default
Requires: libnetfilter_conntrack-license = %{version}-%{release}

%description lib32
lib32 components for the libnetfilter_conntrack package.


%package license
Summary: license components for the libnetfilter_conntrack package.
Group: Default

%description license
license components for the libnetfilter_conntrack package.


%prep
%setup -q -n libnetfilter_conntrack-1.0.9
cd %{_builddir}/libnetfilter_conntrack-1.0.9
pushd ..
cp -a libnetfilter_conntrack-1.0.9 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647925740
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1647925740
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libnetfilter_conntrack
cp %{_builddir}/libnetfilter_conntrack-1.0.9/COPYING %{buildroot}/usr/share/package-licenses/libnetfilter_conntrack/075d599585584bb0e4b526f5c40cb6b17e0da35a
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libnetfilter_conntrack/libnetfilter_conntrack.h
/usr/include/libnetfilter_conntrack/libnetfilter_conntrack_dccp.h
/usr/include/libnetfilter_conntrack/libnetfilter_conntrack_icmp.h
/usr/include/libnetfilter_conntrack/libnetfilter_conntrack_ipv4.h
/usr/include/libnetfilter_conntrack/libnetfilter_conntrack_ipv6.h
/usr/include/libnetfilter_conntrack/libnetfilter_conntrack_sctp.h
/usr/include/libnetfilter_conntrack/libnetfilter_conntrack_tcp.h
/usr/include/libnetfilter_conntrack/libnetfilter_conntrack_udp.h
/usr/include/libnetfilter_conntrack/linux_nf_conntrack_common.h
/usr/include/libnetfilter_conntrack/linux_nfnetlink_conntrack.h
/usr/lib64/libnetfilter_conntrack.so
/usr/lib64/pkgconfig/libnetfilter_conntrack.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libnetfilter_conntrack.so
/usr/lib32/pkgconfig/32libnetfilter_conntrack.pc
/usr/lib32/pkgconfig/libnetfilter_conntrack.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnetfilter_conntrack.so.3
/usr/lib64/libnetfilter_conntrack.so.3.8.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libnetfilter_conntrack.so.3
/usr/lib32/libnetfilter_conntrack.so.3.8.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libnetfilter_conntrack/075d599585584bb0e4b526f5c40cb6b17e0da35a
