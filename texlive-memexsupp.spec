%global tl_name memexsupp
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Experimental memoir support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/memexsupp
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/memexsupp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/memexsupp.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package of code proposed as supporting material for memoir. The
package is intended as a test bed for such code, which may in the
fullness of time be adopted into the main memoir release.

