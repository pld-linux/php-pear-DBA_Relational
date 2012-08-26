%define		_status		devel
%define		_pearname	DBA_Relational
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - Berkeley-style database abstraction class
Summary(pl.UTF-8):	%{_pearname} - abstrakcyjna klasa w stylu bazy danych Berkeley
Name:		php-pear-%{_pearname}
Version:	0.19
Release:	10
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	eab476d233ca303e6e13e3a01c221d59
URL:		http://pear.php.net/package/DBA_Relational/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.0.4-0.pl1
Requires:	php-pear
Requires:	php-pear-DBA
Obsoletes:	php-pear-DBA_Relational-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# included in tests package
%define		_noautoreq pear(empSchema.php) pear(hatSchema.php)

%description
Table management extension for DBA.

%description -l pl.UTF-8
Rozszerzenie klasy DBA do zarządzania tabelami.

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
%{php_pear_dir}/DBA/*.php
