%global tl_name qrcode
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.51
Release:	%{tl_revision}.1
Summary:	Generate QR codes in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/qrcode
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/qrcode.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/qrcode.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/qrcode.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package generates QR (Quick Response) codes in LaTeX, without the
need for PSTricks or any other graphical package.

