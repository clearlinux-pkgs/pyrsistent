#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyrsistent
Version  : 0.17.3
Release  : 48
URL      : https://files.pythonhosted.org/packages/4d/70/fd441df751ba8b620e03fd2d2d9ca902103119616f0f6cc42e6405035062/pyrsistent-0.17.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/4d/70/fd441df751ba8b620e03fd2d2d9ca902103119616f0f6cc42e6405035062/pyrsistent-0.17.3.tar.gz
Summary  : Persistent/Functional/Immutable data structures
Group    : Development/Tools
License  : MIT
Requires: pyrsistent-license = %{version}-%{release}
Requires: pyrsistent-python = %{version}-%{release}
Requires: pyrsistent-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Patch1: 0001-tests.patch

%description
==========

%package license
Summary: license components for the pyrsistent package.
Group: Default

%description license
license components for the pyrsistent package.


%package python
Summary: python components for the pyrsistent package.
Group: Default
Requires: pyrsistent-python3 = %{version}-%{release}

%description python
python components for the pyrsistent package.


%package python3
Summary: python3 components for the pyrsistent package.
Group: Default
Requires: python3-core
Provides: pypi(pyrsistent)

%description python3
python3 components for the pyrsistent package.


%prep
%setup -q -n pyrsistent-0.17.3
cd %{_builddir}/pyrsistent-0.17.3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600111070
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyrsistent
cp %{_builddir}/pyrsistent-0.17.3/LICENCE.mit %{buildroot}/usr/share/package-licenses/pyrsistent/7c2cc2d536dfd9c7f5fa73b1814db5a6df797aa7
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyrsistent/7c2cc2d536dfd9c7f5fa73b1814db5a6df797aa7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
