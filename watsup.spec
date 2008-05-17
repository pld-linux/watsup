#
Summary:	Image editor and processor
Name:		watsup
Version:	09
Release:	1
License:	GPLv2
Group:		Applications
Source0:	http://kornelix.squarespace.com/storage/watsup/%{name}.%{version}.tar.gz
# Source0-md5:	52a7fb23dda3bf3890ece9a981dca729
URL:		http://kornelix.squarespace.com/watsup/
BuildRequires:	bash
BuildRequires:	gtk+2-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -n %{name}

%build
PREFIX=%{_prefix} bash ./build build

%install
rm -rf $RPM_BUILD_ROOT
PREFIX=$RPM_BUILD_ROOT%{_prefix} bash ./build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README changelog watsup-guide.pdf
%attr(755,root,root) %{_bindir}/watsup
%{_datadir}/watsup
