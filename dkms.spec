#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dkms
Version  : 3.0.6
Release  : 19
URL      : https://github.com/dell/dkms/archive/v3.0.6/dkms-3.0.6.tar.gz
Source0  : https://github.com/dell/dkms/archive/v3.0.6/dkms-3.0.6.tar.gz
Source1  : dkms-new-kernel.service
Source2  : dkms-remove-old.service
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: dkms-bin = %{version}-%{release}
Requires: dkms-data = %{version}-%{release}
Requires: dkms-license = %{version}-%{release}
Requires: dkms-man = %{version}-%{release}
Requires: dkms-services = %{version}-%{release}
Patch1: 0001-Add-script-to-run-autoinstall-on-new-kernel.patch
Patch2: 0002-Add-script-to-cleanup-modules-from-removed-kernels.patch

%description
Dynamic Kernel Module System (DKMS)
==
with tarballs which contain a dkms.conf file within them.

%package bin
Summary: bin components for the dkms package.
Group: Binaries
Requires: dkms-data = %{version}-%{release}
Requires: dkms-license = %{version}-%{release}
Requires: dkms-services = %{version}-%{release}

%description bin
bin components for the dkms package.


%package data
Summary: data components for the dkms package.
Group: Data

%description data
data components for the dkms package.


%package license
Summary: license components for the dkms package.
Group: Default

%description license
license components for the dkms package.


%package man
Summary: man components for the dkms package.
Group: Default

%description man
man components for the dkms package.


%package services
Summary: services components for the dkms package.
Group: Systemd services

%description services
services components for the dkms package.


%prep
%setup -q -n dkms-3.0.6
cd %{_builddir}/dkms-3.0.6
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1659484727
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}  dkms


%install
export SOURCE_DATE_EPOCH=1659484727
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dkms
cp %{_builddir}/dkms-3.0.6/COPYING %{buildroot}/usr/share/package-licenses/dkms/4cc77b90af91e615a64ae04893fdffa7939db84c
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/dkms-new-kernel.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/dkms-remove-old.service
## Remove excluded files
rm -f %{buildroot}*/var/lib/dkms/dkms_dbversion
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/
mkdir -p %{buildroot}/usr/bin
install -m0755 dkms-new-kernel.sh %{buildroot}/usr/bin/dkms-new-kernel.sh
install -m0755 dkms-remove-old.sh %{buildroot}/usr/bin/dkms-remove-old.sh
mkdir -p %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants
ln -sf ../dkms-new-kernel.service %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants/dkms-new-kernel.service
ln -sf ../dkms-remove-old.service %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants/dkms-remove-old.service
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/dkms/common.postinst
/usr/lib/dkms/dkms_autoinstaller

%files bin
%defattr(-,root,root,-)
/usr/bin/dkms
/usr/bin/dkms-new-kernel.sh
/usr/bin/dkms-remove-old.sh

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/dkms

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dkms/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/dkms.8.gz

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/dkms-new-kernel.service
/usr/lib/systemd/system/dkms-remove-old.service
/usr/lib/systemd/system/update-triggers.target.wants/dkms-new-kernel.service
/usr/lib/systemd/system/update-triggers.target.wants/dkms-remove-old.service
