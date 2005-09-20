%include	/usr/lib/rpm/macros.php
%define		_class		DBA
%define		_subclass	Relational
%define		_status		devel
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Berkeley-style database abstraction class
Summary(pl):	%{_pearname} - abstrakcyjna klasa w stylu bazy danych Berkeley
Name:		php-pear-%{_pearname}
Version:	0.19
Release:	4.2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	eab476d233ca303e6e13e3a01c221d59
URL:		http://pear.php.net/package/DBA_Relational/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# included in tests package
%define		_noautoreq 'pear(empSchema.php)' 'pear(hatSchema.php)'

%description
Table management extension for DBA.

%description -l pl
Rozszerzenie klasy DBA do zarz±dzania tabelami.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description tests
Tests for PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
