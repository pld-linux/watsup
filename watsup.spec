#
Summary:	System resources monitor
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
Watsup monitors Linux system resources and the processes using those
resources. It is different from monitor programs you have seen before:

- Overhead is low, supporting a sample interval down to 0.1 seconds
- Overall system and top process resources are shown on one page
- CPU, memory, disk I/O, network I/O, and page faults are monitored
- The highest ranked processes fitting in the window are shown, with
  minimal jumping around between samples (easier to watch one or a few
  processes)
- Process rank is a weighted sum of CPU, hard page faults, and disk
  I/O over the last several samples (the weight of each sample declines
  with age)
- Font can be made large or small (for display in a corner of the
  screen)

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
