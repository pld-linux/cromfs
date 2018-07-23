Summary:	Compressed ROM filesystem for Linux in user-space
Summary(pl.UTF-8):	System plików Compressed ROM dla Linuksa działający w przestrzeni użytkownika
Name:		cromfs
Version:	1.5.10.2
Release:	1
License:	GPL v3
Group:		Applications/System
#Source0Download: https://bisqwit.iki.fi/source/cromfs.html#download
Source0:	https://bisqwit.iki.fi/src/arch/%{name}-%{version}.tar.bz2
# Source0-md5:	5d69ebd1959e0b7273148d7bac84084b
URL:		https://bisqwit.iki.fi/source/cromfs.html
BuildRequires:	libfuse-devel >= 0:2.5.2
%if "%{cc_version}" >= "4.2"
BuildRequires:	libgomp-devel
%endif
BuildRequires:	libstdc++-devel
BuildRequires:	lzo-devel >= 2
BuildRequires:	rpmbuild(macros) >= 1.167
Requires:	libfuse-tools >= 2.5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cromfs is a compressed read-only filesystem for Linux. Cromfs is
intended for permanently archiving gigabytes of big files that have
lots of redundancy.

In terms of compression it is much similar to 7-zip files, except that
practical realtime access (albeit much slower than on most other
filesystems) can be provided for the whole archive contents; the user
does not need to launch a program to decompress a single file, nor
does he need to wait while the system decompresses 500 files from a
1000-file archive to get him the 1 file he wanted to open.

The creation of cromfs was inspired from Squashfs and Cramfs.

%description -l pl.UTF-8
cromfs to kompresowany system plików tylko do odczytu dla Linuksa.
Jest przeznaczony do trwałego archiwizowania gigabajtów dużych plików
o dużej redundancji.

Jeśli chodzi o kompresję, jest bardzo podobny do plików 7-zip, ale z
możliwością dostępu praktycznie w czasie rzeczywistym (choć dużo
wolniejszym, niż w przypadku większości innych systemów plików) do
całej zawartości archiwum; użytkownik nie musi uruchamiać programu do
dekompresji pojedynczego pliku ani czekać na zdekompresowanie 500
plików z 1000-plikowego archiwum, aby uzyskać 1 pożądany plik.

Stworzenie cromfs było zainspirowane systemami plików squashfs i
cramfs.

%prep
%setup -q

%build
./configure
%{__make} \
	CC="%{__cc}" \
	CPP="%{__cpp}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	CXXFLAGS="%{rpmcxxflags}" \
	OPTIM="%{rpmcflags}"

%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install cromfs-driver   $RPM_BUILD_ROOT%{_bindir}
install util/mkcromfs   $RPM_BUILD_ROOT%{_bindir}
install util/unmkcromfs $RPM_BUILD_ROOT%{_bindir}
install util/cvcromfs   $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/ChangeLog doc/FORMAT README.html
%attr(755,root,root) %{_bindir}/cromfs-driver
%attr(755,root,root) %{_bindir}/cvcromfs
%attr(755,root,root) %{_bindir}/mkcromfs
%attr(755,root,root) %{_bindir}/unmkcromfs
