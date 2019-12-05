#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyrsistent
Version  : 0.15.6
Release  : 40
URL      : https://files.pythonhosted.org/packages/6c/6f/c1a2e8da80a0029f6b618d7e20e1a6f2a61dd04e2e54225309c2cc4268f7/pyrsistent-0.15.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/6c/6f/c1a2e8da80a0029f6b618d7e20e1a6f2a61dd04e2e54225309c2cc4268f7/pyrsistent-0.15.6.tar.gz
Summary  : Persistent/Functional/Immutable data structures
Group    : Development/Tools
License  : MIT
Requires: pyrsistent-license = %{version}-%{release}
Requires: pyrsistent-python = %{version}-%{release}
Requires: pyrsistent-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : six
Patch1: 0001-tests.patch

%description
Pyrsistent
==========
.. image:: https://travis-ci.org/tobgu/pyrsistent.png?branch=master
:target: https://travis-ci.org/tobgu/pyrsistent

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

%description python3
python3 components for the pyrsistent package.


%prep
%setup -q -n pyrsistent-0.15.6
cd %{_builddir}/pyrsistent-0.15.6
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1574700934
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyrsistent
cp %{_builddir}/pyrsistent-0.15.6/LICENCE.mit %{buildroot}/usr/share/package-licenses/pyrsistent/7c2cc2d536dfd9c7f5fa73b1814db5a6df797aa7
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
