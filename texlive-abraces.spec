Name:		texlive-abraces
Version:	64967
Release:	1
Summary:	Asymmetric over-/underbraces in maths
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/abraces
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abraces.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abraces.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a character key-driven interface to
supplement new constructions of the traditional \overbrace and
\underbrace pairs in an asymmetric or arbitrary way.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/abraces/abraces.sty
%doc %{_texmfdistdir}/doc/latex/abraces/abraces-doc.pdf
%doc %{_texmfdistdir}/doc/latex/abraces/abraces-doc.tex
%doc %{_texmfdistdir}/doc/latex/abraces/README.md

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
