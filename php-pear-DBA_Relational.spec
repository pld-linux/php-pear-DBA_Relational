%include	/usr/lib/rpm/macros.php
%define         _class          DBA
%define         _subclass       Relational
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Berkeley-style database abstraction class
Summary(pl):	%{_pearname} - abstrakcyjna klasa w stylu bazy danych Berkeley
Name:		php-pear-%{_pearname}
Version:	0.19
Release:	3
License:	LGPL
Group:		Development/Languages/PHP
# Source0-md5:	eab476d233ca303e6e13e3a01c221d59
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Table management extension for DBA.

%description -l pl
Rozszerzenie klasy DBA do zarz±dzania tabelami.

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
