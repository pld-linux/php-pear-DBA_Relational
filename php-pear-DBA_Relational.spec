%include	/usr/lib/rpm/macros.php
%define         _class          DBA
%define         _subclass       Relational
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Berkeley-style database abstraction class
Summary(pl):	%{_pearname} - abstrakcyjna klasa w stylu bazy danych Berkeley
Name:		php-pear-%{_pearname}
Version:	0.19
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
Requires:	php-pear-DBA > 0.18
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Table management extension for DBA.

%description -l pl
Rozszerzenie klasy DBA do zarządzania tabelami.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{tests,docs/*}
%{php_pear_dir}/%{_class}/*.php
