Summary:	Compressed ROM filesystem for Linux in user-space
Summary(pl):	System plików Compressed ROM dla Linuksa dzia³aj±cy w przestrzeni u¿ytkownika
Name:		cromfs
Version:	1.1.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://bisqwit.iki.fi/src/arch/%{name}-%{version}.tar.bz2
# Source0-md5:	8c83b5ed2ea6cbc85e65ea88528ecd31
URL:		http://bisqwit.iki.fi/source/cromfs.html
BuildRequires:	libfuse-devel
BuildRequires:	libstdc++-devel
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

%description -l pl
cromfs to kompresowany system plików tylko do odczytu dla Linuksa.
Jest przeznaczony do trwa³ego archiwizowania gigabajtów du¿ych plików
o du¿ej redundancji.

Je¶li chodzi o kompresjê, jest bardzo podobny do plików 7-zip, ale z
mo¿liwo¶ci± dostêpu praktycznie w czasie rzeczywistym (choæ du¿o
wolniejszym, ni¿ w przypadku wiêkszo¶ci innych systemów plików) do
ca³ej zawarto¶ci archiwum; u¿ytkownik nie musi uruchamiaæ programu do
dekompresji pojedynczego pliku ani czekaæ na zdekompresowanie 500
plików z 1000-plikowego archiwum, aby uzyskaæ 1 po¿±dany plik.

Stworzenie cromfs by³o zainspirowane systemami plików squashfs i
cramfs.

%prep
%setup -q

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install cromfs-driver $RPM_BUILD_ROOT%{_bindir}
install util/mkcromfs $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/ChangeLog doc/FORMAT README.html
%attr(755,root,root) %{_bindir}/*
