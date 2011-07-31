# TODO
# - system locale dirs
%define		status		stable
%define		pearname	Horde_SyncMl
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Horde_SyncMl provides an API for processing SyncML requests
Name:		php-horde-Horde_SyncMl
Version:	1.0.1
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	b5d14d3fca08b01787179ba45a3d3086
URL:		https://github.com/horde/horde/tree/master/framework/SyncMl/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Date < 2.0.0
Requires:	php-horde-Horde_Icalendar < 2.0.0
Requires:	php-horde-Horde_Log < 2.0.0
Requires:	php-horde-Horde_Support < 2.0.0
Requires:	php-horde-Horde_Translation < 2.0.0
Requires:	php-horde-Horde_Util < 2.0.0
Requires:	php-horde-Horde_Xml_Wbxml < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Requires:	php-pear-PEAR-core
Suggests:	php-horde-Horde_Auth
Suggests:	php-horde-Horde_Core
Suggests:	php-pear-MDB2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(Horde/Auth.*) pear(Horde/Core.*) pear(MDB2.*)

%description
This package provides classes for implementing a SyncML server.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%doc docs/Horde_SyncMl/*
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/SyncMl.php
%{php_pear_dir}/Horde/SyncMl
%{php_pear_dir}/data/Horde_SyncMl
