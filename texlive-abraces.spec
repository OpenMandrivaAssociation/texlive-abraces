%global tl_name abraces
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2
Release:	%{tl_revision}.1
Summary:	Asymmetric over-/underbraces in maths
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/abraces
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/abraces.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/abraces.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a character key-driven interface to supplement new
constructions of the traditional \overbrace and \underbrace pairs in an
asymmetric or arbitrary way.

