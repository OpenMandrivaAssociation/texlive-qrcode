Name:		texlive-qrcode
Version:	36065
Release:	2
Summary:	Generate QR codes in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/qrcode
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qrcode.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qrcode.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qrcode.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package generates QR (Quick Response) codes in LaTeX,
without the need for PSTricks or any other graphical package.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/qrcode
%{_texmfdistdir}/tex/latex/qrcode
%doc %{_texmfdistdir}/doc/latex/qrcode

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
